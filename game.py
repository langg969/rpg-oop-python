"""Class Game: mengatur alur permainan (COMPOSITION: Game memiliki pahlawan & monster)."""
from pahlawan import Prajurit, Penyihir, Pemanah
from monster import Monster, DAFTAR_MONSTER


class Game:
    KELAS = {"1": Prajurit, "2": Penyihir, "3": Pemanah}

    def __init__(self):
        self.pahlawan = None
        self.potion = 3

    def pilih_karakter(self):
        print("=== RPG TEKS OOP ===")
        nama = input("Nama pahlawan: ").strip() or "Hero"
        print("1. Prajurit  2. Penyihir  3. Pemanah")
        pilihan = input("Pilih kelas: ").strip()
        kelas = self.KELAS.get(pilihan, Prajurit)
        self.pahlawan = kelas(nama)
        print(f"\nSelamat datang, {self.pahlawan}\n")

    def pertarungan(self, monster):
        print(f"--- {monster.nama} muncul! ---")
        while self.pahlawan.hidup and monster.hidup:
            print(f"\n{self.pahlawan} | {monster}")
            aksi = input("1. Serang  2. Potion (sisa %d): " % self.potion).strip()
            if aksi == "2" and self.potion > 0:
                self.potion -= 1
                self.pahlawan.pulihkan(40)
            else:
                self.pahlawan.serang(monster)
            if monster.hidup:
                monster.serang(self.pahlawan)
        return self.pahlawan.hidup

    def mulai(self):
        self.pilih_karakter()
        for data in DAFTAR_MONSTER:
            monster = Monster.dari_dict(data)  # CLASS METHOD dipakai di sini
            if not self.pertarungan(monster):
                print("\nKamu kalah... GAME OVER")
                break
            print(f"\n{monster.nama} dikalahkan!")
        else:
            print("\nSELAMAT! Semua monster berhasil dikalahkan!")
        from karakter import Karakter
        print(f"Total karakter yang dibuat: {Karakter.jumlah_karakter}")
