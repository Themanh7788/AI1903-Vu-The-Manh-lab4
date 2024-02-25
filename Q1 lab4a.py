#1.Create a new empty text file named'sales.txt'
with open(sales.txt, 'w') as file:
    pass
#2.Create file with a date time:
import datetime
datetime_now = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
file = f"{datetime_now}.txt"
with open(file, 'w') as file:
    pass
#3.Create the file with permission:
import os
file = "sample.txt"
os.umask(0)
with open(os.open(file, os.0_CREAT | os.0_WRONLY, 7221),'w') as f:
    f.write('something')




