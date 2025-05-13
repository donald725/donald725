import requests
from bs4 import BeautifulSoup
import re
#import csv

url = 'https://www.ameren.com/missouri/residential/lake-of-the-ozarks/lake-levels-and-operations'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extracting all links
#links = [a['href'] for a in soup.find_all('a', href=True)]

# Extracting all the text
all_text = soup.get_text()
#entries = re.split("\n+", all_text)
lakelevel = re.search(r"(Current.*)\n(\d\d.*)", all_text, re.MULTILINE)
temp = re.search(r"(Surface.*)\n(\d\d.*)", all_text, re.MULTILINE)

print (lakelevel.group(1))
print (lakelevel.group(2))
print (lakelevel)
print (temp.group(1))
print (temp.group(2))
print (temp)
#print (all_text)
#print (entries)
# Saving the extracted data to csv
# with open('data.csv', 'w', newline='', encoding='utf-8') as file:
#    writer = csv.writer(file)
#    writer.writerow(['Links', 'Text'])
#    writer.writerow([links, all_text])