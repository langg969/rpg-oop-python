"""Abstract class Karakter: dasar untuk semua pahlawan dan monster."""
import random
from abc import ABC, abstractmethod


class Karakter(ABC):  # ABSTRACT CLASS
    # CLASS ATTRIBUTE: dimiliki class, dibagi ke semua object
    jumlah_karakter = 0

    def __init__(self, nama, hp, kekuatan):
        self.nama = nama
        self._hp = hp            # ENCAPSULATION: atribut "private" (konvensi _)
        self._hp_maks = hp
        self.kekuatan = kekuatan
        Karakter.jumlah_karakter += 1

    # PROPERTY (getter): akses seperti atribut biasa -> karakter.hp
    @property
    def hp(self):
        return self._hp

    # PROPERTY (setter): validasi agar HP tidak negatif / melebihi maksimum
    @hp.setter
    def hp(self, nilai):
        self._hp = max(0, min(nilai, self._hp_maks))

    @property
    def hidup(self):
        return self._hp > 0

    # STATIC METHOD: tidak butuh self/cls, murni fungsi bantu
    @staticmethod
    def hitung_damage(kekuatan, pengali=1.0):
        return int(kekuatan * pengali * random.uniform(0.8, 1.2))

    # CLASS METHOD: membuat object dari dictionary (alternative constructor)
    @classmethod
    def dari_dict(cls, data):
        return cls(**data)

    # ABSTRACT METHOD: wajib di-override oleh child class
    @abstractmethod
    def serang(self, target):
        pass

    def terima_damage(self, damage):
        self.hp -= damage  # memanggil setter property
        print(f"   {self.nama} menerima {damage} damage (HP: {self.hp}/{self._hp_maks})")

    def pulihkan(self, jumlah):
        self.hp += jumlah
        print(f"   {self.nama} pulih {jumlah} HP (HP: {self.hp}/{self._hp_maks})")

    # DUNDER METHOD: tampilan object saat di-print
    def __str__(self):
        return f"{self.nama} [{type(self).__name__}] HP {self.hp}/{self._hp_maks}"
