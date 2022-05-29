# import pandas as pd
# from bs4 import BeautifulSoup

class ExtractDate(object):

    def splitHtml(self, data):
        data = data.replace('"',"'") # " => '
        data = data.replace(" ","'") # space => '
        data = data.split("'")
        
        return [data]

    def forCondition(self, data, nameInLink):
        array = []
        for line in data[0]:
            if(nameInLink in line):
                array.append(line)
        return array
    
    def searchListInHtml(self, data, arrayWordSearch=[]):
        arrayBooks=[]
        for word in arrayWordSearch:
            arrayBooks = self.forCondition(data, word) 
        return arrayBooks

    def sliptIdTransformation(self, idsVideo):
        arrayIds=[]
        for idVideoWatch in idsVideo:
            idVideo = idVideoWatch.split("=")
            idVideo = idVideo[1].split("\\")
            arrayIds.append(idVideo[0])
        return arrayIds

    def removeDuplicat(self, idsVideo):
        return list(set(idsVideo))
    
    def extractIdsWatch(self, html, arrayWordSearch):
        htmlSlpit  = self.splitHtml(html)
        arrayWatch = self.searchListInHtml(htmlSlpit, arrayWordSearch)
        arrayIds   = self.sliptIdTransformation(arrayWatch)
        arrayIdsClean = self.removeDuplicat(arrayIds)

        return arrayIdsClean