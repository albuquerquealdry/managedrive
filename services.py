import os
import time
def creatWorkstation():
    time.sleep(1)
    print (".")
    time.sleep(1)
    print(".")
    time.sleep(3)
    print ("Sucess")
    directoryWorkStation = r"C:\\Users\\BRYAN\\Desktop\\repositorio\\project\\WorkStation"
    os.mkdir(directoryWorkStation)
    directoryFiles= r"C:\\Users\\BRYAN\\Desktop\\repositorio\\project\\WorkStation\\Files"
    os.mkdir(directoryFiles)
    arquivo = open(r"C:\\Users\\BRYAN\\Desktop\\repositorio\\project\\WorkStation\\file1.py", 'a')
    arquivo.write ("")
    arquivo.close()
    arquivo = open(r"C:\\Users\\BRYAN\\Desktop\\repositorio\\project\\WorkStation\\file2.py", 'a')
    arquivo.write ("")
    arquivo.close()
    arquivo = open(r"C:\\Users\\BRYAN\\Desktop\\repositorio\\project\\WorkStation\\file3.py", 'a')
    arquivo.write ("")
    arquivo.close()
    arquivo = open(r"C:\\Users\\BRYAN\\Desktop\\repositorio\\project\\WorkStation\\Readme.txt", 'a')
    arquivo.write ("RENOMEIE E ULTILIZE OS ARQUIVOS")
    arquivo.close()