from enum import Enum
import xml.etree.ElementTree as ET
import os

# enam
class Actions(Enum):
    ADD = 1
    DELETE = 2
    PRINT = 3
    SEARCH = 4
    APDATE = 5
    EXIT = 6


# def the array var
animals =[]


# print menu and get user selection
def display_menu():
    for x in Actions:
        print(f"{x.value} - {x.name}")
    return Actions(int(input("inter your selection: ")))

# conect each selection to the accurate function
def menu():
    while True:
        user_selection = display_menu()
        if user_selection == Actions.ADD: add()
        if user_selection == Actions.DELETE: delete()
        if user_selection == Actions.PRINT: print(f"""there are corrently {len(animals)} animals on the list
    {animals}""")
        if user_selection == Actions.SEARCH: search()
        if user_selection == Actions.APDATE: apdate()
        if user_selection == Actions.EXIT: return

# add an item to list
def add():
    animals.append({f"name": input("inter name") , "age" : input("inter age"), "gender": input("inter gender")})

# search an item in the list
def search(): 
    if not animals:
        print("list is empty")
        return
    found_animal = None
    input_animal = input("Enter animal gender")
    for animal in animals:
        if animal["gender"] == input_animal:
            found_animal = animal
            print (found_animal)
    if found_animal == None:
        print("not found")
    return found_animal

# delete an item from list
def delete():    
    animal2del = search()  
    if animal2del != None: 
        animals.remove(animal2del)  
        print("was deleted")       

# apdate details of a specific item
def apdate():
    if not animals:
        print("No list")
        return
    animal2update = search()
    if animal2update:
        animal2update["name"] = input("Enter new name: ")
        animal2update["age"] = input("Enter new age: ")
        print("successfully updated")

# save list to XML when program end
def save(file_name):
    if animals:
        root = ET.Element("animals")
        for animal in animals:
            animal_elem = ET.SubElement(root, "animal")
            for key, value in animal.items():
                ET.SubElement(animal_elem, key).text = value
        
        tree = ET.ElementTree(root)
        tree.write(file_name)
        print("Data saved to animals.xml")
    else:
        print("No data to save")

# load list from XML (if exist) when program starts
def load(file_name):
    if os.path.exists(file_name):
        tree = ET.parse(file_name)
        root = tree.getroot()
        animals.clear()  # Clear the existing list before loading

        for animal_elem in root.findall("animal"):
            animal = {}
            for child in animal_elem:
                animal[child.tag] = child.text
            animals.append(animal)
               
        
# terminal - clear and change font name when program starts
def terminal():
    os.system("cls")
    os.system("color 09")
