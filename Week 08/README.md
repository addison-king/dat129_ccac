# Week 08 - Web Scraping

## Authors note: Please look at file "BG_DAT129_HW08_GR_SK.py" first. This file analyzes Stephen King on the goodreads website.
* This program searches the goodreads website for the term "Stephen King." It will also parse through pages of search results (i.e. page 1, page 2, etc).
* Once the html is BeautifulSouped, it finds all of the tags containing every search result. These results are then broken down further into usable pieces.
* RESULTS: Total-averaged average rating, total books, total votes for Stephen King.

## Authors note: The file "BG_DAT129_HW08_HTML_scraping.py" is an expansion project from the lecture.

---

### program objective
* Create a program that uses the urllib and BeautifulSoup to grab HTML code from a public source, parses that source into meaningful bits of data, and spits those meaningufl bits of data into some form that could be transfered into anothre tool, such as a CSV for slurping up into a Database, a JSON file for use in the web, etc.

### suggestions for good pages to parse
* Choose a website whose page content is retrieved with some sort of query, such as a URL-encoded search query. This will allow your system to programatically tinker with the results you get back, and can be scaled to process lots more data than just a single, static page.

* Pages with tables of data are great, since that allows us to loop over trees of page elements and procss their data one at a time

### use methods!
* When possible, please structure your code in discrete methods that accomplish a single task, returning useful values to the caller. This helps reduce code repetition, allows for modular re-use, and makes the code generally more readable than blobs of lines in a heap.