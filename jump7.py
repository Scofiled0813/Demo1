#打印1~100之间的数，而且逢7的倍数和带7的数便跳过

'------------使用for循环---------------------'
for a in range(101):                                 #使用for...in+range（）函数进行循环
    if a%7==0 or a%10==7 or a//10==7:                            #if语句+判断运算符+逻辑运算符
        continue                                     #continue跳过本次循环
    print(a)                                         #打印


'------------使用while循环-------------------'
a=1
while a<100:
    a+=1
    if a%7==0 or a%10==7 or a//10==7:
        continue
    print(a)