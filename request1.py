import requests
import json
from os import path

def func():
	exist = path.exists("courses.json")
	if exist:
		with open("courses.json", "r") as f:
			c = json.load(f)
			availableCourses=c["availableCourses"]
			index=0
			id_dict = {}

			for i in availableCourses:
				a=i['name']
				z=i['id']
				id_dict[index] = z
				print (index,a,z)
				index=index+1
			user=int(input("enter the number: "))
			userid(user)
	else:
		url="http://saral.navgurukul.org/api/courses"
		a=requests.get(url)
		b=a.text
		with open("courses.json", "w") as f:
			f.write(b)

def userid(user):
	index=0
	id_dict = {}

	with open("courses.json", "r") as f:
		c = json.load(f)
		availableCourses=c["availableCourses"]
	for i in availableCourses:
		a=i['name']
		z=i['id']
		id_dict[index] = z
		index=index+1
	# print (index)
	link="http://saral.navgurukul.org/api/courses/" +str(id_dict[user])+ "/exercises"
	print (link)
	mainid = id_dict[user]
	var=requests.get(link)
	var1=var.text
	var3 = json.loads(var1)
	# print (type(var3))

	data=var3["data"]
	count = 0
	print(data)
func()
