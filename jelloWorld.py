from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.ca/Product/ProductList.aspx?Submit=StoreIM&Depa=1&Category=38'

# opening up connection in order to grab page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grabs each product
containers = page_soup.findAll("div", {"class": "item-info"})

# writing to csv file
filename = "firstWScrape.csv"
f = open(filename, "w") #w for write
headers = "brand, product_name, shipping\n"
f.write(headers)

for container in containers:

    brand = container.a.img["title"]

    title_container = container.findAll("a", {"class": "item-title"})
    product_name = title_container[0].text

    shipping_container = container.findAll("li", {"class": "price-ship"})
    shipping = shipping_container[0].text.strip()

    print("brand " + brand)
    print("product: " + product_name)
    print("shipping" + shipping)

    f.write(brand + "," + product_name.replace(",", "|") + "," + shipping + "\n")

f.close()
