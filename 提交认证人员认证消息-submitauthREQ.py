#coding=utf-8
import requests
from padandunpad import padandunpad
from getEveryMsgREQ import getmsgcode
import json

class submitauthREQ():
    def submitauthREQ(self):
        aa = padandunpad()
        data = aa.padplusmsgcode()
        #msgcode=getmsgcode()
        #msgcode=msgcode.requestcode()
        # 加密消息体实例
        # 1：{ "deviceId": "AD00006", "authString": "AD000061490682606","timeStamp": "1490682606"}
        # 2：{"authString": "AD000061490682606","names":"刘晓玲","idCard":"230106199204111421","cardValidity":"20220807","results":"0","scores":"90","idenids":"211627","tabletime":"2017","nameidentify":"终提姓名","suspectscore":"67","timeStamp":"1490682606"，"picobjectid":"1"}
        paddata='{"deviceId":"AD00006","data":"' + data + '","cardPic":"","authPic":"","authsrcPic":""}'
        headers = {'content-type': 'application/json'}
        r = requests.post("http://192.168.97.115:8080/socialFaceAuthAPP/submitauthREQ.do", data=paddata, headers=headers)
       # result = json.loads(r.text)
        #return result
        #打印结果
        print u"结果：\n%s" % (r.text)

code=submitauthREQ()
code.submitauthREQ()