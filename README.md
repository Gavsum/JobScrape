## JobScrape Project

I started working on this project as a simple demo and to also yield some (hopefully) useful insights into the job market. Currently the aim is to scrape data from relevant job postings on carreerbeacon and then present the data visually.

## Libraries in use so Far
* Scrapy: Open source python frame work for scraping web pages https://scrapy.org/
* Scrapy-Splash: plugin for scrapy to render js based pages https://github.com/scrapy-plugins/scrapy-splash

## TODO
* Format scrapy output format into JSON like style for use in MongoDB
* Seperate functionallity in single spider into other python files (eg: use pipeline file for exporting tasks)
* Functionality (in pipeline) to reject poorly formatted results, or duds that have scrapped
* Implement wait times in spider to avoid accidentally DOS'ing a site
* Plan out use of other libraries 
 * MongoDB for results storage and ease of access 
 * Accessing MongoDB with NodeJS
 * Angular & Express or React or Electron(Desktop) for front end stuff
 * Using D3 to represent the keyword frequency visually (eg: most commonly requested skills) or any other useful visualizations
* After stack is figured out using low volume scrape results, scale up to scraping complete results
* Also implementing User input for ...
 * Job search keyword
 * Title keywords to accept / rejected in search results
 * Option to scrape other websites for similar data (probably not though)
