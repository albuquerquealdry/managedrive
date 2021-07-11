import os
import subprocess
import shutil
from datetime import date
import time
def creatWorkstation():
    directoryWay= input("Past you directory Way :  ")
    time.sleep(1)
    print (".")
    time.sleep(1)
    print(".")
    time.sleep(3)
    print ("Sucess")
    directoryWorkStation = directoryWay+"\\Workstation"
    os.mkdir(directoryWorkStation)
    directoryFiles= directoryWay+"\\WorkStation\\Files"
    os.mkdir(directoryFiles)
    arquivo = open(directoryWay+"\\WorkStation\\file1.py", 'a')
    arquivo.write ("")
    arquivo.close()
    arquivo = open(directoryWay+"\\WorkStation\\file2.py", 'a')
    arquivo.write ("")
    arquivo.close()
    arquivo = open(directoryWay+"\\WorkStation\\file3.py", 'a')
    arquivo.write ("")
    arquivo.close()
    arquivo = open(directoryWay+"\\WorkStation\\Readme.txt", 'a')
    arquivo.write ("RENOMEIE E ULTILIZE OS ARQUIVOS")
    arquivo.close()

def copyFiles():
    directory= input("Select name directory: ")
    orig = input("Directory past: ")
    dest = input("Directory way:")+"\\"+directory
    shutil.copytree(orig, dest)
    time.sleep(3)
    print ("Sucess")