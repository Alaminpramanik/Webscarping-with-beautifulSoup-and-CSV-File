import csv #excel file
from urllib.request import urlopen  # web client
from bs4 import BeautifulSoup #Beautiful Soup is a  parsing HTML and XML documents.

#url web scrap from wwwamazon.com 
html=urlopen('https://en.wikipedia.org/wiki/Comparison_of_text_editors')

# parses html into a soup data structure to traverse html
soup= BeautifulSoup(html,'lxml')


# finds each table from the store page
table=soup.findAll('table',{'class':'wikitable'})[0]

# Finds all link tags "tr" from within the first div.
rows=table.findAll("tr")

# name the output file to write to local disk
csvfile= open('edittors.csv','wt', newline='')

# opens file, and writes headers
writer=csv.writer(csvfile)

## writes the dataset to file 
try:
    for row in rows:
        csvRow=[]
        for cell in row.findAll(['tr','td']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvfile.close()            
