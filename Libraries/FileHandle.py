import os

class FileHandle:

    def createDirectory(self, dirName):
        
        msgOut="Directory, {} {}".format(dirName, "already exists")
        if(not os.path.exists(dirName)):
            os.mkdir(dirName)
            msgOut=msgOut.format(dirName,"created")

        print(msgOut) 