# ReviewScraper
Python script for scraping product reviews from flipkart.com

## Demo
![Flipkart Review Scaraper Demo](/demo.gif?raw=true "Flipkart Review Scaraper Demo")

## Requirements
* Beautiful Soup
* Selenium WebDriver

## Usage
* Install the requirements by running `pip install bs4 selenium`.
* Add geckodriver to the PATH. Follow these [instructions](http://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path).
* Put the link of the product in `site` variable inside the script.
* Run the script by running `python scrape.py`.
* Reviews will be saved in the file `review.txt`.
