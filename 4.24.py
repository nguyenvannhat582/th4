S = input("Nhap chuoi can kiem tra ---> ")
dict={'Chu hoa':0 ,'Chu thuong':0}
for i in S:
    if i.isupper():
        dict['Chu hoa'] += 1
    else:
        dict['Chu thuong'] +=  1
print(dict)