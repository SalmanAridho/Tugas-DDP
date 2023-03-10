# -*- coding: utf-8 -*-
"""Tugas_DDP_0110122114_M.SALMAN.ARIDHO_SI10.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12pMbAFDPNbhwAAaJFD-6f140mYwxWlY8
"""

class Gempa:  
    lokasi = ''
    skala = 0

  #member2 kontruktor
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

  #member3 method
    def dampak(self):
        if( self.skala < 2 ):
            ket = 'Tidak terasa'
        elif(self.skala >= 2 and self.skala < 4):
            ket = 'Bangunan retak-retak'
        elif(self.skala >= 4 and self.skala < 6):
            ket = 'Bangunan pada roboh'
        else:
            ket = 'Bangunan roboh dan Berpotensi tsunami'
        print('Telah terjadi gempa di' ,self.lokasi ,'dengan skala' ,self.skala, 'richter', 'berdampak' ,ket)  

  #buat object
g1 = Gempa('Banten',1.2)
g2 = Gempa('Palu',6.1)
g3 = Gempa('Cianjur',5.6)
g4 = Gempa('Jayapura',3.3)
g5 = Gempa('Garut',4.0)

  #panggil fungsi di class Gempa
g1.dampak()
g2.dampak()
g3.dampak()
g4.dampak()
g5.dampak()