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
    if 9 <= datetime.now().hour < 10:
        print("Blocking Websites till 10 o'clock")
    else:
        print("Free time! Unblocking Websites")
    time.sleep(5)