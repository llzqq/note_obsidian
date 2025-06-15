```bash
# 抓取访问web的通信过程
sudo tcpdump -s 2000 -i wlp0s20f3 -ntX '(src 10.194.209.211)or(dst 10.194.209.211)or(arp)'

# wegt
wget --header="Connection:close" http://www.google.com/index.html
```
- 主机109与代理服务器108建立TCP连接
- 109 发送给108 HTTP请求
- 108 通过ARP查询路由器的MAC（想要发送IP报给Web服务器）
- 108 向DNS服务器（219.239.26.42）查询百度域名对应的IP（想要发送IP报给Web服务器）
- 108与Web服务器建立TCP连接
- 108发送HTTP请求
- ...
![[图片：4实例输出.png]]

```bash
# 请求行
GET http://www.baidu.com/index.html HTTP/1.0
# 头部
User-Agent:Wget/1.12(linux-gnu)
Host:www.baidu.com
Connection:close
```

我的电脑上的输出，主机直接与Web服务器建立TCP连接
`两个hex码对应一个字节，字节可以转换为ASCII字符`
- 建立TCP连接
- HTTP请求
- HTTP应答

```bash
1 IP 10.194.209.211.48238 > 182.61.200.110.80: Flags [S], seq 3429355683, win 64240, options [mss 1460,sackOK,TS val 2711153414 ecr 0,nop,wscale 7], length 0
	0x0000:  4500 003c 0d77 4000 4006 d203 0ac2 d1d3  E..<.w@.@.......
	0x0010:  b63d c86e bc6e 0050 cc67 d0a3 0000 0000  .=.n.n.P.g......
	0x0020:  a002 faf0 5b70 0000 0204 05b4 0402 080a  ....[p..........
	0x0030:  a198 eb06 0000 0000 0103 0307            ............
2 IP 182.61.200.110.80 > 10.194.209.211.48238: Flags [S.], seq 4164850111, ack 3429355684, win 8192, options [mss 1412,sackOK,nop,nop,nop,nop,nop,nop,nop,nop,nop,nop,nop,wscale 5], length 0
	0x0000:  4500 003c 0d77 4000 3406 de03 b63d c86e  E..<.w@.4....=.n
	0x0010:  0ac2 d1d3 0050 bc6e f83e 91bf cc67 d0a4  .....P.n.>...g..
	0x0020:  a012 2000 ec1b 0000 0204 0584 0402 0101  ................
	0x0030:  0101 0101 0101 0101 0103 0305            ............
3 IP 10.194.209.211.48238 > 182.61.200.110.80: Flags [.], ack 1, win 502, length 0
	0x0000:  4500 0028 0d78 4000 4006 d216 0ac2 d1d3  E..(.x@.@.......
	0x0010:  b63d c86e bc6e 0050 cc67 d0a4 f83e 91c0  .=.n.n.P.g...>..
	0x0020:  5010 01f6 5b5c 0000                      P...[\..
4 IP 10.194.209.211.48238 > 182.61.200.110.80: Flags [P.], seq 1:146, ack 1, win 502, length 145: HTTP: GET /index.html HTTP/1.1
	0x0000:  4500 00b9 0d79 4000 4006 d184 0ac2 d1d3  E....y@.@.......
	0x0010:  b63d c86e bc6e 0050 cc67 d0a4 f83e 91c0  .=.n.n.P.g...>..
	0x0020:  5018 01f6 5bed 0000 4745 5420 2f69 6e64  P...[...GET./ind
	0x0030:  6578 2e68 746d 6c20 4854 5450 2f31 2e31  ex.html.HTTP/1.1
	0x0040:  0d0a 486f 7374 3a20 7777 772e 6261 6964  ..Host:.www.baid
	0x0050:  752e 636f 6d0d 0a55 7365 722d 4167 656e  u.com..User-Agen
	0x0060:  743a 2057 6765 742f 312e 3230 2e33 2028  t:.Wget/1.20.3.(
	0x0070:  6c69 6e75 782d 676e 7529 0d0a 436f 6e6e  linux-gnu)..Conn
	0x0080:  6563 7469 6f6e 3a20 636c 6f73 650d 0a41  ection:.close..A
	0x0090:  6363 6570 743a 202a 2f2a 0d0a 4163 6365  ccept:.*/*..Acce
	0x00a0:  7074 2d45 6e63 6f64 696e 673a 2069 6465  pt-Encoding:.ide
	0x00b0:  6e74 6974 790d 0a0d 0a                   ntity....
5 IP 182.61.200.110.80 > 10.194.209.211.48238: Flags [.], ack 146, win 2500, length 0
	0x0000:  4500 0028 ed47 4000 2f06 0347 b63d c86e  E..(.G@./..G.=.n
	0x0010:  0ac2 d1d3 0050 bc6e f83e 91c0 cc67 d135  .....P.n.>...g.5
	0x0020:  5010 09c4 6673 0000                      P...fs..
6 IP 182.61.200.110.80 > 10.194.209.211.48238: Flags [P.], seq 2060:2184, ack 146, win 2500, length 124: HTTP
	0x0000:  4500 00a4 ed4a 4000 2f06 02c8 b63d c86e  E....J@./....=.n
	0x0010:  0ac2 d1d3 0050 bc6e f83e 99cb cc67 d135  .....P.n.>...g.5
	0x0020:  5018 09c4 4b6d 0000 3ee6 9bb4 e5a4 9ae4  P...Km..>.......
	0x0030:  baa7 e593 813c 2f61 3e20 3c2f 6469 763e  .....</a>.</div>
	0x0040:  203c 2f64 6976 3e20 3c2f 6469 763e 203c  .</div>.</div>.<
	0x0050:  6469 7620 6964 3d66 7443 6f6e 3e20 3c64  div.id=ftCon>.<d
	0x0060:  6976 2069 643d 6674 436f 6e77 3e20 3c70  iv.id=ftConw>.<p
	0x0070:  2069 643d 6c68 3e20 3c61 2068 7265 663d  .id=lh>.<a.href=
	0x0080:  6874 7470 3a2f 2f68 6f6d 652e 6261 6964  http://home.baid
	0x0090:  752e 636f 6d3e e585 b3e4 ba8e e799 bee5  u.com>..........
	0x00a0:  baa6 3c2f                                ..</
7 IP 10.194.209.211.48238 > 182.61.200.110.80: Flags [.], ack 1, win 502, options [nop,nop,sack 1 {2060:2184}], length 0
	0x0000:  4500 0034 0d7a 4000 4006 d208 0ac2 d1d3  E..4.z@.@.......
	0x0010:  b63d c86e bc6e 0050 cc67 d135 f83e 91c0  .=.n.n.P.g.5.>..
	0x0020:  8010 01f6 5b68 0000 0101 050a f83e 99cb  ....[h.......>..
	0x0030:  f83e 9a47                                .>.G
8 IP 182.61.200.110.80 > 10.194.209.211.48238: Flags [P.], seq 1:648, ack 146, win 2500, length 647: HTTP: HTTP/1.1 200 OK
	0x0000:  4500 02af ed48 4000 2f06 00bf b63d c86e  E....H@./....=.n
	0x0010:  0ac2 d1d3 0050 bc6e f83e 91c0 cc67 d135  .....P.n.>...g.5
	0x0020:  5018 09c4 60e5 0000 4854 5450 2f31 2e31  P...`...HTTP/1.1
	0x0030:  2032 3030 204f 4b0d 0a43 6f6e 7465 6e74  .200.OK..Content
	0x0040:  2d4c 656e 6774 683a 2032 3338 310d 0a43  -Length:.2381..C
	0x0050:  6f6e 7465 6e74 2d54 7970 653a 2074 6578  ontent-Type:.tex
	0x0060:  742f 6874 6d6c 0d0a 5365 7276 6572 3a20  t/html..Server:.
	0x0070:  6266 650d 0a44 6174 653a 2053 756e 2c20  bfe..Date:.Sun,.
	0x0080:  3138 204d 6179 2032 3032 3520 3035 3a33  18.May.2025.05:3
	0x0090:  313a 3234 2047 4d54 0d0a 436f 6e6e 6563  1:24.GMT..Connec
	0x00a0:  7469 6f6e 3a20 636c 6f73 650d 0a0d 0a3c  tion:.close....<
	0x00b0:  2144 4f43 5459 5045 2068 746d 6c3e 0d0a  !DOCTYPE.html>..
	0x00c0:  3c21 2d2d 5354 4154 5553 204f 4b2d 2d3e  <!--STATUS.OK-->
	0x00d0:  3c68 746d 6c3e 203c 6865 6164 3e3c 6d65  <html>.<head><me
	0x00e0:  7461 2068 7474 702d 6571 7569 763d 636f  ta.http-equiv=co
	0x00f0:  6e74 656e 742d 7479 7065 2063 6f6e 7465  ntent-type.conte
	0x0100:  6e74 3d74 6578 742f 6874 6d6c 3b63 6861  nt=text/html;cha
	0x0110:  7273 6574 3d75 7466 2d38 3e3c 6d65 7461  rset=utf-8><meta
	0x0120:  2068 7474 702d 6571 7569 763d 582d 5541  .http-equiv=X-UA
	0x0130:  2d43 6f6d 7061 7469 626c 6520 636f 6e74  -Compatible.cont
	0x0140:  656e 743d 4945 3d45 6467 653e 3c6d 6574  ent=IE=Edge><met
	0x0150:  6120 636f 6e74 656e 743d 616c 7761 7973  a.content=always
	0x0160:  206e 616d 653d 7265 6665 7272 6572 3e3c  .name=referrer><
	0x0170:  6c69 6e6b 2072 656c 3d73 7479 6c65 7368  link.rel=stylesh
	0x0180:  6565 7420 7479 7065 3d74 6578 742f 6373  eet.type=text/cs
	0x0190:  7320 6872 6566 3d68 7474 703a 2f2f 7331  s.href=http://s1
	0x01a0:  2e62 6473 7461 7469 632e 636f 6d2f 722f  .bdstatic.com/r/
	0x01b0:  7777 772f 6361 6368 652f 6264 6f72 7a2f  www/cache/bdorz/
	0x01c0:  6261 6964 752e 6d69 6e2e 6373 733e 3c74  baidu.min.css><t
	0x01d0:  6974 6c65 3ee7 99be e5ba a6e4 b880 e4b8  itle>...........
	0x01e0:  8bef bc8c e4bd a0e5 b0b1 e79f a5e9 8193  ................
	0x01f0:  3c2f 7469 746c 653e 3c2f 6865 6164 3e20  </title></head>.
	0x0200:  3c62 6f64 7920 6c69 6e6b 3d23 3030 3030  <body.link=#0000
	0x0210:  6363 3e20 3c64 6976 2069 643d 7772 6170  cc>.<div.id=wrap
	0x0220:  7065 723e 203c 6469 7620 6964 3d68 6561  per>.<div.id=hea
	0x0230:  643e 203c 6469 7620 636c 6173 733d 6865  d>.<div.class=he
	0x0240:  6164 5f77 7261 7070 6572 3e20 3c64 6976  ad_wrapper>.<div
	0x0250:  2063 6c61 7373 3d73 5f66 6f72 6d3e 203c  .class=s_form>.<
	0x0260:  6469 7620 636c 6173 733d 735f 666f 726d  div.class=s_form
	0x0270:  5f77 7261 7070 6572 3e20 3c64 6976 2069  _wrapper>.<div.i
	0x0280:  643d 6c67 3e20 3c69 6d67 2068 6964 6566  d=lg>.<img.hidef
	0x0290:  6f63 7573 3d74 7275 6520 7372 633d 2f2f  ocus=true.src=//
	0x02a0:  7777 772e 6261 6964 752e 636f 6d2f 69    www.baidu.com/i
