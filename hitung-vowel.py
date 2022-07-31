from itertools import count
from time import sleep


class Chek():
    def hitungVowel(self, kalimat):
        self.kalimat = kalimat.lower()
        self.count = 0
        self.spasi = 0

        for i in self.kalimat:
            if i == " ":
                self.spasi += 1
            else:
                for z in "aiueo":
                    if i == z:
                        self.count += 1


kata = input("masukkan kata: ")
hitung = Chek()
hitung.hitungVowel(kata)
print("Jumlah vowel dalam kalimat adalah: ", hitung.count)
print("Jumlah constanta dalam kalimat adalah: ",
      len(kata)-hitung.spasi-hitung.count)
