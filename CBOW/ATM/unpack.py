#def read():
dic={}
with open('db.txt',mode='rt',encoding='utf-8') as f:
    for line in f:
        user,money=line.strip().split(":")
        dic[user]=money
print(dic)