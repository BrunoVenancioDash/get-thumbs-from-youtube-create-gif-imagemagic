from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
import time

class ConnectionUrl(object):

    def verifyHasConnection(self,timeout=5):
        try:
            response = urlopen("http://www.google.com", timeout=timeout).read()
        except HTTPError as error:
            print('HTTP Error: Data of %s not retrieved because %s\nURL: %s', name, error, url)
        except URLError as error:
            if isinstance(error.reason, timeout):
                print('Timeout Error: Data of %s not retrieved because %s\nURL: %s', name, error, url)
            else:
                print('URL Error: Data of %s not retrieved because %s\nURL: %s', name, error, url)
        else:
            print('Access successful.\n')

    def returnHtmlUrl(self, url, timeDelay=1, thumb=False):
        
        if(len(url)==0): raise "Could not search if you do not inform URL."

        time.sleep(timeDelay)
        req = 0
        try:
            req = Request(url) # , headers={'User-Agent': 'Mozilla/5.0'}
        except HTTPError as error:
            print("Error '%d' to download html form site",error)
            return ""

        try:
            webpage = urlopen(req, timeout=10).read()
        except HTTPError as error:
            print("Error '%d' to download html form site",error)
            return ""
        
        if (thumb): return webpage
        
        return webpage.decode("utf-8")
