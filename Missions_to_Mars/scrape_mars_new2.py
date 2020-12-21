#!/usr/bin/env python
# coding: utf-8

# ### Scraping Nasa's News

#dependencies
import os
import time
import pandas as pd
from bs4 import BeautifulSoup as bs
#from webdriver_manager.chrome import ChromeDriverManager
from splinter import Browser


#set-up splinter, pointing to the directory where chromedriver exists
def init_browser():
    executable_path = {"executable_path":r"C:\Users\pamta\bin\chromedriver"}
    return Browser("chrome", **executable_path, headless = False)

def scrape():
    mars_data = {}
    news_output = scrape_news_info()
    mars_data["mars_news"] = news_output[0]
    mars_data["mars_paragraph"] = news_output[1]
    mars_data["mars_image"] = scrape_image_info()
    mars_data["mars_facts"] = scrape_facts_info()
    mars_data["mars_hemisphere"] = scrape_mars_hemisphere()
   
    return mars_data


def scrape_news_info():
    browser = init_browser()
    
    #visit "https://mars.nasa.gov/news/"
    nasa_url = "https://mars.nasa.gov/news/"
    browser.visit(nasa_url)

    time.sleep(1)

    #scrape page into soup
    html = browser.html
    nasa_soup = bs(html, "html.parser")

    #latest News Title and Paragraph Text
    latest_news_title  = nasa_soup.find("div", class_='list_text')

    list_date = latest_news_title.find("div", class_="list_date").text
    news_title = latest_news_title.find("div", class_="content_title").text
    news_paragraph = latest_news_title.find("div", class_ ="article_teaser_body").text

    return(list_date,news_title,news_paragraph)

# JPL Mars Space Images - Featured Image
#URL of page to be scraped
def scrape_image_info():
    browser = init_browser()
    jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(jpl_url)
    time.sleep(1)
    html = browser.html
    jpl_img_soup = bs(html, "html.parser")

    image = jpl_img_soup.find("img", class_="thumb")["src"]
    featured_image_url = "https://www.jpl.nasa.gov" + image

    return(image,featured_image_url)


# ### Mars Facts
def scrape_facts_info():
    browser = init_browser()
    mars_facts_url = 'https://space-facts.com/mars/'
    browser.visit(mars_facts_url)
    time.sleep(1)

    # use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc
    mars_facts_data = pd.read_html(mars_facts_url)
    mars_facts_data

    mars_facts_df = mars_facts_data[0]
 
    #Use Pandas to convert the data to a HTML table string.
    mars_facts_html = mars_facts_df.to_html(header = False, index = False)
    return(mars_facts_html)

# ### Mars Hemispheres
#visit url
def scrape_mars_hemisphere():
    browser = init_browser()
    mars_hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(mars_hemisphere_url)
    time.sleep(1)
    html =browser.html
    hemis_soup = bs(html, "html.parser")

    mars_hemisphere = []

    products = hemis_soup.find("div", class_ = "result-list" )
    hemispheres = products.find_all("div", class_="item")

    for hemisphere in hemispheres:
        title = hemisphere.find("h3").text
        end_link = hemisphere.find("a")["href"]
        image_link = "https://astrogeology.usgs.gov/" + end_link    
        browser.visit(image_link)
        html = browser.html
        soup=bs(html, "html.parser")
        downloads = soup.find("div", class_="downloads")
        image_url = downloads.find("a")["href"]
        mars_hemisphere.append({"title": title, "img_url": image_url})


    return mars_hemisphere
