import json
import time

with open('LinksDatabase.json', 'r') as BlockedFile:
    Website = json.load(BlockedFile)

while True:
    print("These are your blocked websites:" , ", ".join(Website))
    time.sleep(1)
    choice = input("1. Add another link 2. Remove a link\n")

    if choice == '1':
        NewWeb = input("Paste the whished Website:\n")
        time.sleep(1)
        if Website in Website:
            print(f"{NewWeb} is already in your blocked links!")
            time.sleep(2)
            continue
        Website.append(NewWeb)
        print("Link successfully added to your blocked links!")

    elif choice == '2':
        RemoveLink = input("Which website do you want to remove?:\n")
        time.sleep(1)
        if RemoveLink not in Website:
            print(f"{RemoveLink} is not in your blocked websites!")
            time.sleep(2)
            continue
        Website.remove(RemoveLink)
        print("Link successfully removed!")
    
    else:
        print("Error, please type 1 or 2!")
        time.sleep(2)
        continue
    
    time.sleep(2)
    quit = input("Do you wish to quit? y/n\n")
    if quit == 'y'.lower():
        with open('LinksDatabase.json', 'w') as BlockedFile:
            json.dump(Website, BlockedFile)
            time.sleep(2)
            print("Data Saved!")
            time.sleep(1)
            print("You can close the program!")

    