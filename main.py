# -*- coding:utf-8 -*-
from jd_test import Jd_test

if __name__ == '__main__':
 

    # sku_ids = '100001324422'  # 商品id
    sku_ids = '100005267656'  # 商品id
    area = '2_2815_51975'  # 区域id
    jdt = Jd_test()  # 初始化
    # jdt.login_by_QRcode()  # 扫码登陆
    # jdt.login_by_username()  #账户密码登陆
    # jdt.buy_item_in_stock(sku_ids=sku_ids, area=area, wait_all=False, stock_interval=5)  # 根据商品是否有货自动下单
    # 6个参数：
    # sku_ids: 商品id。可以设置多个商品，也可以带数量，如：'1234' 或 '1234,5678' 或 '1234:2' 或 '1234:2,5678:3'
    # area: 地区id
    # wait_all: 是否等所有商品都有货才一起下单，可选参数，默认False
    # stock_interval: 查询库存时间间隔，可选参数，默认3秒
    # submit_retry: 提交订单失败后重试次数，可选参数，默认3次
    # submit_interval: 提交订单失败后重试时间间隔，可选参数，默认5秒

    #############auction############
    address = "2-2830-51805-0"
    auctionId = 209442030
    eid = "XNCSBQMI4PUEQ65UHQLF4XKENYAO3LP46VS5Q56RONRDUH735QSMF4JA64XUTFD4JNDIVIXVR2AFLCCKLMM2VYOC3Q"
    # entryid = ""
    # initFailed = "false"
    price = 111
    token = "16qggtj54ajtww0dysv15860026907708vqd~NmZeSyVEbFNSdH97dVZdC3R2BghjRHpTBiUjb35DFm5vLUROOBEzLUF7G28iAAFBKBgVFA1EPwIVKDclGENXbm8iVlQiAwpTTx1lKSsTCG5vfmsaIx8/FV4dZWEYQwtub35rGmgEZUcFd38pIlZfC31xDwpjVTAXUSJ3eCYEVAcuIAAKOgouBz9jaxFmCB5fEWYNZHMANx0QJBtvaD1PWj4waxprOnQBAig3LC1PB1ZjJ1hVDUR6LUExKRFmWzEQYiVCWyUPOR9OJSI5JQgBHX90DgtjV2BDVh1lYRhDHUYRZg1kcw4iBRMyfRFmTTEQPS1rGms6dENRbX9hck1dHn1oAAANRCtTT2MiKSASChB3Zg5SOwx0XUEiNG9+Q1VReHNWWSEENBISO38lcgtZBigjVEg4CTQCD3IydCAYCVk1LBUUcwV0S0EoKyQ0WV0EKiwFWzcPOEBbKS50dVRVBH10BQ5oVmFHVXN3NCtDQRApN1kaa0QwRhE7IT48CU8eby1EGmtEZ1NPYy0kJ0NXEHR9Dg9zGw==|~1586171005084~1~20200318~eyJ2aXdlIjoiMCIsImJhaW4iOnsiaWMiOiIxIiwibGUiOiIxMDAiLCJjdCI6IjAiLCJkdCI6ImkifX0=~2~-317~rii4|1dn3-oj,74,5g,1e;1d4g-fr,c,9e,c;1d587-kx,4,ek,4;1d7-l4,a,er,a;1db-l8,f,ev,f;1di-lc,n,ez,n;1dg-lc,z,fe,5;1dg-l9,1a,fb,g;1dh-l3,1s,f5,y;1dg-ky,25,f0,1b;1dh-kv,2g,ex,1m;1dh-kp,2u,er,20;1dh-ki,3c,1t,0;1dh-kd,3u,1o,i;1dh-k6,4j,1h,17;1df-k2,4x,dz,b;1dh-jz,59,dw,n;1dh-jy,5e,dv,s;1dg-jy,5i,dv,w;1dh-jy,5m,dv,10;1dh-jy,5p,dv,13;1dg-jy,5y,v,8;1dh-jx,6i,u,s;1di-k0,71,x,1b;1dh-kf,7j,y,b;1dg-kx,85,1g,x;1dh-le,8l,2b,1;1dh-ls,8z,16,-5;1d11-mm,9o,20,k;1d6-mr,9q,3o,16;1d2h-no,8c,23,13;1d2s-mh,75,3e,1f;1d4h-mb,6u,38,14;1d15-m5,6b,32,l;1d2r-lb,am,28,4w;1d2u-kj,dl,1g,i;1d2q-b9,2u,5b,20;1d26r-m4,8o,31,4;1d1t-o2,a5,4z,1l;1d2r-o4,a3,51,1j;1d54-o3,ad,50,1t;1dg-nx,b0,1h,8;1d2t-nu,e3,37,z;1d2r-nu,ez,38,s;1d2s-nb,fl,48,4t;1d2t-mf,gs,32,r;1d2r-m1,gw,2o,v;1d3d-lv,gw,2i,v;1d4k-ls,gr,2f,q;bdg-ls,gr,2f,q;doei:,1,1,0,0,1,1000,-1000,1000,-1000;dmei:,1,1,1,1000,-1000,1000,-1000,1000,-1000;emc:,d:119;emmm:,d:316-0;emcf:,d:119;ivli:;iivl:;ivcvj:;scvje:;ewhi:;1586170992097,1586171005084,0,0,50,50,0,70,0,0,0;hx4t"
    trackId = "d22bceb5c925b19b55082a66a01109d0"
    # jdt.auction_bid(address,auctionId,eid,price,token,trackId)

    retcode = jdt.coupon_get()
    print(retcode)