9 IP 10.194.209.211.48238 > 182.61.200.110.80: Flags [.], ack 648, win 497, options [nop,nop,sack 1 {2060:2184}], length 0
	0x0000:  4500 0034 0d7b 4000 4006 d207 0ac2 d1d3  E..4.{@.@.......
	0x0010:  b63d c86e bc6e 0050 cc67 d135 f83e 9447  .=.n.n.P.g.5.>.G
	0x0020:  8010 01f1 5b68 0000 0101 050a f83e 99cb  ....[h.......>..
	0x0030:  f83e 9a47                                .>.G
10 IP 182.61.200.110.80 > 10.194.209.211.48238: Flags [P.], seq 2184:2517, ack 146, win 2500, length 333: HTTP
	0x0000:  4500 0175 ed4b 4000 2f06 01f6 b63d c86e  E..u.K@./....=.n
	0x0010:  0ac2 d1d3 0050 bc6e f83e 9a47 cc67 d135  .....P.n.>.G.g.5
	0x0020:  5018 09c4 6a1d 0000 613e 203c 6120 6872  P...j...a>.<a.hr
	0x0030:  6566 3d68 7474 703a 2f2f 6972 2e62 6169  ef=http://ir.bai
	0x0040:  6475 2e63 6f6d 3e41 626f 7574 2042 6169  du.com>About.Bai
	0x0050:  6475 3c2f 613e 203c 2f70 3e20 3c70 2069  du</a>.</p>.<p.i
	0x0060:  643d 6370 3e26 636f 7079 3b32 3031 3726  d=cp>&copy;2017&
	0x0070:  6e62 7370 3b42 6169 6475 266e 6273 703b  nbsp;Baidu&nbsp;
	0x0080:  3c61 2068 7265 663d 6874 7470 3a2f 2f77  <a.href=http://w
	0x0090:  7777 2e62 6169 6475 2e63 6f6d 2f64 7574  ww.baidu.com/dut
	0x00a0:  792f 3ee4 bdbf e794 a8e7 99be e5ba a6e5  y/>.............
	0x00b0:  898d e5bf 85e8 afbb 3c2f 613e 266e 6273  ........</a>&nbs
	0x00c0:  703b 203c 6120 6872 6566 3d68 7474 703a  p;.<a.href=http:
	0x00d0:  2f2f 6a69 616e 7969 2e62 6169 6475 2e63  //jianyi.baidu.c
	0x00e0:  6f6d 2f20 636c 6173 733d 6370 2d66 6565  om/.class=cp-fee
	0x00f0:  6462 6163 6b3e e684 8fe8 a781 e58f 8de9  dback>..........
	0x0100:  a688 3c2f 613e 266e 6273 703b e4ba ac49  ..</a>&nbsp;...I
	0x0110:  4350 e8af 8130 3330 3137 33e5 8fb7 266e  CP...030173...&n
	0x0120:  6273 703b 203c 696d 6720 7372 633d 2f2f  bsp;.<img.src=//
	0x0130:  7777 772e 6261 6964 752e 636f 6d2f 696d  www.baidu.com/im
	0x0140:  672f 6773 2e67 6966 3e20 3c2f 703e 203c  g/gs.gif>.</p>.<
	0x0150:  2f64 6976 3e20 3c2f 6469 763e 203c 2f64  /div>.</div>.</d
	0x0160:  6976 3e20 3c2f 626f 6479 3e20 3c2f 6874  iv>.</body>.</ht
	0x0170:  6d6c 3e0d 0a                             ml>..
11 IP 10.194.209.211.48238 > 182.61.200.110.80: Flags [.], ack 648, win 497, options [nop,nop,sack 1 {2060:2517}], length 0
	0x0000:  4500 0034 0d7c 4000 4006 d206 0ac2 d1d3  E..4.|@.@.......
	0x0010:  b63d c86e bc6e 0050 cc67 d135 f83e 9447  .=.n.n.P.g.5.>.G
	0x0020:  8010 01f1 5b68 0000 0101 050a f83e 99cb  ....[h.......>..
	0x0030:  f83e 9b94                                .>..
12 IP 182.61.200.110.80 > 10.194.209.211.48238: Flags [.], seq 648:2060, ack 146, win 2500, length 1412: HTTP
	0x0000:  4500 05ac ed49 4000 2f06 fdc0 b63d c86e  E....I@./....=.n
	0x0010:  0ac2 d1d3 0050 bc6e f83e 9447 cc67 d135  .....P.n.>.G.g.5
	0x0020:  5010 09c4 056e 0000 6d67 2f62 645f 6c6f  P....n..mg/bd_lo
	0x0030:  676f 312e 706e 6720 7769 6474 683d 3237  go1.png.width=27
	0x0040:  3020 6865 6967 6874 3d31 3239 3e20 3c2f  0.height=129>.</
	0x0050:  6469 763e 203c 666f 726d 2069 643d 666f  div>.<form.id=fo
	0x0060:  726d 206e 616d 653d 6620 6163 7469 6f6e  rm.name=f.action
	0x0070:  3d2f 2f77 7777 2e62 6169 6475 2e63 6f6d  =//www.baidu.com
	0x0080:  2f73 2063 6c61 7373 3d66 6d3e 203c 696e  /s.class=fm>.<in
	0x0090:  7075 7420 7479 7065 3d68 6964 6465 6e20  put.type=hidden.
	0x00a0:  6e61 6d65 3d62 646f 727a 5f63 6f6d 6520  name=bdorz_come.
	0x00b0:  7661 6c75 653d 313e 203c 696e 7075 7420  value=1>.<input.
	0x00c0:  7479 7065 3d68 6964 6465 6e20 6e61 6d65  type=hidden.name
	0x00d0:  3d69 6520 7661 6c75 653d 7574 662d 383e  =ie.value=utf-8>
	0x00e0:  203c 696e 7075 7420 7479 7065 3d68 6964  .<input.type=hid
	0x00f0:  6465 6e20 6e61 6d65 3d66 2076 616c 7565  den.name=f.value
	0x0100:  3d38 3e20 3c69 6e70 7574 2074 7970 653d  =8>.<input.type=
	0x0110:  6869 6464 656e 206e 616d 653d 7273 765f  hidden.name=rsv_
	0x0120:  6270 2076 616c 7565 3d31 3e20 3c69 6e70  bp.value=1>.<inp
	0x0130:  7574 2074 7970 653d 6869 6464 656e 206e  ut.type=hidden.n
	0x0140:  616d 653d 7273 765f 6964 7820 7661 6c75  ame=rsv_idx.valu
	0x0150:  653d 313e 203c 696e 7075 7420 7479 7065  e=1>.<input.type
	0x0160:  3d68 6964 6465 6e20 6e61 6d65 3d74 6e20  =hidden.name=tn.
	0x0170:  7661 6c75 653d 6261 6964 753e 3c73 7061  value=baidu><spa
	0x0180:  6e20 636c 6173 733d 2262 6720 735f 6970  n.class="bg.s_ip
	0x0190:  745f 7772 223e 3c69 6e70 7574 2069 643d  t_wr"><input.id=
	0x01a0:  6b77 206e 616d 653d 7764 2063 6c61 7373  kw.name=wd.class
	0x01b0:  3d73 5f69 7074 2076 616c 7565 206d 6178  =s_ipt.value.max
	0x01c0:  6c65 6e67 7468 3d32 3535 2061 7574 6f63  length=255.autoc
	0x01d0:  6f6d 706c 6574 653d 6f66 6620 6175 746f  omplete=off.auto
	0x01e0:  666f 6375 733e 3c2f 7370 616e 3e3c 7370  focus></span><sp
	0x01f0:  616e 2063 6c61 7373 3d22 6267 2073 5f62  an.class="bg.s_b
	0x0200:  746e 5f77 7222 3e3c 696e 7075 7420 7479  tn_wr"><input.ty
	0x0210:  7065 3d73 7562 6d69 7420 6964 3d73 7520  pe=submit.id=su.
	0x0220:  7661 6c75 653d e799 bee5 baa6 e4b8 80e4  value=..........
	0x0230:  b88b 2063 6c61 7373 3d22 6267 2073 5f62  ...class="bg.s_b
	0x0240:  746e 223e 3c2f 7370 616e 3e20 3c2f 666f  tn"></span>.</fo
	0x0250:  726d 3e20 3c2f 6469 763e 203c 2f64 6976  rm>.</div>.</div
	0x0260:  3e20 3c64 6976 2069 643d 7531 3e20 3c61  >.<div.id=u1>.<a
	0x0270:  2068 7265 663d 6874 7470 3a2f 2f6e 6577  .href=http://new
	0x0280:  732e 6261 6964 752e 636f 6d20 6e61 6d65  s.baidu.com.name
	0x0290:  3d74 6a5f 7472 6e65 7773 2063 6c61 7373  =tj_trnews.class
	0x02a0:  3d6d 6e61 763e e696 b0e9 97bb 3c2f 613e  =mnav>......</a>
	0x02b0:  203c 6120 6872 6566 3d68 7474 703a 2f2f  .<a.href=http://
	0x02c0:  7777 772e 6861 6f31 3233 2e63 6f6d 206e  www.hao123.com.n
	0x02d0:  616d 653d 746a 5f74 7268 616f 3132 3320  ame=tj_trhao123.
	0x02e0:  636c 6173 733d 6d6e 6176 3e68 616f 3132  class=mnav>hao12
	0x02f0:  333c 2f61 3e20 3c61 2068 7265 663d 6874  3</a>.<a.href=ht
	0x0300:  7470 3a2f 2f6d 6170 2e62 6169 6475 2e63  tp://map.baidu.c
	0x0310:  6f6d 206e 616d 653d 746a 5f74 726d 6170  om.name=tj_trmap
	0x0320:  2063 6c61 7373 3d6d 6e61 763e e59c b0e5  .class=mnav>....
	0x0330:  9bbe 3c2f 613e 203c 6120 6872 6566 3d68  ..</a>.<a.href=h
	0x0340:  7474 703a 2f2f 762e 6261 6964 752e 636f  ttp://v.baidu.co
	0x0350:  6d20 6e61 6d65 3d74 6a5f 7472 7669 6465  m.name=tj_trvide
	0x0360:  6f20 636c 6173 733d 6d6e 6176 3ee8 a786  o.class=mnav>...
	0x0370:  e9a2 913c 2f61 3e20 3c61 2068 7265 663d  ...</a>.<a.href=
	0x0380:  6874 7470 3a2f 2f74 6965 6261 2e62 6169  http://tieba.bai
	0x0390:  6475 2e63 6f6d 206e 616d 653d 746a 5f74  du.com.name=tj_t
	0x03a0:  7274 6965 6261 2063 6c61 7373 3d6d 6e61  rtieba.class=mna
	0x03b0:  763e e8b4 b4e5 90a7 3c2f 613e 203c 6e6f  v>......</a>.<no
	0x03c0:  7363 7269 7074 3e20 3c61 2068 7265 663d  script>.<a.href=
	0x03d0:  6874 7470 3a2f 2f77 7777 2e62 6169 6475  http://www.baidu
	0x03e0:  2e63 6f6d 2f62 646f 727a 2f6c 6f67 696e  .com/bdorz/login
	0x03f0:  2e67 6966 3f6c 6f67 696e 2661 6d70 3b74  .gif?login&amp;t
	0x0400:  706c 3d6d 6e26 616d 703b 753d 6874 7470  pl=mn&amp;u=http
	0x0410:  2533 4125 3246 2532 4677 7777 2e62 6169  %3A%2F%2Fwww.bai
	0x0420:  6475 2e63 6f6d 2532 6625 3366 6264 6f72  du.com%2f%3fbdor
	0x0430:  7a5f 636f 6d65 2533 6431 206e 616d 653d  z_come%3d1.name=
	0x0440:  746a 5f6c 6f67 696e 2063 6c61 7373 3d6c  tj_login.class=l
	0x0450:  623e e799 bbe5 bd95 3c2f 613e 203c 2f6e  b>......</a>.</n
	0x0460:  6f73 6372 6970 743e 203c 7363 7269 7074  oscript>.<script
	0x0470:  3e64 6f63 756d 656e 742e 7772 6974 6528  >document.write(
	0x0480:  273c 6120 6872 6566 3d22 6874 7470 3a2f  '<a.href="http:/
	0x0490:  2f77 7777 2e62 6169 6475 2e63 6f6d 2f62  /www.baidu.com/b
	0x04a0:  646f 727a 2f6c 6f67 696e 2e67 6966 3f6c  dorz/login.gif?l
	0x04b0:  6f67 696e 2674 706c 3d6d 6e26 753d 272b  ogin&tpl=mn&u='+
	0x04c0:  2065 6e63 6f64 6555 5249 436f 6d70 6f6e  .encodeURICompon
	0x04d0:  656e 7428 7769 6e64 6f77 2e6c 6f63 6174  ent(window.locat
	0x04e0:  696f 6e2e 6872 6566 2b20 2877 696e 646f  ion.href+.(windo
	0x04f0:  772e 6c6f 6361 7469 6f6e 2e73 6561 7263  w.location.searc
	0x0500:  6820 3d3d 3d20 2222 203f 2022 3f22 203a  h.===."".?."?".:
	0x0510:  2022 2622 292b 2022 6264 6f72 7a5f 636f  ."&")+."bdorz_co
	0x0520:  6d65 3d31 2229 2b20 2722 206e 616d 653d  me=1")+.'".name=
	0x0530:  2274 6a5f 6c6f 6769 6e22 2063 6c61 7373  "tj_login".class
	0x0540:  3d22 6c62 223e e799 bbe5 bd95 3c2f 613e  ="lb">......</a>
	0x0550:  2729 3b3c 2f73 6372 6970 743e 203c 6120  ');</script>.<a.
	0x0560:  6872 6566 3d2f 2f77 7777 2e62 6169 6475  href=//www.baidu
	0x0570:  2e63 6f6d 2f6d 6f72 652f 206e 616d 653d  .com/more/.name=
	0x0580:  746a 5f62 7269 6963 6f6e 2063 6c61 7373  tj_briicon.class
	0x0590:  3d62 7269 2073 7479 6c65 3d22 6469 7370  =bri.style="disp
	0x05a0:  6c61 793a 2062 6c6f 636b 3b22            lay:.block;"
13 IP 10.194.209.211.48238 > 182.61.200.110.80: Flags [.], ack 2517, win 483, length 0
	0x0000:  4500 0028 0d7d 4000 4006 d211 0ac2 d1d3  E..(.}@.@.......
	0x0010:  b63d c86e bc6e 0050 cc67 d135 f83e 9b94  .=.n.n.P.g.5.>..
	0x0020:  5010 01e3 5b5c 0000                      P...[\..
14 IP 182.61.200.110.80 > 10.194.209.211.48238: Flags [F.], seq 2517, ack 146, win 2500, length 0
	0x0000:  4500 0028 ed4c 4000 2f06 0342 b63d c86e  E..(.L@./..B.=.n
	0x0010:  0ac2 d1d3 0050 bc6e f83e 9b94 cc67 d135  .....P.n.>...g.5
	0x0020:  5011 09c4 5c9e 0000 0000 0000 0000       P...\.........
15 IP 10.194.209.211.48238 > 182.61.200.110.80: Flags [F.], seq 146, ack 2518, win 501, length 0
	0x0000:  4500 0028 0d7e 4000 4006 d210 0ac2 d1d3  E..(.~@.@.......
	0x0010:  b63d c86e bc6e 0050 cc67 d135 f83e 9b95  .=.n.n.P.g.5.>..
	0x0020:  5011 01f5 5b5c 0000                      P...[\..
16 IP 182.61.200.110.80 > 10.194.209.211.48238: Flags [F.], seq 2517, ack 146, win 2500, length 0
	0x0000:  4500 0028 ed4d 4000 2f06 0341 b63d c86e  E..(.M@./..A.=.n
	0x0010:  0ac2 d1d3 0050 bc6e f83e 9b94 cc67 d135  .....P.n.>...g.5
	0x0020:  5011 09c4 5c9e 0000 0000 0000 0000       P...\.........
17 IP 10.194.209.211.48238 > 182.61.200.110.80: Flags [.], ack 2518, win 501, options [nop,nop,sack 1 {2517:2518}], length 0
	0x0000:  4500 0034 0d7f 4000 4006 d203 0ac2 d1d3  E..4..@.@.......
	0x0010:  b63d c86e bc6e 0050 cc67 d136 f83e 9b95  .=.n.n.P.g.6.>..
	0x0020:  8010 01f5 5b68 0000 0101 050a f83e 9b94  ....[h.......>..
	0x0030:  f83e 9b95                                .>..
18 IP 182.61.200.110.80 > 10.194.209.211.48238: Flags [P.], seq 1:648, ack 146, win 2500, length 647: HTTP: HTTP/1.1 200 OK
	0x0000:  4500 02af ed4e 4000 2f06 00b9 b63d c86e  E....N@./....=.n
	0x0010:  0ac2 d1d3 0050 bc6e f83e 91c0 cc67 d135  .....P.n.>...g.5
	0x0020:  5018 09c4 60e5 0000 4854 5450 2f31 2e31  P...`...HTTP/1.1
	0x0030:  2032 3030 204f 4b0d 0a43 6f6e 7465 6e74  .200.OK..Content
	0x0040:  2d4c 656e 6774 683a 2032 3338 310d 0a43  -Length:.2381..C
	0x0050:  6f6e 7465 6e74 2d54 7970 653a 2074 6578  ontent-Type:.tex
	0x0060:  742f 6874 6d6c 0d0a 5365 7276 6572 3a20  t/html..Server:.
	0x0070:  6266 650d 0a44 6174 653a 2053 756e 2c20  bfe..Date:.Sun,.
	0x0080:  3138 204d 6179 2032 3032 3520 3035 3a33  18.May.2025.05:3
	0x0090:  313a 3234 2047 4d54 0d0a 436f 6e6e 6563  1:24.GMT..Connec
	0x00a0:  7469 6f6e 3a20 636c 6f73 650d 0a0d 0a3c  tion:.close....<
	0x00b0:  2144 4f43 5459 5045 2068 746d 6c3e 0d0a  !DOCTYPE.html>..
	0x00c0:  3c21 2d2d 5354 4154 5553 204f 4b2d 2d3e  <!--STATUS.OK-->
	0x00d0:  3c68 746d 6c3e 203c 6865 6164 3e3c 6d65  <html>.<head><me
	0x00e0:  7461 2068 7474 702d 6571 7569 763d 636f  ta.http-equiv=co
	0x00f0:  6e74 656e 742d 7479 7065 2063 6f6e 7465  ntent-type.conte
	0x0100:  6e74 3d74 6578 742f 6874 6d6c 3b63 6861  nt=text/html;cha
	0x0110:  7273 6574 3d75 7466 2d38 3e3c 6d65 7461  rset=utf-8><meta
	0x0120:  2068 7474 702d 6571 7569 763d 582d 5541  .http-equiv=X-UA
	0x0130:  2d43 6f6d 7061 7469 626c 6520 636f 6e74  -Compatible.cont
	0x0140:  656e 743d 4945 3d45 6467 653e 3c6d 6574  ent=IE=Edge><met
	0x0150:  6120 636f 6e74 656e 743d 616c 7761 7973  a.content=always
	0x0160:  206e 616d 653d 7265 6665 7272 6572 3e3c  .name=referrer><
	0x0170:  6c69 6e6b 2072 656c 3d73 7479 6c65 7368  link.rel=stylesh
	0x0180:  6565 7420 7479 7065 3d74 6578 742f 6373  eet.type=text/cs
	0x0190:  7320 6872 6566 3d68 7474 703a 2f2f 7331  s.href=http://s1
	0x01a0:  2e62 6473 7461 7469 632e 636f 6d2f 722f  .bdstatic.com/r/
	0x01b0:  7777 772f 6361 6368 652f 6264 6f72 7a2f  www/cache/bdorz/
	0x01c0:  6261 6964 752e 6d69 6e2e 6373 733e 3c74  baidu.min.css><t
	0x01d0:  6974 6c65 3ee7 99be e5ba a6e4 b880 e4b8  itle>...........
	0x01e0:  8bef bc8c e4bd a0e5 b0b1 e79f a5e9 8193  ................
	0x01f0:  3c2f 7469 746c 653e 3c2f 6865 6164 3e20  </title></head>.
	0x0200:  3c62 6f64 7920 6c69 6e6b 3d23 3030 3030  <body.link=#0000
	0x0210:  6363 3e20 3c64 6976 2069 643d 7772 6170  cc>.<div.id=wrap
	0x0220:  7065 723e 203c 6469 7620 6964 3d68 6561  per>.<div.id=hea
	0x0230:  643e 203c 6469 7620 636c 6173 733d 6865  d>.<div.class=he
	0x0240:  6164 5f77 7261 7070 6572 3e20 3c64 6976  ad_wrapper>.<div
	0x0250:  2063 6c61 7373 3d73 5f66 6f72 6d3e 203c  .class=s_form>.<
	0x0260:  6469 7620 636c 6173 733d 735f 666f 726d  div.class=s_form
	0x0270:  5f77 7261 7070 6572 3e20 3c64 6976 2069  _wrapper>.<div.i
	0x0280:  643d 6c67 3e20 3c69 6d67 2068 6964 6566  d=lg>.<img.hidef
	0x0290:  6f63 7573 3d74 7275 6520 7372 633d 2f2f  ocus=true.src=//
	0x02a0:  7777 772e 6261 6964 752e 636f 6d2f 69    www.baidu.com/i
19 IP 10.194.209.211.48238 > 182.61.200.110.80: Flags [.], ack 2518, win 501, options [nop,nop,sack 1 {1:648}], length 0
	0x0000:  4500 0034 0d80 4000 4006 d202 0ac2 d1d3  E..4..@.@.......
	0x0010:  b63d c86e bc6e 0050 cc67 d136 f83e 9b95  .=.n.n.P.g.6.>..
	0x0020:  8010 01f5 5b68 0000 0101 050a f83e 91c0  ....[h.......>..
	0x0030:  f83e 9447                                .>.G
20 IP 182.61.200.110.80 > 10.194.209.211.48238: Flags [.], seq 648:2060, ack 146, win 2500, length 1412: HTTP
	0x0000:  4500 05ac ed4f 4000 2f06 fdba b63d c86e  E....O@./....=.n
	0x0010:  0ac2 d1d3 0050 bc6e f83e 9447 cc67 d135  .....P.n.>.G.g.5
	0x0020:  5010 09c4 056e 0000 6d67 2f62 645f 6c6f  P....n..mg/bd_lo
	0x0030:  676f 312e 706e 6720 7769 6474 683d 3237  go1.png.width=27
	0x0040:  3020 6865 6967 6874 3d31 3239 3e20 3c2f  0.height=129>.</
	0x0050:  6469 763e 203c 666f 726d 2069 643d 666f  div>.<form.id=fo
	0x0060:  726d 206e 616d 653d 6620 6163 7469 6f6e  rm.name=f.action
	0x0070:  3d2f 2f77 7777 2e62 6169 6475 2e63 6f6d  =//www.baidu.com
	0x0080:  2f73 2063 6c61 7373 3d66 6d3e 203c 696e  /s.class=fm>.<in
	0x0090:  7075 7420 7479 7065 3d68 6964 6465 6e20  put.type=hidden.
	0x00a0:  6e61 6d65 3d62 646f 727a 5f63 6f6d 6520  name=bdorz_come.
	0x00b0:  7661 6c75 653d 313e 203c 696e 7075 7420  value=1>.<input.
	0x00c0:  7479 7065 3d68 6964 6465 6e20 6e61 6d65  type=hidden.name
	0x00d0:  3d69 6520 7661 6c75 653d 7574 662d 383e  =ie.value=utf-8>
	0x00e0:  203c 696e 7075 7420 7479 7065 3d68 6964  .<input.type=hid
	0x00f0:  6465 6e20 6e61 6d65 3d66 2076 616c 7565  den.name=f.value
	0x0100:  3d38 3e20 3c69 6e70 7574 2074 7970 653d  =8>.<input.type=
	0x0110:  6869 6464 656e 206e 616d 653d 7273 765f  hidden.name=rsv_
	0x0120:  6270 2076 616c 7565 3d31 3e20 3c69 6e70  bp.value=1>.<inp
	0x0130:  7574 2074 7970 653d 6869 6464 656e 206e  ut.type=hidden.n
	0x0140:  616d 653d 7273 765f 6964 7820 7661 6c75  ame=rsv_idx.valu
	0x0150:  653d 313e 203c 696e 7075 7420 7479 7065  e=1>.<input.type
	0x0160:  3d68 6964 6465 6e20 6e61 6d65 3d74 6e20  =hidden.name=tn.
	0x0170:  7661 6c75 653d 6261 6964 753e 3c73 7061  value=baidu><spa
	0x0180:  6e20 636c 6173 733d 2262 6720 735f 6970  n.class="bg.s_ip
	0x0190:  745f 7772 223e 3c69 6e70 7574 2069 643d  t_wr"><input.id=
	0x01a0:  6b77 206e 616d 653d 7764 2063 6c61 7373  kw.name=wd.class
	0x01b0:  3d73 5f69 7074 2076 616c 7565 206d 6178  =s_ipt.value.max
	0x01c0:  6c65 6e67 7468 3d32 3535 2061 7574 6f63  length=255.autoc
	0x01d0:  6f6d 706c 6574 653d 6f66 6620 6175 746f  omplete=off.auto
	0x01e0:  666f 6375 733e 3c2f 7370 616e 3e3c 7370  focus></span><sp
	0x01f0:  616e 2063 6c61 7373 3d22 6267 2073 5f62  an.class="bg.s_b
	0x0200:  746e 5f77 7222 3e3c 696e 7075 7420 7479  tn_wr"><input.ty
	0x0210:  7065 3d73 7562 6d69 7420 6964 3d73 7520  pe=submit.id=su.
	0x0220:  7661 6c75 653d e799 bee5 baa6 e4b8 80e4  value=..........
	0x0230:  b88b 2063 6c61 7373 3d22 6267 2073 5f62  ...class="bg.s_b
	0x0240:  746e 223e 3c2f 7370 616e 3e20 3c2f 666f  tn"></span>.</fo
	0x0250:  726d 3e20 3c2f 6469 763e 203c 2f64 6976  rm>.</div>.</div
	0x0260:  3e20 3c64 6976 2069 643d 7531 3e20 3c61  >.<div.id=u1>.<a
	0x0270:  2068 7265 663d 6874 7470 3a2f 2f6e 6577  .href=http://new
	0x0280:  732e 6261 6964 752e 636f 6d20 6e61 6d65  s.baidu.com.name
	0x0290:  3d74 6a5f 7472 6e65 7773 2063 6c61 7373  =tj_trnews.class
	0x02a0:  3d6d 6e61 763e e696 b0e9 97bb 3c2f 613e  =mnav>......</a>
	0x02b0:  203c 6120 6872 6566 3d68 7474 703a 2f2f  .<a.href=http://
	0x02c0:  7777 772e 6861 6f31 3233 2e63 6f6d 206e  www.hao123.com.n
	0x02d0:  616d 653d 746a 5f74 7268 616f 3132 3320  ame=tj_trhao123.
	0x02e0:  636c 6173 733d 6d6e 6176 3e68 616f 3132  class=mnav>hao12
	0x02f0:  333c 2f61 3e20 3c61 2068 7265 663d 6874  3</a>.<a.href=ht
	0x0300:  7470 3a2f 2f6d 6170 2e62 6169 6475 2e63  tp://map.baidu.c
	0x0310:  6f6d 206e 616d 653d 746a 5f74 726d 6170  om.name=tj_trmap
	0x0320:  2063 6c61 7373 3d6d 6e61 763e e59c b0e5  .class=mnav>....
	0x0330:  9bbe 3c2f 613e 203c 6120 6872 6566 3d68  ..</a>.<a.href=h
	0x0340:  7474 703a 2f2f 762e 6261 6964 752e 636f  ttp://v.baidu.co
	0x0350:  6d20 6e61 6d65 3d74 6a5f 7472 7669 6465  m.name=tj_trvide
	0x0360:  6f20 636c 6173 733d 6d6e 6176 3ee8 a786  o.class=mnav>...
	0x0370:  e9a2 913c 2f61 3e20 3c61 2068 7265 663d  ...</a>.<a.href=
	0x0380:  6874 7470 3a2f 2f74 6965 6261 2e62 6169  http://tieba.bai
	0x0390:  6475 2e63 6f6d 206e 616d 653d 746a 5f74  du.com.name=tj_t
	0x03a0:  7274 6965 6261 2063 6c61 7373 3d6d 6e61  rtieba.class=mna
	0x03b0:  763e e8b4 b4e5 90a7 3c2f 613e 203c 6e6f  v>......</a>.<no
	0x03c0:  7363 7269 7074 3e20 3c61 2068 7265 663d  script>.<a.href=
	0x03d0:  6874 7470 3a2f 2f77 7777 2e62 6169 6475  http://www.baidu
	0x03e0:  2e63 6f6d 2f62 646f 727a 2f6c 6f67 696e  .com/bdorz/login
	0x03f0:  2e67 6966 3f6c 6f67 696e 2661 6d70 3b74  .gif?login&amp;t
	0x0400:  706c 3d6d 6e26 616d 703b 753d 6874 7470  pl=mn&amp;u=http
	0x0410:  2533 4125 3246 2532 4677 7777 2e62 6169  %3A%2F%2Fwww.bai
	0x0420:  6475 2e63 6f6d 2532 6625 3366 6264 6f72  du.com%2f%3fbdor
	0x0430:  7a5f 636f 6d65 2533 6431 206e 616d 653d  z_come%3d1.name=
	0x0440:  746a 5f6c 6f67 696e 2063 6c61 7373 3d6c  tj_login.class=l
	0x0450:  623e e799 bbe5 bd95 3c2f 613e 203c 2f6e  b>......</a>.</n
	0x0460:  6f73 6372 6970 743e 203c 7363 7269 7074  oscript>.<script
	0x0470:  3e64 6f63 756d 656e 742e 7772 6974 6528  >document.write(
	0x0480:  273c 6120 6872 6566 3d22 6874 7470 3a2f  '<a.href="http:/
	0x0490:  2f77 7777 2e62 6169 6475 2e63 6f6d 2f62  /www.baidu.com/b
	0x04a0:  646f 727a 2f6c 6f67 696e 2e67 6966 3f6c  dorz/login.gif?l
	0x04b0:  6f67 696e 2674 706c 3d6d 6e26 753d 272b  ogin&tpl=mn&u='+
	0x04c0:  2065 6e63 6f64 6555 5249 436f 6d70 6f6e  .encodeURICompon
	0x04d0:  656e 7428 7769 6e64 6f77 2e6c 6f63 6174  ent(window.locat
	0x04e0:  696f 6e2e 6872 6566 2b20 2877 696e 646f  ion.href+.(windo
	0x04f0:  772e 6c6f 6361 7469 6f6e 2e73 6561 7263  w.location.searc
	0x0500:  6820 3d3d 3d20 2222 203f 2022 3f22 203a  h.===."".?."?".:
	0x0510:  2022 2622 292b 2022 6264 6f72 7a5f 636f  ."&")+."bdorz_co
	0x0520:  6d65 3d31 2229 2b20 2722 206e 616d 653d  me=1")+.'".name=
	0x0530:  2274 6a5f 6c6f 6769 6e22 2063 6c61 7373  "tj_login".class
	0x0540:  3d22 6c62 223e e799 bbe5 bd95 3c2f 613e  ="lb">......</a>
	0x0550:  2729 3b3c 2f73 6372 6970 743e 203c 6120  ');</script>.<a.
	0x0560:  6872 6566 3d2f 2f77 7777 2e62 6169 6475  href=//www.baidu
	0x0570:  2e63 6f6d 2f6d 6f72 652f 206e 616d 653d  .com/more/.name=
	0x0580:  746a 5f62 7269 6963 6f6e 2063 6c61 7373  tj_briicon.class
	0x0590:  3d62 7269 2073 7479 6c65 3d22 6469 7370  =bri.style="disp
	0x05a0:  6c61 793a 2062 6c6f 636b 3b22            lay:.block;"
21 IP 10.194.209.211.48238 > 182.61.200.110.80: Flags [.], ack 2518, win 501, options [nop,nop,sack 1 {648:2060}], length 0
	0x0000:  4500 0034 0d81 4000 4006 d201 0ac2 d1d3  E..4..@.@.......
	0x0010:  b63d c86e bc6e 0050 cc67 d136 f83e 9b95  .=.n.n.P.g.6.>..
	0x0020:  8010 01f5 5b68 0000 0101 050a f83e 9447  ....[h.......>.G
	0x0030:  f83e 99cb                                .>..
22 IP 182.61.200.110.80 > 10.194.209.211.48238: Flags [.], ack 147, win 2500, length 0
	0x0000:  4500 0028 ed50 4000 2f06 033e b63d c86e  E..(.P@./..>.=.n
	0x0010:  0ac2 d1d3 0050 bc6e f83e 9b95 cc67 d136  .....P.n.>...g.6
	0x0020:  5010 09c4 5c9d 0000 0000 0000 0000       P...\.........

```