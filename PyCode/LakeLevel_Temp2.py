import requests
from bs4 import BeautifulSoup
import re
#import csv

#url = 'https://www.ameren.com/missouri/residential/lake-of-the-ozarks/lake-levels-and-operations'
url = 'https://www.ameren.com/property/lake-of-the-ozarks/reports'
#url = 'https://www.python.org'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extracting all links
#links = [a['href'] for a in soup.find_all('a', href=True)]

# Extracting all the text
all_text = soup.get_text()
#entries = re.split("\n+", all_text)
reportdate = re.search(r"(Report.*)\n(\d\d.*)", all_text, re.MULTILINE)
lakelevel = re.search(r"(Current.*)\n(\d\d.*)", all_text, re.MULTILINE)
temp = re.search(r"(Surface.*)\n(\d\d.*)", all_text, re.MULTILINE)

print (reportdate.group(1)+"  "+reportdate.group(2))
print (lakelevel.group(1)+"  "+lakelevel.group(2))
#print (lakelevel.group(2))
#print (lakelevel)
print (temp.group(1)+"  "+temp.group(2))
#print (temp.group(2))
#print (temp)
#print (all_text)
#print (entries)
# Saving the extracted data to csv
# with open('data.csv', 'w', newline='', encoding='utf-8') as file:
#    writer = csv.writer(file)
#    writer.writerow(['Links', 'Text'])
#    writer.writerow([links, all_text])