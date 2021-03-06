# TACTICAL HACKER -:- https://github.com/TacticalHacker
#Python Script to extract Profile Info from GitHub

import requests
from bs4 import BeautifulSoup

GitID = input("Enter GitHub username: ")
type(GitID)
try:
	# specify the url
	quote_page = 'https://github.com/'
	quote_page = quote_page + GitID

	# query the website and return the html to the variable 'page'
	page = requests.get(quote_page)

	# parse the html using beautiful soap and store in variable `soup`
	soup = BeautifulSoup(page.text, 'html.parser')
except:
	print("Please enter a valid GitHub username.")
	quit()

print("\n\nGITHUB PROFILE INFO OF "+ GitID + ": \n")

try:
	fullname_box = soup.find('span', attrs={'class': 'p-name vcard-fullname d-block overflow-hidden'})
	fullname = fullname_box.text.strip()
	print("FULLNAME: " + fullname)
except:
	print("Something went wrong while accessing Fullname!")

try:
	username_box = soup.find('span', attrs={'class': 'p-nickname vcard-username d-block'})
	username = username_box.text.strip()
	print("USERNAME: " + username)
except:
	print("Something went wrong while accessing Username!")

try:
	address_box = soup.find('span', attrs={'class': 'p-label'})
	address = address_box.text.strip()
	print("ADDRESS: " + address)
except:
	print("Something went wrong while accessing Address!")

try:
	repositories_box = soup.find('span', attrs={'class': 'Counter'})
	repositories = repositories_box.text.strip()
	print("REPOSITORIES: " + repositories)
except:
	print("Something went wrong while accessing Repositories!")

try:
	contribution_box = soup.find('h2', attrs={'class': 'f4 text-normal mb-2'})
	contribution = contribution_box.text
	print("OTHER ACTIVITIES: "+contribution)
except:
	print("Something went wrong while accessing Other Contributions!")



