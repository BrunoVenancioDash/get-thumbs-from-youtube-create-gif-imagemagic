# author: Bruno Venâncio
# date: 21/03/2022

import Libraries.SearchHttp as sh

url = "https://www.youtube.com/"

linkInformation = sh.SearchHttp()
linkInformation.fromLink(url, nameInLink=['/watch?'],  writeCsv=False)

# linkInformation.fromCsv()