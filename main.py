import time
import services
import dbconnect


creatService = ("Create Struture of work drive")
copyService = ("Copy Drive and PC")
retriveService = ("Retrive data for email")
insertEmail= ("Insert email to email list")
generalServiceInteract =("Selection Service \n 1-{} \n 2-{} \n 3-{}".format(creatService,copyService,insertEmail))
print (generalServiceInteract)
choiceUser= str(input("Select numer: "))

if choiceUser == "1":
    print ("You Select {} ".format(creatService))
    services.creatWorkstation()
if choiceUser == "2":
    print ("You Select {} ".format(copyService)) 
    services.copyFiles()
if choiceUser == "3":
    print ("You Select {} ".format(insertEmail))
    dbconnect.insert_email()    