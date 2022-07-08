from fuzzy import (
    down,
    Permintaan,
    Persediaan,
    Produksi,
    up
)

class PermintaanBaru(Permintaan):
    nilai_tengah = 4500

    def turun(self, x):
        if x >= self.nilai_tengah:
            return 0
        elif x<= self.minimum:
            return 1
        else:
            return down(x, self.minimum, self.nilai_tengah)
    
    def tetap(self, x):
        if x >= self.maximum or x<= self.minimum:
            return 0
        elif self.minimum < x < self.nilai_tengah:
            return up(x, self.minimum, self.nilai_tengah)
        elif self.nilai_tengah < x < self.maximum:
            return down(x, self.nilai_tengah, self.maximum)
        else:
            return 1

    def naik(self, x):
        if x >= self.maximum:
            return 1
        elif x<= self.nilai_tengah:
            return 0
        else:
            return up(x, self.nilai_tengah, self.maximum)
    
class ProduksiBaru(Produksi):

    def inferensi(self):
        permintaan_baru = PermintaanBaru()
        stok = Persediaan()
        data_inferensi = super().inferensi(permintaan_baru=permintaan_baru)

        a5 = min(permintaan_baru.tetap(self.permintaan), stok.sedikit(self.persediaan))
        z5 = self.bertambah(a5)
        data_inferensi.append((a5, z5))

        a6 = min(permintaan_baru.tetap(self.permintaan), stok.sedikit(self.persediaan))
        z6 = self.berkurang(a6)
        data_inferensi.append((a6, z6))
        return data_inferensi

    def defuzifikasi(self):
        return super().defuzifikasi(self.inferensi())



pm = Permintaan()
print("=====Permintaan=====")
print("Permintaan Minimum", pm.minimum)
print("Permintaan Maximum", pm.maximum)

psd = Persediaan()
print("=====Persediaan=====")
print("Persedian Minimum", psd.minimum)
print("Persedian Maximum", psd.maximum)

pd = Produksi()
print("=====Produksi=====")
print("Produksi Minimum", pd.minimum)
print("Produksi Maximum", pd.maximum)