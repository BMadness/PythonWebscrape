
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
#URL I want to scrape
my_url= 'https://www.newegg.com/p/pl?Submit=StoreIM&Depa=1&Category=9&PageSize=96'

#grabs and downloads webpage
uClient = uReq(my_url)
#html file for the page that has been scraped
page_html = uClient.read()
#close the client's connection to the webpage
uClient.close()

#parse the html file and save it as a parsed html file
page_soup = soup(page_html, "html.parser")

#looking at different elements
print ("page header 1: \n%s" % page_soup.h1)
print ("page divider: \n%s" % page_soup.div)

#all products are in 'item-containers' so we check for all of them
containers = page_soup.findAll("div" , {"class":"item-container"})
print ("number of containers found: %d" % len(containers))

filename = "products.csv"

f = open(filename, "w")
headers = "brand, product_name, shipping\n"

f.write(headers)

for container in containers:

    brand_container = container.find("a", {"class": "item-brand"})

    brand = brand_container.img["title"]

    title_container = container.find("a", {"class":"item-title"})
    title = title_container.text.strip()

    shipping_container = container.find("li", {"class" : "price-ship"})
    shipping_price = shipping_container.text.strip()

    print("brand " + brand)
    print("title " + title)
    print("shipping " + shipping_price)

    f.write(brand + "," + title.replace(",", "|") + "," + shipping_price + "\n")

f.close()

