# web-scraping-challenge
In this scraping challenge, there were three sources of information that I used to get data about Mars lates news,Mars facts, and Mars hemisphere images.  The sources are shown below:
a) https://mars.nasa.gov/news
b) https://space-facts.com/mars/
c) https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars

There were two main steps involved  Scraping and  MongiDB/Flask application.
Step 1: 

1.1 Initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

1.2 Created a Jupyter Notebook file called mission_to_mars.ipynb and used this to complete all of scraping and analysis tasks. 

1.3 Scraped Nasa Mars News and collected the latest news title, paragrapg text.  Assigned the text to variables that you can reference later.

1.4 Scraped JPL Mars Space Images - Featured Images
	1.4.1 Visit the url for JPL Featured Space Image
	1.4.2 Make sure to find the image url to the full size .jpg image.
	1.4.3 Make sure to save a complete url string for this image.

1.5 Scraped mars facts by visiting the Mars Facts webpage and used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc. Used Pandas to convert the data to a HTML table string.

1.6 Scraped Mars Hemispheres by visiting the USGS Astrogeology site to obtain high resolution images for each of Mar's hemispheres. Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

Step2:MongoDB and Flask Application
2.1 Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.


2.2 Start by converting Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that would executed all of your scraping code from above and return one Python dictionary containing all of the scraped data.


2.3 Created a route called /scrape that imported  scrape_mars.py script and call your scrape function.

2.4 Stored the return value in Mongo as a Python dictionary.



2.5 Created a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.


2.6 Created a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements. 






