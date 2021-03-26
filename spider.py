import urllib.request
import urllib
import urllib.parse
import re
import os

def load_page(key):

    try:
        header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"}
        #key={"word":key}
        key={"q":key}
        key_url = urllib.parse.urlencode(key)
        print('key_url=', key_url)
        
        bing_base_url = "https://cn.bing.com/images/search?"
        bing_tail_url = "&form=HDRSC2&first=1&tsc=ImageBasicHover"
        #url = base_url + key_url
        url = bing_base_url + key_url + bing_tail_url
        print('url=', url)
        
        req = urllib.request.Request(url, headers=header)
        
        res = urllib.request.urlopen(req, timeout=5)
        html = res.read().decode("utf-8")
        
        #with open("web.html", "w", encoding="utf-8") as f:
            #f.write(html)

    except Exception as e:
        print(e)

    return html


def get_img(html):
    reg = r'https?://[^\s][^https?]*?\.jpg'
    imgre = re.compile(reg)
    imglist = imgre.findall(html)
    print(len(imglist))
    
    x = 0
    img_path = os.getcwd() + '/pics'
    if not os.path.isdir(img_path):
        os.makedirs(img_path)
    paths = img_path + '/'
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl, '{0}{1}.jpg'.format(paths, x))
        x = x + 1
    return imglist

keyword = 'change keyword'
page = load_page(keyword)
print(get_img(page))
