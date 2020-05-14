import requests,urllib.parse,json,hashlib,time,platform,random
import sys
sys.path.append("Src")
from Auth import Auth
from config import config
import time
sleep = time.sleep
if platform.system() == "Windows":
    from Windows_Log import Log
else:
    from Unix_Log import Log

def data_write(tianid):
    f = open('tianxuanid.dat','w')
    f.write(tianid)
    f.close()

def data_read():
    f = open('tianxuanid.dat','r')
    tianid=f.read()
    f.close()
    return tianid

def sign():
    sleep(1)
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 9; DUK-AL20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36','Cookie':cookie}
    url = 'https://api.live.bilibili.com/xlive/lottery-interface/v1/Anchor/AwardRecord?page=1'
    request1 = requests.get(url, headers=headers)
    print(request1.text)
    r=json.loads(request1.text)
    print(r['data']['list'][0]['award_name'])
    return r


Log.info("\n======START======"+str(time.asctime())+"============\n")

a=Auth()
a.work()
csrf = config['Token']['CSRF']
Log.info(str(csrf))
cookie = config['Token']['COOKIE']
SCKEY = config['SCKEY']['SCKEY']
Log.info(str(cookie))
while 1:
    tian=sign()
    tianid1=str(tian['data']['list'][0]['id'])
    tianid2=data_read()
    if tianid1 == '':
        sleep(600)
        continue
    if tianid2 == '':
        data_write(tianid1)
        data1=time.strftime("%H:%M:%S  内容：", time.localtime())+str(tian['data']['list'][0]['award_name'])
        data2=tian['data']['list'][0]
        url='https://sc.ftqq.com/'+SCKEY+'.send?text='+data1+'&desp='+str(tian['data']['list'][0])
        request1 = requests.post(url)
        print(request1.text)
        sleep(600)
        continue
    if(tianid1==tianid2):
        sleep(600)
        continue
    data_write(tianid1)
    data1=time.strftime("%H:%M:%S  内容：", time.localtime())+str(tian['data']['list'][0]['award_name'])
    data2=tian['data']['list'][0]
    url='https://sc.ftqq.com/'+SCKEY+'.send?text='+data1+'&desp='+str(tian['data']['list'][0])
    request1 = requests.get(url)
    print(request1.text)
    sleep(600)




    
