import urllib.request, urllib.error, urllib.parse,re,xbmc,urllib.request,urllib.parse,urllib.error,requests
def getdatacontent(url,reg):
    proxy_handler = urllib.request.ProxyHandler({})
    opener = urllib.request.build_opener(proxy_handler)
    req = urllib.request.Request(url)
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    r = opener.open(req)
    html = r.read().decode('utf-8')
    data = re.compile(reg).findall(html)
    return data

def resolve_videobin(url):  
    reg = 'sources\s*:\s*\[(.+?)\]'
    streamurl = getdatacontent(url,reg)
    streamurl = streamurl[0]
    streamurl = streamurl.split('","')
    streamurl = streamurl[1]
    return streamurl