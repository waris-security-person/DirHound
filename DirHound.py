import requests

banner = r"""
██████╗ ██╗██████╗     ██╗  ██╗ ██████╗ ██╗   ██╗███╗   ██╗██████╗ 
██╔══██╗██║██╔══██╗    ██║  ██║██╔═══██╗██║   ██║████╗  ██║██╔══██╗
██║  ██║██║██████╔╝    ███████║██║   ██║██║   ██║██╔██╗ ██║██║  ██║
██║  ██║██║██╔══██╗    ██╔══██║██║   ██║██║   ██║██║╚██╗██║██║  ██║
██████╔╝██║██║  ██║    ██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║██████╔╝
╚═════╝ ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═════╝ 

example http://google.com/ or http://google.com/                                                                 
"""
print(banner)

domain = input("Enter domain name: ")
file_name = input("Enter wordlist name: ")
f = open(file_name,"r")

for i in f.readlines():
    url = domain + i[0:len(i)-1]
    response = requests.get(url)
    if response.status_code == 200:
        print(url)

f.close()