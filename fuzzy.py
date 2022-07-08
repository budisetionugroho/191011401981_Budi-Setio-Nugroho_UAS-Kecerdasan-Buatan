def down(x, xmin, xmax):
    return (xmax - x) / (xmax - xmin)

def up(x, xmin, xmax):
    return (x - xmin) / (xmax - xmin)

class Permintaan():
    minimum = 500
    maximum = 6000

    def turun(self, x):
        if x >= self.maximum:
            return 0
        elif x<= self.minimum:
            return 1
        else:
            return down(x, self.minimum, self.maximum)

    def naik(self, x):
        if x >= self.maximum:
            return 1
        elif x<= self.minimum:
            return 0
        else:
            return up(x, self.minimum, self.maximum)

class Persediaan():
    minimum = 200
    maximum = 800

    def sedikit(self, x):
        if x >= self.maximum:
            return 0
        elif x<= self.minimum:
            return 1
        else:
            return down(x, self.minimum, self.maximum)

    def banyak(self, x):
        if x >= self.maximum:
            return 1
        elif x<= self.minimum:
            return 0
        else:
            return up(x, self.minimum, self.maximum)


class Produksi():
    minimum = 3000
    maximum = 9000
    permintaan = 0
    persediaan = 0

    def berkurang(self, a):
        return self.maximum - a*(self.maximum - self.minimum)

    def bertambah(self, a):
        return a*(self.maximum - self.minimum) + self.minimum

    def inferensi(self, pmt=Permintaan(), psd=Persediaan()):
        result = []
        #  JIKA Permintaan TURUN, dan Persediaan BANYAK, MAKA
        # Produksi Barang BERKURANG.
        aturan1 = min(pmt.turun(self.permintaan), psd.banyak(self.persediaan))
        case1 = self.berkurang(aturan1)
        result.append((aturan1, case1))
        #  JIKA Permintaan TURUN, dan Persediaan SEDIKIT, MAKA
        # Produksi Barang BERKURANG.
        aturan2 = min(pmt.turun(self.permintaan), psd.sedikit(self.persediaan))
        case2 = self.berkurang(aturan2)
        result.append((aturan2, case2))
        #  JIKA Permintaan NAIK, dan Persediaan BANYAK, MAKA
        # Produksi Barang BERTAMBAH.
        aturan3 = min(pmt.naik(self.permintaan), psd.banyak(self.persediaan))
        case3 = self._bertambah(aturan3)
        result.append((aturan3, case3))
        #  JIKA Permintaan NAIK, dan Persediaan SEDIKIT, MAKA
        # Produksi Barang BERTAMBAH.
        aturan4 = min(pmt.naik(self.permintaan), psd.sedikit(self.persediaan))
        case4 = self.bertambah(aturan4)
        result.append((aturan4, case4))
        return result
    
    def defuzifikasi(self, data_inferensi=[]):
        data_inferensi = data_inferensi if data_inferensi else self.inferensi()
        res_a_z = 0
        res_a = 0
        for data in data_inferensi:
            res_a_z += data[0] * data[1]
            res_a += data[0]
        return res_a_z/res_a