'''
注意当：1. form_data里面的sign需要换成单词所在页面的sign，否则换成其他单词会出错（不同的单词有不同的sign）
       2. 同理token也是和是sign一样的
       3. headers里面的内容需要复制fiddler里面raw所有的内容（除了'Accept-Encoding': 'gzip, deflate, br'）这一项是压缩，会导致到时候解码出现问题）

'''
import urllib.request
import urllib.parse

post_url = 'https://fanyi.baidu.com/v2transapi'
word = input('输入你要查询的单词： ')

form_data = {
    'from': 'en',
    'to': 'zh',
    'query': word,
    'transtype': 'enter',
    'simple_means_flag': '3',
    'sign':	'221212.492333',
    'token': 'ebacf3c6f4b0ee1cba86467af7547fb1',
}

headers = {
    'Host': 'fanyi.baidu.com',
    'Connection': 'keep-alive',
    'Content-Length': '119',
    'Accept': '*/*',
    'Origin': 'https://fanyi.baidu.com',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36',
    'DNT': '1',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'https://fanyi.baidu.com/',
   # 'Accept-Encoding': 'gzip, deflate, br',              -----------这一条不需要
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cookie': 'BAIDUID=705482AB710B2E46DF7296EA0345BB8B:FG=1; BIDUPSID=705482AB710B2E46DF7296EA0345BB8B; PSTM=1558355256; BDRCVFR[1dpuk6qxdKY]=mk3SLVN4HKm; delPer=0; BDRCVFR[JZ0gYmR161D]=mbxnW11j9Dfmh7GuZR8mvqV; PSINO=5; H_PS_PSSID=; pgv_pvi=48121856; pgv_si=s9359634432; ZD_ENTRY=google; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1564635447; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1564635447; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; yjs_js_security_passport=bc7410ecc69857de9c4a22267389da4e09315a17_1564635448_js; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D',
}

request = urllib.request.Request(url = post_url, headers = headers)
form_data = urllib.parse.urlencode(form_data).encode()

response = urllib.request.urlopen(request, form_data)

print(response.read().decode())

