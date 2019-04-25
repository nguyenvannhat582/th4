#nhập một list từ bàn phím
ds=input('nhap chuoi:').split()
#cắt list:lấy list nhưng bỏ phần tử đầu và cuối
x=ds[0:-1]
for c in x:
    print(c)
#thêm phần tử vào list
    ds.append('abc')
    for ch in ds:
        print(ch)
 #bỏ phần tử khỏi list
    ds.remove('123')
    for ch in ds:
        print(ch)
#tìm kiếm phần tử trong list
print("vị trí của chuỗi abc là",ds.index('abc'))
#sắp xếp các phần tử trong list
ds.sort()
for ch in ds:
    print(ch)

