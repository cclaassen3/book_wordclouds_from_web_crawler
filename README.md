### Introduction to web crawling

This project is a web crawler implemented in Python using the Scrapy framework to crawl data about books on books.toscrape.com. It extracts the titles, descriptions, and categories/genres of books and stores them such that they can be indexed by the book category. To run the web crawler, run the following command from the current directory:

    ~:book_wordclouds_from_webcrawler user$ scrapy crawl book

This will store the extracted data in the data/ directory in text files corresponding to category.txt, where category refers to the book category/genre.

### Word cloud generator

To make use of the extracted data, I have implemented functionality to generate word clouds for each category based on the frequency of words in the titles and descriptions of the books belonging to that category. To generate a word cloud, run the following command from the current directory:

    ~:book_wordclouds_from_webcrawler user$ python wordcloud_generator.py

This will open a GUI that will list all the scraped book categories. You can then select a category and press the 'generate word cloud!' button and the script will close the GUI and display the word cloud image. With the default setting, it will also save the word cloud image to the wordclouds/ directory. Here is an example word cloud for the "Travel" category:

![alt text](https://github.com/cclaassen3/book_wordclouds_from_web_crawler/blob/master/wordclouds/Travel.jpg)
