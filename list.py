# Membuat list kosong untuk menampung nilai array
stop = False
pegawai = [ ] 
# pegawai adalah variable global yang bisa diakses oleh semua fungsi
def tambah():
	
	stop = False
	i = 0

	#Mengisi Array
	while(not stop):
		pegawai_baru = raw_input("Inputkan nama pegawai yang ke-{}: ".format(i+1))
		pegawai.append(pegawai_baru)
		# methode append menambahkan list/item dari belakang 
		# Increment 1
		i += 1

		tanya = raw_input("Mau isi lagi ? (y/t): ")
		if(tanya == "t"):
			menu()
def lihat():
	# Cetak Semua Pegawai
	print "\n"
	print "=" * 100
	print "Kamu memiliki {} pegawai" .format(len(pegawai))
	for hb in pegawai:
		print "- {}" .format(hb)
	print "\n"
	pilih = raw_input("mau kembali ke menu ? (y/t): ")
	if(pilih == "y"):
		menu()
	else:
		lihat()
	#fungsi len digunakan untuk mengambil panjang list
	
def menu():
	print "*" * 100
	print "1. Tambah Data Pegawai \n"
	print "2. Lihat Data Pegawai \n"
	print "3. Hapus Data Pegawai \n"
	print "4. Exit \n"

	pilih = input("Masukkan Pilihan (1/2/3/4)  = ")
	if(pilih == 1):
		tambah()
	elif(pilih == 2) :
		lihat()
	elif(pilih == 3):
		hapus()
	elif(pilih == 4):
		stop = True
	else:
		stop = True
def hapus():
	a = 0
	print "Kamu memiliki {} pegawai" .format(len(pegawai))
	for hb in pegawai:
		print "- {}" .format(hb)
	print "\n"
	a = input("hapus data pegawai yang ke - ")
	del pegawai[a-1]
	print "Data Pegawai telah dihapus "
	menu()

menu()