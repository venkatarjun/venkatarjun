#!bin/python3
import subprocess #module
import optparse 
import re  #module
#new type of input insted of a  = imput(enter numer) beacuse this will be more 
# 
#secure

def get_arguments():
    parser = optparse.OptionParser() #parser is varibale(child)(object),Optionparser is a class 
    #class always starts with captil letter 
    parser.add_option("-i" , "--interface",dest="interface",help="interface to its mac address")
    parser.add_option("-m", "--mac",dest="new_mac",help="new mac address")#.add_option is a method
    return parser.parse_args()

def change_mac(interface,new_mac):
    print("changing mac address for the interface" + interface + "to "+new_mac)
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface, "hw","ether",new_mac])
    subprocess.call(["ifconfig",interface,"up"])
(options,arguments) = get_arguments()
change_mac(options.interface,options.new_mac)

