#coding=utf-8
import requests
from padandunpad import padandunpad
import json

class getmsgcode():
    def requestcode(self):
        aa=padandunpad()
        data=aa.pad()
        # 定义头文件
        headers = {'content-type': 'application/json'}
        # 进行POST请求
        r = requests.post("http://192.168.97.115:8080/socialFaceAuthAPP/getEveryMsgREQ.do", data=data,
                          headers=headers)
        # 打印JSON串
        # print(r.text)
        # 调用JSON串中的‘msgcode’
        msgcode = json.loads(r.text).get("msgcode")
        # 解密数据
        print msgcode
        return msgcode

code=getmsgcode()
code.requestcode()
