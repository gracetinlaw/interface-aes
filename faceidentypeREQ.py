#coding=utf-8
import requests
from padandunpad import padandunpad
import json

class faceidentypeREQ():
    def faceidentypeREQ(self):
        aa = padandunpad()
        data = aa.pad()

        headers = {'content-type': 'application/json'}
        r = requests.post("http://192.168.97.115:8080/socialFaceAuthAPP/faceidentypeREQ.do", data=data, headers=headers)
       # result = json.loads(r.text)
        #return result
        #打印结果
        print u"结果：\n%s" % (r.text)

code=faceidentypeREQ()
code.faceidentypeREQ()