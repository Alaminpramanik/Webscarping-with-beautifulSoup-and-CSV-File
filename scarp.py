import csv #excel file
from urllib.request import urlopen as uReq # web client
from bs4 import BeautifulSoup as soup #data stracture

#url web scrap from www.startech.com.bd
my_url= 'https://www.startech.com.bd/component/graphics-card'

#openning up connecting ,grabing the page url
uClient=uReq(my_url)

# parses html into a soup data structure to traverse html
# as if it were a json data type.
page_soup = soup(uClient.read(),"html.parser")
uClient.close()


#grabe each product store page
containers=page_soup.findAll('div',{'class':'row main-content'})

#loops over each product and grabs attributes about
container=containers[0]
#print(container.div.img['alt'])

# finds each product from the store page
product_container=container.findAll('h4',{'class':'product-name'})
#product(product_container[0].text)

# finds each product from the store page
price_container=container.findAll('div',{'class':'price'})
#price(price_container[0].text)

# name the output file to write to local disk
filename= "products.csv"

# opens file, and writes headers unicode
f=open(filename,"w",encoding='utf-8')
# header of csv file to be written
headers = ("brand ,product_name, price'\n" )
f.write(headers)

#for loops over each product and grabs attributes about container
for container in containers:
	
	brand=container.div.img['alt']

	# Finds all link tags "a" from within the first div.
	product_container=container.findAll('h4',{'class':'product-name'})
	product_name=product_container[0].text

	 # Grabs the div from the price
	price_container=container.findAll('div',{'class':'price'})
	price=price_container[0].text.strip()

	 # prints the dataset to console
	print("brand: " + brand +'\n')
	print("product_name: " + product_name +'\n')
	print("price: " + price +'\n')

	 # writes the dataset to file
	f.write(brand+ "," +product_name.replace(",","|") + "," + price + "\n")
f.close() # Close the file








