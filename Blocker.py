import time
from datetime import datetime

# The path to your Windows hosts file
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com"]

def MainMenu():
    print("------------------------------------------")
    print("WELCOME TO WEBSITE BLOCKER")
    print("------------------------------------------\n" )
    time.sleep(1)
    print("1. Start Blocking")
    print("2. Exit")
    
    choice = input("What do you want to do?\n")
    if choice == "1":
        Block()

def Block():
    try:
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
        
        print("\nWebsites Blocked")    
        
        stop = input("Unblock the websites by typing stop: ").lower() 
        
        if stop == "stop":
            with open(hosts_path, "r+") as file:
                content = file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in website_list):
                        file.write(line)
                file.truncate()
            
            print("Websites Unblocked")
            time.sleep(2)
            MainMenu()
            
    except PermissionError:
        print("\n[ERROR]: You must run your terminal/editor as ADMINISTRATOR for it to work.")
        time.sleep(3)
        MainMenu()

MainMenu()