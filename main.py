import json
import urllib2
import pickle
from bs4 import BeautifulSoup
import os

def image_link(url):
	json = download_json(url)
	links = []
	links = links + links_in_local_url(json)
	print(len(links))
	while json["user"]["media"]["page_info"]["has_next_page"]:
		end_cursor = json["user"]["media"]["page_info"]["end_cursor"]
		new_url = url+"&max_id="+end_cursor
		json = download_json(new_url)
		links = links + links_in_local_url(json)
		print(len(links))
		pass

	fi = open("links.sh",'w')
	number = 1
	for l in links:
		w = "wget "+l+" -O "+"%s"%number+".jpg"
		number = number+1
		fi.write(w)
		fi.write("\n")
	fi.close()
	print("Total number is  ")
	print(number-1)
	return links


def links_in_local_url(local_json):
	links = []
	for i in range(len(local_json["user"]["media"]["nodes"])):
		links.append(local_json["user"]["media"]["nodes"][i]["display_src"])
	# print(len(links))
	links = [item.encode('utf-8') for item in links]
	return links


def follow_this(data):
	follow = []
	for i in range(len(data["data"]["user"]["edge_followed_by"]["edges"])):
		follow.append(data["data"]["user"]["edge_followed_by"]["edges"][i]["node"]["username"])
	follow = [item.encode('utf-8') for item in follow]
	file_ = open("user_name.p",'w')
	pickle.dump(m,file_)
	file.close()
	pass

def download_json(url):
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page,"html5lib")
	main_json = soup.body.string
	main_json = json.loads(main_json)
	# print("filenames loaded")
	# links = image_link(disha)
	return main_json

def dowload(links,user__name):
	number = 1
	os.mkdir(user__name)
	os.chdir(user__name)
	for link in links:
		print("Downloading image : %d"%number)
		img = urllib2.urlopen(link)
		image_name = str(number)+".jpg"
		localFile = open(image_name, 'wb')
		localFile.write(img.read())
		localFile.close()
		number = number+1
	pass

user__name = "dishagram_1"
url = "http://www.instagram.com/"+user__name+"/?__a=1"
links = image_link(url)
dowload(links,user__name)
