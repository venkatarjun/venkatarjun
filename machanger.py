#!bin/python3
import subprocess #module
import optparse   #module
#new type of input insted of a  = imput(enter numer) beacuse this will be more secure


def get_arguments():
    parser = optparse.OptionParser()    #parser is varibale(child)(object),Optionparser is a class 
                                        #class always starts with captil letter 
    parser.add_option("-i" , "--interface",dest="interface",help="interface to its mac address")
    parser.add_option("-m", "--mac",dest="new_mac",help="new mac address")#.add_option is a method
    (options,arguments) = parser.parse_args()   #allows the able to undersyanf the user input
    if not options.interface:     #options are eth0 ,and arugements are -i
        parser.error("plz specify thr interface")
    elif not options.new_mac:
        parser.error("pz specfiy thr  mac")
    return options


def change_mac(interface,new_mac):
    print("changing mac address for the interface" + interface + "to "+new_mac)
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface, "hw","ether",new_mac])
    subprocess.call(["ifconfig",interface,"up"])

    
options = get_arguments()
change_mac(options.interface,options.new_mac)
