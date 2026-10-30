# dtcmp

Personal study notes for DataCamp courses. Folder and checklist structure follows public course, chapter, and lesson **titles** so you can track progress and write your own notes. Content in this repository is original study material (or empty placeholders for it). **Not affiliated with DataCamp.** Do not copy course body text, exercises, solutions, videos, or PDFs from DataCamp into this repo.

## Purpose

- Keep a local outline of courses you care about (career tracks plus a broader catalog).
- Use title-only checklists as a scaffold for notes, synthetic exercises, and solutions written in your own words.
- Plan learning with the unofficial catalog and learning-path indexes.

## Repository layout

### Career-track indexes (existing course folders)

| Track | Index |
|---|---|
| Data Analyst with Python | [`README_data_analyst_with_python.md`](./README_data_analyst_with_python.md) |
| Data Engineer | [`README_data_engineer.md`](./README_data_engineer.md) |
| Python Programmer | [`README_python_programmer.md`](./README_python_programmer.md) |
| Others | [`README_others.md`](./README_others.md) |

Course material that already lived in the repo sits in **snake_case folders at the repo root** (for example `introduction_to_python/`). Many of those folders include a `lessons.md` checklist and chapter subfolders for your own notes.

### Broader module outlines (`modules/`)

Outlines for the remaining catalog courses (not covered by the data-engineering progress index) live under:

```text
modules/<topic>/<course_slug>/
  README.md      # title + DataCamp link + pointer to lessons.md
  lessons.md     # chapter/lesson title checklist with empty note placeholders
```

Topics include applied finance, AI, cloud, data engineering, visualization, machine learning, programming, and more. See [`MODULES_ALL.md`](./MODULES_ALL.md) for the full index.

### Planning indexes

| File / folder | What it is |
|---|---|
| [`catalog/`](./catalog/) | Unofficial public DataCamp catalog (names + URLs; snapshot 2026-10-30) |
| [`learning-paths/data-engineering.md`](./learning-paths/data-engineering.md) | 19-course data engineering outline |
| [`MODULES.md`](./MODULES.md) | Data engineering progress index (19 courses · `lessons.md` per course) |
| [`MODULES_ALL.md`](./MODULES_ALL.md) | Index of the other 757 course checklists under `modules/` (and a few root folders) |
| [`CAVEATS.md`](./CAVEATS.md) | Known thin or awkward outlines (for example Introduction to Power BI) |
| [`REMOVED_ASSETS.md`](./REMOVED_ASSETS.md) | Record of DataCamp-owned PDFs and copied prose removed from the working tree |

## How to use the checklists

1. Open a course folder (root track folder or `modules/<topic>/<slug>/`).
2. Open that course's `lessons.md` and tick items as you go.
3. Under each lesson, fill **Notes (own words)**, **Exercise (synthetic data)**, and **Solution** yourself.
4. Use synthetic data only. Prefer original wording over anything from the platform.

Example shape of a generated checklist:

```markdown
## Chapter 1: …

### Lesson title

- [ ] Notes (own words)
- [ ] Exercise (synthetic data)
- [ ] Solution
```

## Regenerating module outlines

Source snapshot: a titles-only `lessons_all.txt` (course / chapter / lesson headings and URLs). Generator:

```bash
python3 scripts/generate_module_outlines.py /path/to/lessons_all.txt
```

Defaults: source `/workspace/datacamp-de/lessons_all.txt`, repo root = parent of `scripts/`. The script is idempotent, skips the 19 courses already tracked in `MODULES.md`, writes/updates `lessons.md` files, refreshes `MODULES_ALL.md`, `CAVEATS.md`, and `scripts/generate_module_outlines_stats.json`.

## Removed assets

DataCamp chapter PDFs and copied course-description prose were deleted from the working tree. Paths are listed in [`REMOVED_ASSETS.md`](./REMOVED_ASSETS.md). Those blobs may still exist in older git history; rewriting history or changing visibility is a separate decision.

## Disclaimer

This repository is a personal study aid. Course, chapter, and lesson titles and public URLs are used only for navigation and planning. It is not an official DataCamp product, mirror, or redistribution of DataCamp content.
