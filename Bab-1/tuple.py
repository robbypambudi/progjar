# Touple bersifat immutable
# Tuple adalah jenis dari data yang tidak dapat diubah elemennya

address = 'localhost', 80 , 21

# Cara akses elemen tuple
print('Alamat server: ', address[0])
print('Port HTTP: ', address[1])
print('Port FTP: ', address[2])


# Cara mengubah elemen tuple
address[0] = '192.168.1.1'
# Hasilnya akan error, karena tuple bersifat immutable

print(address)