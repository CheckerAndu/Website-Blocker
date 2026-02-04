import time
from datetime import datetime

# The path to your Windows hosts file
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

# Where we redirect blocked sites (your own computer)
redirect = "127.0.0.1"

#Websites blocked
website_list = ["www.facebook.com", "facebook.com"]

while True:
    #Check current time
    if 9 <= datetime.now().hour < 14:
        print("Blocking Websites")

        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        print("Free time! Unblocking Websites")

        with open(hosts_path, "r+") as file:
            content = file.readlines()

            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(300)