angka = int(input("Masukkan sebuah angka: "))
faktorial = 1
for i in range(1, angka + 1):
    faktorial *= i
print(f"Faktorial dari {angka}", f"adalah {faktorial}")
