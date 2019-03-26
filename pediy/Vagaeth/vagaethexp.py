abc = "abcdefghiABCDEFGHIJKLMNjklmn0123456789opqrstuvwxyzOPQRSTUVWXYZ"                      
kan = "KanXueCTF2019JustForhappy"                                                           
index = 0                                                                                   
num = []
for i in kan:                                                                               
    for j in abc:                                                                           
        if j==i:                                                                            
            num.append(abc.find(j))
            index += 1
print(num)

secret = []
index2 = 0
for a in num:
    if  0 <= a <= 9:
        secret.append(chr(a+48))
    elif 10 <= a <= 35:
        secret.append(chr(a+87))
    elif 36 <= a <= 61:
        secret.append(chr(a+0x1d))
print ''.join(secret)
