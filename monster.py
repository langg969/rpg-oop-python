"""Class Monster: child lain dari Karakter."""
from karakter import Karakter


class Monster(Karakter):
    def __init__(self, nama, hp, kekuatan):
        super().__init__(nama, hp, kekuatan)

    def serang(self, target):
        damage = self.hitung_damage(self.kekuatan)
        print(f"{self.nama} menyerang {target.nama}!")
        target.terima_damage(damage)


# Data monster disimpan sebagai dictionary, dibuat lewat @classmethod dari_dict
DAFTAR_MONSTER = [
    {"nama": "Goblin", "hp": 50, "kekuatan": 8},
    {"nama": "Orc", "hp": 80, "kekuatan": 12},
    {"nama": "Naga", "hp": 130, "kekuatan": 18},
]
