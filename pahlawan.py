"""Class pahlawan: INHERITANCE dari Karakter + POLYMORPHISM pada serang()."""
import random
from karakter import Karakter


class Prajurit(Karakter):  # INHERITANCE
    def __init__(self, nama, hp=120, kekuatan=15):
        super().__init__(nama, hp, kekuatan)

    def serang(self, target):  # POLYMORPHISM: serangan biasa
        damage = self.hitung_damage(self.kekuatan)
        print(f"{self.nama} menebas {target.nama}!")
        target.terima_damage(damage)


class Penyihir(Karakter):
    def __init__(self, nama, hp=80, kekuatan=14):
        super().__init__(nama, hp, kekuatan)
        self.mana = 30

    def serang(self, target):  # POLYMORPHISM: pakai mana, damage besar
        if self.mana >= 10:
            self.mana -= 10
            damage = self.hitung_damage(self.kekuatan, pengali=1.8)
            print(f"{self.nama} melempar bola api ke {target.nama}! (mana sisa {self.mana})")
        else:
            damage = self.hitung_damage(self.kekuatan, pengali=0.5)
            print(f"{self.nama} kehabisan mana, memukul pakai tongkat.")
        target.terima_damage(damage)


class Pemanah(Karakter):
    def __init__(self, nama, hp=95, kekuatan=13):
        super().__init__(nama, hp, kekuatan)

    def serang(self, target):  # POLYMORPHISM: peluang critical hit
        if random.random() < 0.3:
            damage = self.hitung_damage(self.kekuatan, pengali=2.0)
            print(f"{self.nama} memanah titik lemah {target.nama}! CRITICAL!")
        else:
            damage = self.hitung_damage(self.kekuatan)
            print(f"{self.nama} memanah {target.nama}.")
        target.terima_damage(damage)
