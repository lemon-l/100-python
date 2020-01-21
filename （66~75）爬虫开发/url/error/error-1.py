import urllib.parse
import urllib.request
import urllib.error

url = 'http://chiren.com/'

try:
    response = urllib.request.urlopen(url)
    print(response)
except urllib.error.HTTPError as e:
    print(e)
    print(e.code)
except urllib.error.URLError as e:
    print(e)
