# coding:utf-8
import requests
import json
from common import  Log

logger = Log.getLogger();

class HttpRequest():
    def __init__(self, url, method, req_data, check_data):
        self.url = url;
        self.method = method;
        self.req_data = req_data;
        self.check_data = check_data;
        
    def reqeust(self):
        headers = {"Content-type":"application/json;charset=utf-8",
          "Accept":"application/json"};
        try:
            if self.method.upper() == 'GET':
                response = requests.get(self.url, params=self.req_data, headers=headers);
            elif self.method.upper() == 'POST':
                response = requests.post(self.url, data=self.req_data, headers=headers);
            result = response.json();
        except:
            logger.error('请求失败')
        return result;
        
'''
import random
from common import SaveSession


url = 'http://192.168.74.128:8080/mobile/api/user/register'
headers = {"Content-type":"application/json;charset=utf-8",
          "Accept":"application/json"};
send_data = {'mobile':'1375105%d' % random.randint(0000, 9999), 'password':'123456',
           'platform':'windows',
           'username':'wujuan001',
           'sex':1,
           'age':20,
           'email':'wujuan@msn.cn',
           'code':'1234'}

# send_data = {'mobile1':'13751052657', 'password':'123456'}

print type(json.dumps(send_data))
response = requests.post(url, data=json.dumps(send_data), headers=headers);
result = response.json();

http = HttpRequest(url, "post", json.dumps(send_data), "");
result = http.reqeust()
save = SaveSession.SaveSession();
save.


print result['msg']
print result['code']
print result['data']

print result['data']['id']
print result['data']['username']
print result['data']['mobile']
print result['data']['age']
print result['data']['sex']
print result['data']['email']
print result['data']['pmoney']
print result['data']['identity']
print result['data']['money']
print result['data']['createtime']
print result['data']['lasttime']
print result['data']['token']
print result['data']['gqid']
print len(result['data'])

#############      登录          ##############
url = 'http://192.168.74.128:8080/mobile/api/user/login'
send_data = {'mobile':result['data']['mobile'], 'password':'123456'}

response = requests.post(url, data=json.dumps(send_data), headers=headers);
result = response.json();
'''

