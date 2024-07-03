'''from datetime import datetime 

start = "2:13:57"
end = "11:46:38"


time1 = datetime.strptime("6:20:50", "%H:%M:%S") 
print('Start time is :', time1.time()) 

time2 = datetime.strptime("11:56:18", "%H:%M:%S") 
print('End time is :', time2.time()) 


delta = time2 - time1 


print("Time difference in seconds is", delta.total_seconds(), "seconds")
print(delta.total_seconds()/3600)

import datetime

e = datetime.datetime.now()

print ("Current date and time = %s" % e)

print ("The time is now: = %s:%s:%s" % (e.hour, e.minute, e.second))'''

import datetime
import time
import math

# Record the first time
start_time = datetime.datetime.now()
time.sleep(2)
end_time = datetime.datetime.now()

time_difference = end_time - start_time
sec_temp=time_difference.total_seconds()
sec=int(sec_temp)
#time_difference=math.trunc(time_difference)

# Print the results
print(f"Start time: {start_time}")
print(f"End time: {end_time}")
print(f"Time difference: {sec_temp}")
