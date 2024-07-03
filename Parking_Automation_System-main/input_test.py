from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017')
print(client)
db = client['Vidushi']
collection = db['Parking']

parking={}
veh_num = input("Vehicle Number = ")
name_cous = input("Name = ")
cous_num = input("Mobile number = ")

parking["vehicle"] = veh_num
parking["name"] = name_cous
parking["mobile"] = cous_num

collection.insert_one(parking)
