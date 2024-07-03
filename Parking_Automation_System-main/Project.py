import cv2
from PIL import Image
from pytesseract import pytesseract
from pymongo import MongoClient
import datetime
import math

park_slots=100
def remove(string):
    return string.replace(" ", "")
def keep_first_line(input_string):
    lines = input_string.split('\n')
    first_line = lines[0] if len(lines) > 0 else ""
    result_string = first_line  
    return result_string


#Number Plate Recognisation
def capture():
    camera=cv2.VideoCapture(0)

    while True:
        _,image=camera.read()
        cv2.imshow('image',image)
        if cv2.waitKey(1)& 0xFF==ord('s'):
            cv2.imwrite('test1.jpg',image)
            break
    camera.release()
    cv2.destroyAllWindows()

    path_to_tesseract = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    image_path = "test1.jpg"
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(Image.open(image_path))
    return text


#MongoDB Database Connect
client = MongoClient('mongodb://localhost:27017')
db = client['Mrigyank']
collection = db['Parking']


#_______________________________________________________________________#


while(True):
    print("     \n=> Parking <= ")
    print("1 -> Enrty")
    print("2 -> Exit")
    print("")

    choice=int(input("Enter Choice : "))

    if(choice == 1):
        #Entry Intilization
        parking={}
        #print("=> Parking slots remaining : ",park_slots)
        #print("")

        #Capturing Number Plate And converting in storeable format
        num_plate=capture()
        temp=remove(num_plate)
        veh_num=keep_first_line(temp)

        print("Vehicle number = ", veh_num)
        result= input("Yes/No ?  ")
        print("")

        if((result != "Yes")):
            if((result != "yes")):
                num_plate = input("Enter Vehicle number :")
                temp=remove(num_plate)
                veh_num=keep_first_line(temp)
                print("")

        current_time = datetime.datetime.now()

        result = collection.find_one({'vehicle':veh_num})
        #If User is in Database
        if result:
            update = {"$set": {"time": current_time}}
            collection.update_one(result, update)
            print(f"Vehicle Number : {veh_num}")
            print(f"Name: {result['name']}")
            print(f"Phone Number: {result['mobile']}")

        #If user data is in the database
        else:
            name_cous = input("Name : ")
            cous_num = input("Mobile number : ")
            parking["vehicle"] = veh_num
            parking["name"] = name_cous
            parking["mobile"] = cous_num
            parking["time"] = current_time
            collection.insert_one(parking)
            print("Data entered successfully in Database")
        print("\n->BILLING RATES<-")
        print("Entry Time: %s:%s:%s" % (current_time.hour, current_time.minute, current_time.second))
        print("   20 rs/Hours ")
        print("____________________________________")
        park_slots=park_slots-1
        #Entry Completed


    elif(choice == 2):
        #Exit Intilization
        exit_num_plate= capture()
        temp=remove(exit_num_plate)
        exit_num=keep_first_line(temp)

        print("Vehicle number = ", exit_num)
        result= input("Yes/No ?  ")
        print("")

        if((result != "Yes")):
            if((result != "yes")):
                exit_num_plate = input("Enter Vehicle number :")
                temp=remove(exit_num_plate)
                exit_num=keep_first_line(temp)
                print("")

        result_exit = collection.find_one({'vehicle':exit_num})

        if result:
            exit_time = datetime.datetime.now()
            print("____________________________________")
            print(f"\nVehicle Number : {exit_num}")
            print(f"Name: {result_exit['name']}")
            print(f"Phone Number: {result_exit['mobile']}")
            entry_time = result_exit['time']

            #Calculating Bill
            time_difference = exit_time - entry_time
            temp=time_difference.total_seconds()/3600
            sec_temp=int(temp)
            print("Hours parked : ",sec_temp)

            #Updating Parkign Slots
            print("Total Cost = ",sec_temp*20)
            park_slots=park_slots+1
            print("____________________________________")

        else:
            print("Handeled Manually")
            park_slots=park_slots+1
