# dlink-619l-buffer_overflow

![image](https://github.com/hhhhu8045759/dlink-619l-buffer_overflow/blob/master/619_2.png)

when requesting goform/Login authentication, websRedirect at the bottom of function formLogin, websRedirect passes sprintf ("<html> <head> </ head>, body. This d") of the send_r_moved_perm function to copy the Request parameter curTime  to Stack overflow in local variables
formLogin-> websRedirect-> send_r_moved_perm-> sprintf  curTime parameter causes stack overflow

An attacker can specially construct an http request containing a curTime parameter causing an overflow
