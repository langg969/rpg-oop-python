# RPG Teks OOP (Python)

Game RPG berbasis terminal untuk tugas mata kuliah OOP.

**Nama:** (isi nama) | **NIM:** (isi NIM)

## Cara menjalankan
```bash
python main.py
```

## Penerapan konsep OOP

| Konsep | Lokasi |
|---|---|
| Class & Object | semua file |
| Atribut instance & class attribute | `karakter.py` (`jumlah_karakter`) |
| Instance method | `serang()`, `terima_damage()` |
| Class method | `Karakter.dari_dict()` |
| Static method | `Karakter.hitung_damage()` |
| Property (getter/setter) | `Karakter.hp` |
| Encapsulation | atribut `_hp`, `_hp_maks` |
| Abstract class & method | `Karakter`, `serang()` |
| Inheritance | `Prajurit`, `Penyihir`, `Pemanah`, `Monster` |
| Polymorphism | `serang()` berbeda di tiap class |
| Composition | `Game` memiliki pahlawan & monster |
| Dunder method | `__str__` |

## Struktur file
- `karakter.py` - abstract class induk
- `pahlawan.py` - Prajurit, Penyihir, Pemanah
- `monster.py` - Monster + data
- `game.py` - alur permainan
- `main.py` - titik masuk program