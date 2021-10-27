# #strip and split usning list comprehensuion
# device1_str = " laddu , venkat ,venkat arjun "
# device1 = [item.strip() for item in device1_str.split(",")]
# print(" " , device1) 

import nmap
nm = nmap.PortScanner()
while True:
    ip = input("enter ip add")
    if not ip:
        break
    print(f"beginning of scan {ip}")
    output = nm.scan(ip,'22-1024')
    print(f"---command :{nmap.command_line()} ")
    print("OUTPUT")
    pprint(output)