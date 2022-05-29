import Libraries.ConnectionUrl as connection
import Libraries.ExtractDate   as extract
import Libraries.DataframeWork as dfw
import Libraries.DownloadThumb as dt
import Libraries.ImageMagick   as image
# pandas: 
# BeautifulSoup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

class SearchHttp:

    connect=""
    extract=""
    dfwork=""

    def fromLink(self, url, nameInLink, writeCsv=False, sample=1):
        
        directoryName="folderOrigin"

        html = self.connect.returnHtmlUrl(url, timeDelay=5)
        
        arrayIds = self.extract.extractIdsWatch(html, nameInLink)[:sample]
        
        arrayImages = dt.DownloadThumb().ManagerThumbsVideos(arrayIds, directoryName=directoryName)

        arrayDissolved = image.ImageMagick().dissolving( directoryNameIn=directoryName, 
                                                directoryNameOut='ImageOut',
                                                fileNames=arrayIds
                                                )
        # print(arrayDissolved)
        image.ImageMagick().createGif(  dirMainOut='GifOut',
                                        dirArrayNameOut=arrayIds,
                                        array=arrayDissolved)

        # (arrayWatchsClean, 'folderOrigin')
        # df = self.ExtractDateBooks(arrayBooks)
        # self.dfwork.showDataFrame(df)
        # if(writeCsv): self.dfwork.writeDataFrame(df)

    def __init__(self):
        self.connect = connection.ConnectionUrl()
        self.extract = extract.ExtractDate()
        self.dfwork  = dfw.DataframeWork()
        self.connect.verifyHasConnection()


        # def fromCsv(self, path="", writeCsv=False):
        # dfRead     = dfwork.readDataFrame("list_of_trading_books.csv")
        # arrayBooks = dfRead["link"]
        
        # df = self.ExtractDateBooks(arrayBooks)
        # self.dfwork.showDataFrame(df)
        # if(writeCsv): self.dfwork.writeDataFrame(df)

        # fileOrigen=$"ImageIn/$file"
        # newFolderOut=$"ImageOut/$(StringSlip $file)"
        # mkdir $newFolderOut
        
        # echo Origen: $fileOrigen
        # echo Folder: $newFolderOut
        # echo resultado: $"$newFolderOut/$fileOrigen"
        
        #echo $"ImageOut/$folder/$(StringSlip $file)"
        # sequenceOfImage=""
        # result=$"$newFolderOut/$(StringSlip $file)_"
        # for i in $(seq 0 10 95); do
        #     sequenceOfImage=$"$sequenceOfImage $result$i.png"
        # done
        
        # fileOut=$newFolderOut.gif
        # fileGif=$"$COMMAND_CONVERT $sequenceOfImage $fileOut"
        # $fileGif
        