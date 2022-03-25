"""
Nama           : Tamara Dwi R
NIM              : 119140196
Kelas            : PBO RC
Nomor Soal : 1
"""
class TokoBuku:
 def __init__(self, nm, gr, ps, tn):
  self.nama = str(nm);
  self.genre = str(gr);
  self.penulis = str(ps);
  self.tahun = int(tn);  

 def getNama(self):
  return self.nama;

 def getGenre(self):
  return self.genre;

 def getPenulis(self):
  return self.penulis;

 def getTahun(self):
  return self.tahun;

 def setNama(self, nm):
  self.nama = nm;

 def setGenre(self, gr):
  self.genre = gr;

 def setPenulis(self, ps):
  self.penulis=ps;

 def setTahun(self, tn):
  self.tahun=tn; 

DftrTkbk = {};
loop = True;

print("===================================");
print("=         Daftar Mahasiswa        =");
print("===================================");
print("= # MENU                          =");
print("= 1. Tambah Mahasiswa             =");
print("= 2. Lihat list Buku              =");
print("= 3. Modifikasi buku              =");
print("= 4. Hapus buku lama              =");
print("= 5. Keluar Program               =");

while(loop):
 print("\n\n");
 menu = int(input("Masukan menu : "));

 if menu == 1:

  nama = str(input("Masukan nama : "));      #membuat program untuk menginput 
  genre = str(input("Masukan genre : "));
  penulis = str(input("Masukan penulis : "));
  tahun = int(input("Masukan tahun : "));
  Tkbk = TokoBuku(nama, genre, penulis, tahun);
  DftrTkbk[nama] = Tkbk;
 elif menu == 2:                            #membuat program untuk menampilkan data buku yang telah disimpan
  for i in DftrTkbk:
   print("Nama :", DftrTkbk[i].getNama());
   print("Genre :", DftrTkbk[i].getGenre());
   print("Penulis :", DftrTkbk[i].getPenulis());
   print("Tahun :", DftrTkbk[i].getTahun()); 
 elif menu == 3:                            #membuat program untuk mengedit nama buku
  nama = str(input("Masukan nama : "));
  if(nama in DftrTkbk):
   namaBaru = str(input("Masukan Nama Baru : "));
   DftrTkbk[nama].setNama(namaBaru);
  else:
   print("Data tidak ditemukan!!!");

 elif menu == 4:                            #menghapus data buku 
  nama = str(input("Masukan nama : "));
  if(nama in DftrTkbk):
   del DftrTkbk[nama];
  else:
   print("Data tidak ditemukan!!!");

 elif menu == 5:
  loop = False;
 else:

  print("XXXX");
