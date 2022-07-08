from cgi import test


class fuzzy():
    kecepatanLambat = 0.0
    kecepatanCepat = 0.0
    suhuRendah = 0.0
    suhuTinggi = 0.0
    a_predikat_1 = a_predikat_2 = a_predikat_3 = a_predikat_4 = 0.0
    z1 = z2 = z3 =z4  = 0.0

    zTotal =  z = a_pred_z = 0.0

    def fuzzyKecepatan(self, kecepatan) :
        if kecepatan <= 1000:
            self.kecepatanLambat = 1
            self.kecepatanCepat = 0
        elif kecepatan >= 1000 and kecepatan <= 5000:
            self.kecepatanLambat = (5000- kecepatan) / (5000-1000)
            self.kecepatanCepat = (kecepatan - 1000) / (5000-1000)
        else :
            self.kecepatanCepat = 1
            self.kecepatanLambat = 0

        print('Derajat keanggotaan kecepatan cepat = ',self.kecepatanCepat )
        print('Derajat keanggotaan kecepatan lambat = ',self.kecepatanLambat )

    def fuzzifikasiSuhu(self, suhu):
        if suhu <= 100 :
            self.suhuRendah = 1
            self.suhuTinggi = 0
        elif suhu >= 100 and suhu <= 600 :
            self.suhuRendah = (600-suhu) / (600-100)
            self.suhuTinggi = (suhu - 100) / (600-100)
        else :
            self.suhuRendah = 0
            self.suhuTinggi = 1
            
        print('Derajat keanggotaan suhu rendah = ',self.suhuRendah )
        print('Derajat keanggotaan suhu tinggi = ',self.suhuTinggi )

    def mesinInferensiTsukamoto(self):
        self.a_predikat_1 = min(self.kecepatanLambat, self.suhuTinggi)
        self.z1 = 7000 - self.a_predikat_1 * (7000-2000)
        print("A predikat 1 : ", self.a_predikat_1, " | ", "z1 : ", self.z1)

        self.a_predikat_2 = min(self.kecepatanLambat, self.suhuRendah)
        self.z2 = 7000 - self.a_predikat_2 * (7000-2000)
        print("A predikat 2 : ", self.a_predikat_2, " | ", "z2 : ", self.z2)

        self.a_predikat_3 = min(self.kecepatanCepat, self.suhuTinggi)
        self.z3 = 2000 - self.a_predikat_3 * (2000-7000)
        print("A predikat 3 : ", self.a_predikat_3, " | ", "z3 : ", self.z3)

        self.a_predikat_4 = min(self.kecepatanCepat, self.suhuRendah)
        self.z4 = 2000 - self.a_predikat_4 * (2000-7000)
        print("A predikat 4 : ", self.a_predikat_4, " | ", "z4 : ", self.z4)

    def defuzziFikasi(self) :
        self.a_pred_z = (self.a_predikat_1 * self.z1) + (self.a_predikat_2 * self.z2) + (self.a_predikat_3 * self.z3) + (self.a_predikat_4 * self.z4)

        self.z = self.a_predikat_1 + self.a_predikat_2 + self.a_predikat_3 + self.a_predikat_4
        self.zTotal = self.a_pred_z/self.z

        print("Output Fuzzy berupa Frekuensi Kipas : ", self.zTotal, "Hz")

testFuzzy = fuzzy()
testFuzzy.fuzzyKecepatan(4000)
print("=======================")
testFuzzy.fuzzifikasiSuhu(300)
print("=======================")
testFuzzy.mesinInferensiTsukamoto()
print("=======================")
testFuzzy.defuzziFikasi()
