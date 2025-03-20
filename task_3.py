import requests

response = requests.get('https://randomuser.me/api/?results=500')
response.status_code

response.json()

response.json().keys()

data = response.json()["results"]
data
#Male and Female list 
gender =[item["gender"]for item in data]
print(gender)

#Male list
male_gender =[]
for identity in gender:
    if identity == "male":
        male_gender.append(identity)
print (male_gender)

#Female list
female_gender =[]
for identity in gender:
    if identity == "female":
        female_gender.append(identity)
print (female_gender)

#Extract Date of Birth(DOB)

dob = [item["dob"] ["date"]for item in data]
dob

#Concatenate first name and last name
names= [item["name"] for item in data]
names

full_name = [item["first"]+ " " + item["last"] for item in names]
full_name