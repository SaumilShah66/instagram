import pickle
import urllib2
from bs4 import BeautifulSoup as bs


def check_private(user_name):
	posts = []
	main = "http://www.instagram.com"
	link = main+"/"+user_name
	try:
		page = urllib2.urlopen(link)
		soup = bs(page,"html5lib")
		all_links = soup.find_all("a")
		if len(all_links)>=6:
			posts.append(main+str(all_links[0].get("href")))
			posts.append(main+str(all_links[1].get("href")))
		page.close()
		soup.clear()
	except:
		print("failed")
		pass
	return posts

users = pickle.load(open("user_name.p",'r'))
links_of_posts = []
n=1
for user in users:
	k = check_private(user)
	print("User checked : %d"%n)
	n=n+1
	links_of_posts = links_of_posts + k

file = open("macro.txt",'w')
for line in links_of_posts:
	file.write("URL GOTO="+line)
	file.write("\n")
	file.write("WAIT SECONDS=1 \nTAG POS=1 TYPE=A ATTR=TXT:Like")
file.close()




