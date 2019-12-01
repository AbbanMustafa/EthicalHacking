import requests
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import time


letters = 'abcdefghijklmnopqrstuvwxyz'
major = 'computer+science'



f = open("emails.txt", "a")


for char in letters:

	url = 'https://directory.utexas.edu/advanced.php?aq%5BName%5D='+char+'&aq%5BCollege%2FDepartment%5D='+major+'&aq%5BTitle%5D=&aq%5BEmail%5D=&aq%5BHome+Phone%5D=&aq%5BOffice+Phone%5D=&scope=all'

	request = requests.get(url)

	soup = BeautifulSoup(request.content, 'html5lib')

	table = soup.find('div', attrs = {'id':'aresults'}) 
	print(soup.prettify)

	for row in table.find_all('li'):
		# row = table.find_all('li')[0]
		time.sleep(5)
		newRequest = requests.get('https://directory.utexas.edu/'+row.a['href'])
		person = BeautifulSoup(newRequest.content, 'html5lib')
		# print(person.prettify)
		person_table = person.find('table', attrs = {'class':'dir_info'})
		name = person_table.find_all('td')[1].get_text().split(",")[0].lstrip()
		email = person_table.find_all('td')[3].a['href'].split(":")[1].lstrip()

		print(name+","+email)
		f.write(name+","+email+"\n")

	time.sleep(60)
# print(soup.prettify)

f.close()
