import time
import services

creatService = ("Create Struture of work drive")
copyService = ("Copy Drive and PC")
retriveService = ("Retrive data for email")
cloneService= ("Clone drive for drive")
generalServiceInteract =("Selection Service \n 1-{} \n 2-{} \n 3-{}".format(creatService,copyService,cloneService))
print (generalServiceInteract)
choiceUser= str(input("Select numer: "))

if choiceUser == "1":
    print ("You Select {} ".format(creatService))
    services.creatWorkstation()
if choiceUser == "2":
    print ("You Select {} ".format(copyService)) 
    services.copyFiles()
if choiceUser == "3":
    print ("You Select {} ".format(cloneService))    