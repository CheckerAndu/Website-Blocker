import json
import time

with open('LinksDatabase.json', 'r') as BlockedFile:
    Links = json.load(BlockedFile)

while True:
    print("These are your blocked websites:" , ", ".join(Links))
    time.sleep(1)
    choice = input("1. Add another link 2. Remove a link\n")

    if choice == '1':
        NewLink = input("Paste the whished link:\n")
        time.sleep(1)
        if NewLink in Links:
            print(f"{NewLink} is already in your blocked links!")
            time.sleep(2)
            continue
        Links.append(NewLink)
        print("Link successfully added to your blocked links!")

    elif choice == '2':
        RemoveLink = input("Which link do you want to remove?:\n")
        time.sleep(1)
        if RemoveLink not in Links:
            print(f"{RemoveLink} is not in your blocked websites!")
            time.sleep(2)
            continue
        Links.remove(RemoveLink)
        print("Link successfully removed!")
    
    else:
        print("Error, please type 1 or 2!")
        time.sleep(2)
        continue
    
    time.sleep(2)
    quit = input("Do you wish to quit? y/n\n")
    if quit == 'y'.lower():
        with open('LinksDatabase.json', 'w') as BlockedFile:
            json.dump(Links, BlockedFile)
            time.sleep(2)
            print("Data Saved!")
            time.sleep(1)
            print("You can close the program!")

    