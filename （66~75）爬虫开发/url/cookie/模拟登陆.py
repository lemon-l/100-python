import urllib.request
import urllib.parse

url = 'http://www.renren.com/971759485/profile'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)\
     AppleWebKit/537.36 (KHTML, like Gecko) \
     Chrome/72.0.3626.96 Safari/537.36',
     'Cookie': 'anonymid=jt8ujei3ahq2yq; _r01_=1; \
         JSESSIONID=abcL6CRuEPLQo7X31b9Lw; depovince=GW;\
         ick_login=c4fe5b42-c84c-4f02-bd5c-a50680ba86fb;\
         ick=d787a99a-3546-467f-97c7-1cf8e9ee3ccf; \
         first_login_flag=1; ln_uact=15929878681; \
         ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif;\
         jebe_key=b6d9abe9-3bf5-4b68-954f-3ee353cd4186%7Ccb69ee40d40c246dcc7666413580b3e8%7C1564829654688%7C1%7C1564829656039;\
         jebe_key=b6d9abe9-3bf5-4b68-954f-3ee353cd4186%7Ccb69ee40d40c246dcc7666413580b3e8%7C1564829654688%7C1%7C1564829656043; \
         jebecookies=882a5b13-456d-4d9d-b2c1-58951b898911|||||; _de=D1CBFCE5C8C05DA8382A09DEF9B60216; \
         p=b511f70e9b9b7727982e3274e0eb39b95; t=587512885594bf15b0f930581c16e5c25; societyguester=587512885594bf15b0f930581c16e5c25;\
         id=971759485; xnsid=a8d99e4d; ver=7.0; loginfrom=null; wp_fold=0',
}

request = urllib.request.Request(url,headers = headers)

response = urllib.request.urlopen(request)

with open('renren.html', 'wb') as fp:
    fp.write(response.read())