from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time



def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path":r"C:\Users\pamta\bin\chromedriver"}
    return Browser("chrome", executable_path, headless=False)

def scrape_info():
    browser = init_browser()

    # Visit visitcostarica.herokuapp.com
    nasa_url = "https://mars.nasa.gov/news/"
    browser.visit(nasa_url)

    time.sleep(1)

    # Scrape page into Soup
    #html = browser.html
    #news_soup = bs(html, "html.parser")



#def scrape():
    #mars_data = {}
    #news_output = marsNews()
    #mars_data["mars_news"] = news_output[0]
    #mars_data["mars_paragraph"] = news_output[1]
    #mars_data["mars_image"] = marsImage()
    #mars_data["mars_facts"] = marsFacts()
    #mars_data["mars_hemisphere"] = marsHemisphere()
   
    #return mars_data


#def marsNews():
    #browser = init_browser()
    #news_url = "https://mars.nasa.gov/news/"
    #browser.visit(news_url)
    #html = browser.html
    #news_soup = bs(html, "html.parser")
    #article = news_soup.find("div", class_='list_text')
    #news_t = article.find("div", class_="content_title").text
    #news_p = news_soup.find("div", class_ ="article_teaser_body").text
    
    #news_output = [news_t,news_p]
    #return news_output
 
#def marsImage():
    #browser = init_browser()
    #jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    #browser.visit(jpl_url)
    
    #html = browser.html
    #image_soup = bs(html, "html.parser")
    #image = image_soup.find("img", class_="thumb")["src"]
    #featured_image_url='https://www.jpl.nasa.gov'+image

    #return featured_image_url
 
#def marsFacts():
    #browser = init_browser()
    #facts_url = "https://space-facts.com/mars/"
    #browser.visit(facts_url)
   
    #html = browser.html
    #facts_soup = bs(html, "html.parser")
   


    #mars_facts = pd.read_html(facts_url)
    #mars_facts = pd.DataFrame(mars_facts[1])
    #mars_facts.column = ['Des','Values']
    #mars_facts.set_index('Des')
    #mars_facts_html = mars_facts.to_html(header=True, index=True)
    #print(mars_facts_df_html)
    #return mars_facts_df_html

#def marsHemisphere():
    #browser = init_browser()
    #mars_hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    #browser.visit(mars_hemisphere_url)
    #html =browser.html
    #hemis_soup = bs(html, "html.parser")
    #mars_hemisphere = []

    #products = hemis_soup.find("div", class_ = "result-list")
    #hemispheres = products.find_all("div", class_="item")

    #for hem in hemispheres:
        #title = hem.find("h3").text
        #end_link = hem.find("a")["href"]
        #image_link = "https://astrogeology.usgs.gov/" + end_link    
        #browser = init_browser()
        #html = browser.html
        #soup=bs(html, "html.parser")
        #downloads = soup.find("div", class_="downloads")
        #image_url = downloads.find("a")["href"]
        #mars_hemisphere.append({"title": title, "img_url": image_url})

    #return mars_hemisphere








