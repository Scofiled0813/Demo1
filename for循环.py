#结构for...in...
'-------------------------range（）函数----------------------------------'
for a in range(1,11):                                                #a为1~10
    print(a)                                                         #输出a

'-------------------------指定列表内元素循环----------------------------------'
namelist=\
    ['张三','李四','王五','王二麻子','杨阳','刘智兵','飞机']                #定义列表
for i in namelist:                                                    #i属于列表namelist里的元素
    print(i)                                                          #输出i

'-------------------------break关键字----------------------------------'
#break表示停止当前循环
for a in range(11):                                              #0~10的整数循环
    if a == 7:                                                   #如果a=7
        break                                                    #停止循环
    print(a)                                                     #输出a：0~6



