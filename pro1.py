import time
from datetime import datetime as dt

host_temp="hosts"
host_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.xvideos.com","xvideos.com","www.pornhub.com","pornhub.com","xnxx.com","www.xnxx.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,0) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,23):
        print("Dont watch God is watching")
        with open(host_path,'r+') as file:
             content=file.read()
             for website in website_list:
                 if website in content:
                     pass
                 else:
                     file.write(redirect+" "+website+"\n")
    else:
        with open(host_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("help your self and read the bible")
    time.sleep(5)
