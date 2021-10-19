# -*- codeing = utf-8 -*-
# @Time : $2021/9/23 18:29
# @Author : Astronaut
# @File : test1.py
# @software: PyCharm

import requests
import time

log_name = r'日志文件绝对地址.txt'
Riqi = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
file_name = r'自己的key的绝对地址.txt'
with open(file_name) as file_obj:
     lines = file_obj.readlines()
     key = ''
     for line in lines:
         key += line.strip()
sleeptime = 1

url = "https://jdsd.gzhu.edu.cn/coctl_gzhu/index_wx.php"

#每日签到
payload = "route=signin&key="+key+"\r\n"
length1=len(payload)
headers = {
  'Host': 'jdsd.gzhu.edu.cn',
  'Connection': 'keep-alive',
  'Content-Length': 'length1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Referer': 'https://servicewechat.com/wxb78a5743a9eed5bf/16/page-frame.html',
  'Accept-Encoding': 'gzip, deflate, br'
}

response = requests.request("POST", url, headers=headers, data=payload)
#print(response.text)
time.sleep(sleeptime)

#诗词1
payload = "route=classic_time&addtime=90&type=1&key="+key+"\r\n"
length1=len(payload)
headers = {
  'Host': 'jdsd.gzhu.edu.cn',
  'Connection': 'keep-alive',
  'Content-Length': 'length1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Referer': 'https://servicewechat.com/wxb78a5743a9eed5bf/16/page-frame.html',
  'Accept-Encoding': 'gzip, deflate, br'
}

response = requests.request("POST", url, headers=headers, data=payload)
#print(response.text)
time.sleep(sleeptime)

#诗词2
payload = "route=classic_time&addtime=90&type=2&key="+key+"\r\n"
length1=len(payload)
headers = {
  'Host': 'jdsd.gzhu.edu.cn',
  'Connection': 'keep-alive',
  'Content-Length': 'length1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Referer': 'https://servicewechat.com/wxb78a5743a9eed5bf/16/page-frame.html',
  'Accept-Encoding': 'gzip, deflate, br'
}

response = requests.request("POST", url, headers=headers, data=payload)
#print(response.text)
time.sleep(sleeptime)

#诗词3
payload = "route=classic_time&addtime=90&type=3&key="+key+"\r\n"
length1=len(payload)
headers = {
  'Host': 'jdsd.gzhu.edu.cn',
  'Connection': 'keep-alive',
  'Content-Length': 'length1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Referer': 'https://servicewechat.com/wxb78a5743a9eed5bf/16/page-frame.html',
  'Accept-Encoding': 'gzip, deflate, br'
}

response = requests.request("POST", url, headers=headers, data=payload)
#print(response.text)
time.sleep(sleeptime)

#诗词4
payload = "route=classic_time&addtime=90&type=4&key="+key+"\r\n"
length1=len(payload)
headers = {
  'Host': 'jdsd.gzhu.edu.cn',
  'Connection': 'keep-alive',
  'Content-Length': 'length1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Referer': 'https://servicewechat.com/wxb78a5743a9eed5bf/16/page-frame.html',
  'Accept-Encoding': 'gzip, deflate, br'
}

response = requests.request("POST", url, headers=headers, data=payload)
#print(response.text)
time.sleep(sleeptime)

#诗词5
payload = "route=classic_time&addtime=90&type=5&key="+key+"\r\n"
length1=len(payload)
headers = {
  'Host': 'jdsd.gzhu.edu.cn',
  'Connection': 'keep-alive',
  'Content-Length': 'length1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Referer': 'https://servicewechat.com/wxb78a5743a9eed5bf/16/page-frame.html',
  'Accept-Encoding': 'gzip, deflate, br'
}

response = requests.request("POST", url, headers=headers, data=payload)
#print(response.text)
time.sleep(sleeptime)

#每日一练
item=0
while item < 5:
    payload = "route=train_finish&train_id=2811984&train_result=%5B%5B%22y42e3U6tDL%2Fhq6URUG5Ckw%3D%3D%22%2C%220%22%5D%2C%5B%22EcmA%2Faf8%2F5%2FMMA7%2F2Q10qA%3D%3D%22%2C%221%22%5D%2C%5B%22kJY24THMX%2FcdxFUbEqAUXA%3D%3D%22%2C%220%22%5D%2C%5B%22lAe2Kglr%2BQ5gQ4MEsQwm7Q%3D%3D%22%2C%221%22%5D%2C%5B%22%2Fq7Ax8kdklm3FFFt61Q4VA%3D%3D%22%2C%221%22%5D%5D&key="+key+"\r\n"
    length1=len(payload)
    headers = {
    'Host': 'jdsd.gzhu.edu.cn',
    'Connection': 'keep-alive',
    'Content-Length': 'length1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'https://servicewechat.com/wxb78a5743a9eed5bf/16/page-frame.html',
    'Accept-Encoding': 'gzip, deflate, br'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    time.sleep(sleeptime)
    item+=1
print("您已得到21分")
with open (log_name, 'a') as file_object:
    file_object.write(Riqi+"\n")
    file_object.write(response.text+"\n")
