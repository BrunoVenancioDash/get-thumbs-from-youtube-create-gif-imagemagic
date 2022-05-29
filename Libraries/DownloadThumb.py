import Libraries.ConnectionUrl as connection
import Libraries.FileHandle    as fh

class DownloadThumb:

    def downloadThumb(self, idWatch, directoryName):
        connect = connection.ConnectionUrl()
        filesName = str(idWatch)
        linkOfThumb = 'https://img.youtube.com/vi/{filesName}/maxresdefault.jpg'
        linkToDownloadThumb = linkOfThumb.format(filesName=filesName)
        
        print(linkToDownloadThumb)
        
        dateImagem = connect.returnHtmlUrl(linkToDownloadThumb, thumb=True)
        
        path='{}/{}.jpg'.format(directoryName,filesName)
        try:
            imagem = open(path, 'wb')
            imagem.write(dateImagem)
            imagem.close()
            print("image salved in {}\n".format(path))
        except:
            print("Some error happened {}\n".format(linkOfThumb))



    def ManagerThumbsVideos(self, arrayIdVideo, directoryName):
        arrayImages=[]
        fh.FileHandle().createDirectory(directoryName)
        for idWatch in arrayIdVideo:
            print(idWatch)
            path = self.downloadThumb(idWatch, directoryName=directoryName)
            arrayImages.append(path)

        print("List of Thumbs download and Saved, Sucessful\n")
        return arrayImages
