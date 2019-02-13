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

	user1 = input("Enter your input: ")
	if user1 == 'up':
		func()
	elif user1 == 'n':
		next = user+1
		if next < index:
			userid(next)
		else:
			print ("this was the last input")
			# func()	
	elif user1 == 'p':
		next = user-1
		if next >= 0:
			userid(user-1)
		else:
			print ("index out of range")
			# func()
	elif user1 == 'b':
		print ('thanks for playing')
	else:
		print ("your input was wrong! please try again")
func()