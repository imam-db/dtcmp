# Web Scraping in Python

[link course](https://app.datacamp.com/learn/courses/web-scraping-with-python)

The ability to build tools capable of retrieving and parsing information stored across the internet has been and continues to be valuable in many veins of data science. In this course, you will learn to navigate and parse html code, and build tools to crawl websites automatically. Although our scraping will be conducted using the versatile Python library scrapy, many of the techniques you learn in this course can be applied to other popular Python libraries as well, including BeautifulSoup and Selenium. Upon the completion of this course, you will have a strong mental model of html structure, will be able to build tools to parse html code and access desired information, and create a simple scrapy spiders to crawl the web at scale. 


## [Introduction to HTML](./01_introduction_to_html/)

Learn the structure of HTML. We begin by explaining why web scraping can be a valuable addition to your data science toolbox and then delving into some basics of HTML. We end the chapter by giving a brief introduction on XPath notation, which is used to navigate the elements within HTML code. 

## [XPaths and Selectors](./02_xpaths_and_selectors/)

Leverage XPath syntax to explore scrapy selectors. Both of these concepts will move you towards being able to scrape an HTML document. 

## [CSS Locators, Chaining, and Responses](./03_css_locators_chaining_and_responses/)

Learn CSS Locator syntax and begin playing with the idea of chaining together CSS Locators with XPath. We also introduce Response objects, which behave like Selectors but give us extra tools to mobilize our scraping efforts across multiple websites. 

## [Spiders](./04_spiders/)

Learn to create web crawlers with scrapy. These scrapy spiders will crawl the web through multiple pages, following links to scrape each of those pages automatically according to the procedures we've learned in the previous chapters. 