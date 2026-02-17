class buku :
    def __init__ (self,judul,nama_penulis,penerbit,tahun_terbit):
        self.judul = judul
        self.nama_penulis = nama_penulis
        self.penerbit = penerbit
        self.tahun_terbit = tahun_terbit
        self.status_buku = False #kalau status buku muncul false, berarti tersedia
    
    def dipinjam(self):
        self.status_buku = True
        
    def dikembalikan(self):
        self.status_buku = False
    
    def daftar_buku(self):
        print(f"judul buku      : {self.judul}")
        print(f"nama pengarang  : {self.nama_penulis}")
        print(f"penerbit        : {self.penerbit}")
        print(f"tahun terbit    : {self.tahun_terbit}\n")

    
class member :
    def __init__ (self,nama,usia,no_member) :
        self.nama = nama
        self.usia = usia
        self.no_member = no_member
        self.daftar_peminjaman = []
    
    def peminjaman_buku(self,buku):
        if not buku.status_buku :
            buku.dipinjam()
            self.daftar_peminjaman.append(buku)
            print(f"{self.nama} dengan member {self.no_member} berhasil meminjam buku {buku.judul}")
            
        else :
            print(f'maaf {self.nama} dengan member {self.no_member}, buku {buku.judul} sedang dipinjam atau tidak tersedia. silahkan cari buku lain')
            
    def pengembalian_buku(self,buku):
        if buku in self.daftar_peminjaman :
            buku.dikembalikan()
            self.daftar_peminjaman.remove(buku)
            print(f"{self.nama} telah mengembalikan buku tepat waktu")
    
    def member_perpus(self):
        print(f"nama member : {self.nama}")
        print(f"usia member : {self.usia} tahun")
        print(f"nomor member: {self.no_member}\n")
    
            
buku1 = buku("Mein Kampf (Perjuangan Saya)","adolf hitler","Anak Hebat Indonesia",1925)
buku2 = buku("Cerita Dari Digul (2022)","Pramoedya Ananta Toer", "Kepustakaan Populer Gramedia",2022)

member1 = member("nara", 18, "0000001")
member2 = member("agus", 19, "0000002")
member3 = member("chelsi", 18, "0002304")

member1.peminjaman_buku(buku1)
member1.pengembalian_buku(buku1)
member2.peminjaman_buku(buku2)
member3.peminjaman_buku(buku2)

print("\n"+ 5*"-" + "daftar buku" + 5*"-")
buku1.daftar_buku()
buku2.daftar_buku()

print("\n"+ 5*"-" + "daftar member" + 5*"-")
member1.member_perpus()
member2.member_perpus()
member3.member_perpus()


