from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017')
print(client)
db = client['Vidushi']
collection = db['Parking']

exit_num = input("Vehicle Number = ")

result = collection.find_one({'vehicle':exit_num})

print(f"Vehicle Number : {exit_num}")
print(f"Name: {result['name']}")
print(f"Phone Number: {result['mobile']}")

#exit_veh = collection.find_one({'vehicle':exit_num},{'vehicle':1 , '_id':0})
#exit_name = collection.find_one({'vehicle':exit_num},{'name':1 ,'_id':0})
#exit_number = collection.find_one({'vehicle':exit_num},{'mobile':1 ,'_id':0})

#print( exit_name)
#print( exit_veh)
#print( exit_number)
