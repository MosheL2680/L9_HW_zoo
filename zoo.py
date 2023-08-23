 # imports
from zooHelper import menu,Actions,terminal,load,save


# entery point
if __name__ == "__main__":
    terminal()
    load("animal.xml")
    menu()
    print("GoodBye:)")
    save("animal.xml")