"""

	author	:  Dio

"""

num = int(input("Masukkan nilai: "))
if num % 2 == 0:
    print("Angka Genap")
else:
    print("Angka Ganjil")

year = int(input("Masukkan tahun: "))
if year % 100 == 0 and year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
    print("Tahun kabisat")
else:
    print("Tahun bukan kabisat")
