"""
stride_x = satır boyunca öteleme
stride_y = sütun boyunca öteleme

out_x = sonuç olarak istediğimiz resmin x boyutu
out_y = sonuç olarak istediğimiz resmin y boyutu

row = resmin satır sayısı
col = resmin sütun sayısı
"""

"""
TO DO
- padding
"""
stride_x = 128
stride_y = 108

out_x = 128
out_y = 128

row = 2969
col = 1413

for  i in range(0, row - out_x + 1, out_x):
    for j in range(0, col - out_y + 1, stride_y):
        print(str(i) + ':' + str(i+stride_x) + ',' + str(j) + ':' + str(j+out_x))
    print('-------')


"""
num_images = [((y – b) // s_y)+1] * [((x – a) // s_x) + 1]
"""

result = ((col - out_y)// stride_y + 1) * ((row - out_x + 1) // stride_x + 1)
print('Number of Images: {}'.format(result))