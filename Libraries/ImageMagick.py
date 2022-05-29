import os
import Libraries.FileHandle as fh

class ImageMagick:    

    def dissolving( self, 
                    directoryNameIn, 
                    directoryNameOut,
                    fileNames, 
                    imageBeDissolved="base/youtube.png"):
        
        if (len(fileNames)==0): raise "Error, there is no image base"
        if (len(imageBeDissolved)==0): raise "Error, there is no image to be dissolved"
        fh.FileHandle().createDirectory(directoryNameOut)
        
        arrayOut=[]

        for fileName in fileNames:
            mkdirDirectoryOut = "{}/{}".format(directoryNameOut, fileName[:-4])
            # print("mkdirDirectoryOut: {}\n".format(mkdirDirectoryOut))
            fh.FileHandle().createDirectory(mkdirDirectoryOut)

            fileOrigen='{}/{}.jpg'.format(directoryNameIn,fileName)
            
            arrayOutFile=[]
            for i in range(0, 100, 20):
                fileOut="{}/{}_{}.png".format(mkdirDirectoryOut, fileName, i )
                # print(fileOut)
                imageOut="composite -blend {} -gravity Center {} {} {}".format(i,imageBeDissolved, fileOrigen, fileOut)
                os.system(imageOut)
                # print(imageOut)
                arrayOutFile.append(fileOut)    
            arrayOut.append(arrayOutFile)

        return arrayOut    
    
    def createGif(self, dirMainOut, dirArrayNameOut, array, delay=20, loop=0):

        command="convert -delay {} -loop {} -dispose Background".format(delay,loop)
        fh.FileHandle().createDirectory(dirMainOut)
        
        for folder in dirArrayNameOut:
            print()
            # mkFolderGif="{}/{}".format(dirMainOut, folder)
            # fh.FileHandle().createDirectory(mkFolderGif)
            
            listDissolved = array[dirArrayNameOut.index(folder)]
            
            # command in imagemagick
            sequenceOfImage= " ".join(listDissolved)
            fileOut="{}/{}.gif".format(dirMainOut,folder)

            #listOfCommands = 
            commandOut = " ".join([command, sequenceOfImage, fileOut])
            
            # print(listOfCommands)
            print(commandOut)
            os.system(commandOut)
        

    # def mergeThumbsWithYoutube(self, imagesDissolved, dirName):

    #     for file in imagesDissolved:
    #         fh.FileHandle().createDirectory(mkdirDirectoryOut)
    #         self.acessFolder('gifs')
            #for idVideo in arrayIdVideo[:5]:
            #    self.acessFolder(idVideo)
            #    for i in range(5):
            #        idVideo
