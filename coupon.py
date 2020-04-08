# -*- coding:utf-8 -*-
from jd_test import Jd_test

if __name__ == '__main__':
    
    jdt = Jd_test()  # 初始化
    
    retcode = jdt.coupon_get()
    print(retcode)