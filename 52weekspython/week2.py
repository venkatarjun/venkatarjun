#a device in python
from pprint import PrettyPrinter, pprint
device = {
    "name ":"venkat",    #first item
    "vendor":"ciscp ",   #secind item
    "model":"GTA",       #third item
    "os":"linux",        #and so on
    "ip":"192.166.6..6.",
}
print(type(device))
#simple print

print("\n ------simple print")
print("device",device)
print("device name",device["name "])#refering key-value

print("device vendor",device["os"])



#preety print
print("\n--------------preety ptint-----")
pprint(device)
#not a bulid in function,need to import


#for loop

print("\n for loop using f string")
for key , value in device.items():
    print(f"{key:>16}  :  {value}")

