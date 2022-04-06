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

for i in range(0, row  + 1, stride_x):
    for j in range(0, col + 1, stride_y):
        if i+stride_x > row:
            
            if j+stride_y > col:
                #print('1. if i n ifi')
                plt.imsave(str(row-out_x) + '_' + str(row) + '_' + str(col-out_y) + '_' + str(col) + '.png',img[row-out_x:row, col-out_y:col,:])
                print(str(row-out_x) + ':' + str(row) + ',' + str(col-out_y) + ':' + str(col))
            else:
                #print('1. if in else i')
                plt.imsave(str(row-out_x) + '_' + str(row) + '_' + str(j) + '_' + str(j+out_y) + '.png',img[row-out_x:row, j:j+out_y,:])
                print(str(row-out_x) + ':' + str(row) + ',' + str(j) + ':' + str(j+out_x))


        elif j+stride_y > col:
            
            if i+stride_x > row:
                #print('elifin ifi')
                plt.imsave(str(row-out_x) + ':' + str(row) + ',' + str(col-out_y) + ':' + str(col) + '.png',img[row-out_x:row, col-out_y:col,:])
                print(str(row-out_x) + ':' + str(row) + ',' + str(col-out_y) + ':' + str(col))
            else:
                #print('2. ifin else i')
                plt.imsave(str(i) + '_' + str(i+out_x) + '_' + str(col-out_y) + '_' + str(col) + '.png',img[i:i+out_x, col-out_y:col,:])
                print(str(i) + ':' + str(i+stride_x) + ',' + str(col-out_y) + ':' + str(col))

        else:
            #print('else')
            plt.imsave(str(i) + '_' + str(i+out_x) + '_' + str(j) + '_' + str(j+out_y) + '.png',img[i:i+out_x, j:j+out_y,:])
            print(str(i) + ':' + str(i+stride_x) + ',' + str(j) + ':' + str(j+out_x))
        
    print('-------')
