from urllib import urlencode
from urllib2 import urlopen,Request
import threading

def download_word(id):
    f=urlopen("http://baike.baidu.com/view/"+str(id)+".htm")
    s=f.read()
    f.close()
    f=open("F:\\baike_words\\"+str(id),"w")
    f.write(s)
    f.close()

def download(begin,end):
    for i in range(begin,end):
        download_word(i)

for i in range(10):
    th=threading.Thread(target=download,args=(i*100,(i+1)*100))
    th.start()
    
