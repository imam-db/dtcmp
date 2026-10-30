#!/usr/bin/env python3
"""Generate lesson checklists for DataCamp courses.

Reads a titles-only snapshot (lessons_all.txt), writes a lessons.md checklist
per course, plus a grouped index (MODULES_ALL.md) and stats JSON. Idempotent:
running twice produces byte-identical files.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

SNAPSHOT = "2026-10-30"

SKIP_SLUGS = {
    "understanding-data-engineering",
    "introduction-to-sql",
    "intermediate-sql",
    "joining-data-in-sql",
    "introduction-to-relational-databases-in-sql",
    "database-design",
    "data-warehousing-concepts",
    "introduction-to-snowflake-sql",
    "understanding-data-visualization",
    "intro-to-python-for-data-science",
    "introduction-to-python",
    "intermediate-python",
    "introduction-to-importing-data-in-python",
    "intermediate-importing-data-in-python",
    "understanding-cloud-computing",
    "cleaning-data-in-python",
    "writing-efficient-python-code",
    "streamlined-data-ingestion-with-pandas",
    "introduction-to-git",
    "software-engineering-principles-in-python",
}

SKIP_TITLES = {
    "Understanding Data Engineering",
    "Introduction to SQL",
    "Intermediate SQL",
    "Joining Data in SQL",
    "Introduction to Relational Databases in SQL",
    "Database Design",
    "Data Warehousing Concepts",
    "Introduction to Snowflake SQL",
    "Understanding Data Visualization",
    "Introduction to Python",
    "Intermediate Python",
    "Introduction to Importing Data in Python",
    "Intermediate Importing Data in Python",
    "Understanding Cloud Computing",
    "Cleaning Data in Python",
    "Writing Efficient Python Code",
    "Streamlined Data Ingestion with pandas",
    "Introduction to Git",
    "Software Engineering Principles in Python",
}

FOLDER_ALIASES = {
    "understanding-data-engineering": "understand_data_engineering",
    "writing-efficient-python-code": "writing_eficient_python_code",
    "exploratory-data-analysis-in-python": "exploratory_data_anaylisis_in_python",
    "big-data-fundamentals-with-pyspark": "big_data_fundamental_with_pyspark",
    "intro-to-python-for-data-science": "introduction_to_python",
    "analyze-police-activity-with-pandas": "analyzing_police_activity_with_pandas",
    # Current DataCamp slugs → existing track folder names in this repo
    "web-scraping-with-python": "web_scraping_in_python",
    "introduction-to-relational-databases-in-python": "introduction_to_databases_in_python",
    "introduction-to-using-mongodb-for-data-science-with-python": "introduction_to_mongodb_in_python",
    "introduction-to-apache-airflow-in-python": "introduction_to_airflow_in_python",
}

COURSE_RE = re.compile(r"^# (.*) \((https?://[^)]+)\)\s*$")
CHAPTER_RE = re.compile(r"^## (.*)$")
LESSON_RE = re.compile(r"^- (.*)$")
NUMBERED_DIR_RE = re.compile(r"^\d{2}_.+$")
NUMBERED_PREFIX_RE = re.compile(r"^\d{2}_")


def slugify_topic(topic: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "_", topic.lower()).strip("_")
    return slug or "other"


def normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def parse_source(path: Path) -> list[dict]:
    courses: list[dict] = []
    current: dict | None = None
    for line in path.read_text(encoding="utf-8").splitlines():
        match = COURSE_RE.match(line)
        if match:
            title, url = match.groups()
            current = {
                "title": title,
                "url": url,
                "slug": url.rstrip("/").split("/")[-1],
                "chapters": [],
            }
            courses.append(current)
            continue
        if current is None:
            continue
        match = CHAPTER_RE.match(line)
        if match:
            current["chapters"].append({"title": match.group(1), "lessons": []})
            continue
        match = LESSON_RE.match(line)
        if match and current["chapters"]:
            current["chapters"][-1]["lessons"].append(match.group(1))
    return courses


def load_topics(catalog_path: Path) -> dict[str, str]:
    topics: dict[str, str] = {}
    with catalog_path.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            if row.get("type") != "course":
                continue
            slug = row["url"].rstrip("/").split("/")[-1]
            topics[slug] = (row.get("topic") or "").strip()
    return topics


def numbered_subdirs(folder: Path) -> list[str]:
    if not folder.is_dir():
        return []
    return sorted(
        child.name
        for child in folder.iterdir()
        if child.is_dir() and NUMBERED_DIR_RE.match(child.name)
    )


def chapter_heading(index: int, title: str, subdirs: list[str]) -> str:
    if subdirs:
        target = normalize(title)
        matches = [
            name
            for name in subdirs
            if normalize(NUMBERED_PREFIX_RE.sub("", name)) == target
        ]
        linked = matches[0] if len(matches) == 1 else None
        if linked is None and index < len(subdirs):
            linked = subdirs[index]
        if linked is not None:
            return f"## Chapter {index + 1}: [{title}](./{linked}/)"
    return f"## Chapter {index + 1}: {title}"


def render_lessons(course: dict, subdirs: list[str]) -> str:
    lines = [
        f"# {course['title']} — lesson checklist",
        "",
        f"Reference (titles only; unofficial): [{course['title']}]({course['url']})",
        "",
        "Write all notes, exercises, and solutions in your own words. Use synthetic data only.",
        "",
        "Placeholders under each lesson:",
        "",
        "- Notes (own words)",
        "- Exercise (synthetic data)",
        "- Solution",
        "",
    ]
    for index, chapter in enumerate(course["chapters"]):
        lines.append(chapter_heading(index, chapter["title"], subdirs))
        lines.append("")
        for lesson in chapter["lessons"]:
            lines.extend(
                [
                    f"### {lesson}",
                    "",
                    "- [ ] Notes (own words)",
                    "- [ ] Exercise (synthetic data)",
                    "- [ ] Solution",
                    "",
                ]
            )
    return "\n".join(lines).rstrip("\n") + "\n"


def render_readme(course: dict) -> str:
    return (
        f"# {course['title']}\n\n"
        "Unofficial study outline (titles only). Not affiliated with DataCamp.\n\n"
        f"- DataCamp: [{course['title']}]({course['url']})\n"
        "- Lesson checklist: [`lessons.md`](./lessons.md)\n\n"
        "Write notes in your own words. Use synthetic data only.\n"
    )


def write_if_changed(path: Path, content: str) -> bool:
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def render_index(entries: list[dict]) -> str:
    by_topic: dict[str, list[dict]] = defaultdict(list)
    for entry in entries:
        by_topic[entry["topic"] or "Other"].append(entry)

    lines = [
        "# All modules index",
        "",
        (
            f"Progress checklist for the remaining {len(entries)} DataCamp courses. "
            "Each course folder has a `lessons.md` with **chapter and lesson titles only** "
            f"(snapshot {SNAPSHOT}). Not affiliated with DataCamp."
        ),
        "",
        (
            "Generated by [`scripts/generate_module_outlines.py`](./scripts/generate_module_outlines.py). "
            "The 19 data engineering courses tracked in [`MODULES.md`](./MODULES.md) are not included."
        ),
        "",
    ]

    number = 0
    for topic in sorted(by_topic, key=str.casefold):
        lines.extend(
            [
                f"## {topic}",
                "",
                "| # | Course | Folder | Chapters | Lessons | Done |",
                "|---|---|---|---:|---:|:---:|",
            ]
        )
        for entry in sorted(
            by_topic[topic],
            key=lambda item: (item["course"]["title"].casefold(), item["slug"]),
        ):
            number += 1
            chapters = len(entry["course"]["chapters"])
            lessons = sum(len(chapter["lessons"]) for chapter in entry["course"]["chapters"])
            folder = entry["folder"].as_posix() + "/"
            label = "existing" if entry["root"] else "new"
            lines.append(
                f"| {number:02d} | {entry['course']['title']} | "
                f"[`{folder}`](./{folder}) ({label}) | {chapters} | {lessons} | [ ] |"
            )
        lines.append("")

    total_chapters = sum(len(entry["course"]["chapters"]) for entry in entries)
    total_lessons = sum(
        len(chapter["lessons"])
        for entry in entries
        for chapter in entry["course"]["chapters"]
    )
    lines.append(
        f"**Totals:** {len(entries)} courses · {total_chapters} chapters · {total_lessons} lessons"
    )
    return "\n".join(lines).rstrip("\n") + "\n"


def render_caveats(entries: list[dict]) -> str:
    project_guidance = sum(
        1
        for entry in entries
        for chapter in entry["course"]["chapters"]
        if chapter["title"] == "Project Guidance"
    )
    power_bi = next(
        (entry for entry in entries if entry["slug"] == "introduction-to-power-bi"),
        None,
    )
    power_bi_line = "- Introduction to Power BI is thin"
    if power_bi is not None:
        chapters = len(power_bi["course"]["chapters"])
        lessons = sum(len(chapter["lessons"]) for chapter in power_bi["course"]["chapters"])
        power_bi_line = (
            f"- **Introduction to Power BI** (`{power_bi['folder'].as_posix()}/`) is thin: "
            f"the current page layout yielded only {chapters} chapters / {lessons} lessons. "
            "Needs a manual check."
        )

    return (
        "# Caveats\n\n"
        f"{power_bi_line}\n"
        "- **Intermediate Python** has truncated lesson titles (\"Dictionaries, Part\", "
        "\"Pandas, Part\", \"Loop Data Structures Part\"). It is skipped here because PR #1 "
        "already covers it; mention this when regenerating.\n"
        f"- {project_guidance} chapters across the remaining courses use the title "
        "\"Project Guidance\" (project-style courses).\n"
        "- No lesson titles ending in \", Part\" remain in the generated set; the truncated "
        "ones are in the skipped Intermediate Python course.\n"
    )


def update_root_readme(repo_root: Path) -> bool:
    readme = repo_root / "README.md"
    if not readme.exists():
        return False
    text = readme.read_text(encoding="utf-8")
    if "MODULES_ALL.md" in text:
        return False
    anchor = (
        "- [`MODULES.md`](./MODULES.md) — data engineering progress index "
        "(`lessons.md` checklists per course)"
    )
    link = (
        "- [`MODULES_ALL.md`](./MODULES_ALL.md) — index of all remaining DataCamp course "
        "checklists (grouped by topic)"
    )
    if anchor in text:
        text = text.replace(anchor, anchor + "\n" + link, 1)
    else:
        text = text.rstrip("\n") + "\n" + link + "\n"
    readme.write_text(text, encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "source",
        nargs="?",
        default="/workspace/datacamp-de/lessons_all.txt",
        help="Path to lessons_all.txt",
    )
    parser.add_argument(
        "--repo-root",
        default=str(Path(__file__).resolve().parents[1]),
        help="Repository root (default: parent of scripts/)",
    )
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    source = Path(args.source)
    topics = load_topics(repo_root / "catalog" / "datacamp-catalog.csv")
    courses = parse_source(source)

    managed: list[dict] = []
    skipped = 0
    for course in courses:
        if course["slug"] in SKIP_SLUGS or course["title"] in SKIP_TITLES:
            skipped += 1
            continue
        topic = topics.get(course["slug"], "")
        root_folder = FOLDER_ALIASES.get(course["slug"], course["slug"].replace("-", "_"))
        root_path = repo_root / root_folder
        if root_path.is_dir():
            folder = Path(root_folder)
            is_root = True
        else:
            folder = Path("modules") / slugify_topic(topic) / course["slug"].replace("-", "_")
            is_root = False
        managed.append(
            {
                "course": course,
                "slug": course["slug"],
                "topic": topic or "Other",
                "folder": folder,
                "root": is_root,
            }
        )

    lessons_created = 0
    lessons_updated = 0
    readmes_added = 0
    for entry in managed:
        folder = repo_root / entry["folder"]
        subdirs = numbered_subdirs(folder)
        lessons_path = folder / "lessons.md"
        existed = lessons_path.exists()
        if write_if_changed(lessons_path, render_lessons(entry["course"], subdirs)):
            if existed:
                lessons_updated += 1
            else:
                lessons_created += 1
        if not entry["root"]:
            readme_path = folder / "README.md"
            if not readme_path.exists():
                folder.mkdir(parents=True, exist_ok=True)
                readme_path.write_text(render_readme(entry["course"]), encoding="utf-8")
                readmes_added += 1

    index_content = render_index(managed)
    write_if_changed(repo_root / "MODULES_ALL.md", index_content)
    write_if_changed(repo_root / "CAVEATS.md", render_caveats(managed))
    update_root_readme(repo_root)

    total_chapters = sum(len(entry["course"]["chapters"]) for entry in managed)
    total_lessons = sum(
        len(chapter["lessons"])
        for entry in managed
        for chapter in entry["course"]["chapters"]
    )
    root_count = sum(1 for entry in managed if entry["root"])
    stats = {
        "snapshot": SNAPSHOT,
        "source": source.name,
        "skipped_courses": skipped,
        "managed_courses": len(managed),
        "chapters": total_chapters,
        "lessons": total_lessons,
        "root_folders": root_count,
        "module_folders": len(managed) - root_count,
        "lessons_files": len(managed),
        "topics": dict(sorted(Counter(entry["topic"] for entry in managed).items())),
    }
    stats_path = repo_root / "scripts" / "generate_module_outlines_stats.json"
    write_if_changed(stats_path, json.dumps(stats, indent=2, ensure_ascii=False) + "\n")

    print(f"Source: {source}")
    print(f"Skipped courses: {skipped}")
    print(f"Managed courses: {len(managed)}")
    print(f"Chapters: {total_chapters}")
    print(f"Lessons: {total_lessons}")
    print(f"lessons.md created: {lessons_created}, updated: {lessons_updated}")
    print(f"Root folders reused: {root_count}")
    print(f"Module folders: {len(managed) - root_count}")
    print(f"Course READMEs added: {readmes_added}")
    print(f"Index: {repo_root / 'MODULES_ALL.md'}")
    print(f"Stats: {stats_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
