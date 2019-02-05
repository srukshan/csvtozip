import requests

def is_downloadable(url):
    """
    Does the url contain a downloadable resource
    """
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True

def download(source, destination):
    if(not(is_downloadable(source))):
        print("Not Downloadable : "+source)
        return False
    r = requests.get(source, allow_redirects=True)
    open(destination, 'wb').write(r.content)
    return True

def getDestination(source, desPath, desFile):
    ext = ""
    if source.find('.'):
        ext = source.rsplit('.', 1)[1]
    else:
        print("no extention found for "+source+", using default jgp format")
        ext = "jpg"
    
    return (desPath+desFile+"."+ext)

class downloader:
    def __init__(self, des):
        self.des = des

    def downloadSet(self, x):
        if(str(x[1]).strip()==""):
            print("Empty Url : "+x[0])
            return
        isSuccess = download(x[1],getDestination(x[1],self.des, x[0]))
        if isSuccess:
            print("File downloaded : "+x[0])

