import pandas as pd

# Fuzzifikasi Penghasilan

# Klasifikasi Fuzzy Penghasilan Tinggi
def penghasilanTinggi(n):
    nilaiFuzzy = 0
    if n > 19.69:
        nilaiFuzzy = 1
    elif n <= 15.94:
        nilaiFuzzy = 0
    else:
        nilaiFuzzy = (n - 15.94) / (19.69 - 15.94)
    return round(nilaiFuzzy, 2)


# Klasifikasi Fuzzy Penghasilan Rendah
def penghasilanRendah(n):
    nilaiFuzzy = 0
    if n <= 4.62:
        nilaiFuzzy = 1
    elif n >= 8.39:
        nilaiFuzzy = 0
    else:
        nilaiFuzzy = (8.39 - n) / (8.39 - 4.62)
    return round(nilaiFuzzy, 2)


# Klasifikasi Fuzzy Penghasilan Menengah Bawah
def penghasilanMenRendah(n):
    nilaiFuzzy = 0
    if n > 8.39 and n <= 9.40:
        nilaiFuzzy = (n - 8.39) / (9.40 - 8.39)
    elif n > 9.40 and n <= 11.17:
        nilaiFuzzy = 1
    elif n > 11.17 and n <= 12.17:
        nilaiFuzzy = (12.17 - n) / (12.17 - 11.17)
    else:
        nilaiFuzzy = 0
    return round(nilaiFuzzy, 2)


# Klasifikasi Fuzzy Penghasilan Menengah Atas
def penghasilanMenTinggi(n):
    nilaiFuzzy = 0
    if n > 12.17 and n <= 13.33:
        nilaiFuzzy = (n - 12.17) / (13.18 - 12.17)
    elif n > 13.33 and n <= 14.63:
        nilaiFuzzy = 1
    elif n > 14.63 and n <= 15.93:
        nilaiFuzzy = (15.96 - n) / (15.96 - 14.63)
    else:
        nilaiFuzzy = 0
    return round(nilaiFuzzy, 2)


# Fuzzifikasi Pengeluaran

# Klasifikasi Fuzzy Pengeluaran Tinggi
def pengeluaranTinggi(n):
    nilaiFuzzy = 0
    if n >= 11.29:
        nilaiFuzzy = 1
    elif n <= 9.29:
        nilaiFuzzy = 0
    else:
        nilaiFuzzy = (n - 9.29) / (11.29 - 9.29)
    return nilaiFuzzy


# Klasifikasi Fuzzy Pengeluaran Rendah
def pengeluaranRendah(n):
    nilaiFuzzy = 0
    if n <= 3.44:
        nilaiFuzzy = 1
    elif n > 5.29:
        nilaiFuzzy = 0
    else:
        nilaiFuzzy = (5.29 - n) / (5.29 - 3.44)
    return nilaiFuzzy


# Klasifikasi Fuzzy Pengeluaran Menengah Rendah
def pengeluaranMenRendah(n):
    nilaiFuzzy = 0
    if n > 5.28 and n <= 6.00:
        nilaiFuzzy = (n - 6.00) / (6.00 - 5.28)
    elif n > 6.00 and n <= 6.55:
        nilaiFuzzy = 0
    elif n > 6.55 and n <= 7.28:
        nilaiFuzzy = (7.28 - n) / (7.28 - 6.55)
    else:
        nilaiFuzzy = 0
    return nilaiFuzzy


# Klasifikasi Fuzzy Pengeluaran Menengah Atas
def pengeluaranMenTinggi(n):
    nilaiFuzzy = 0
    if n > 7.28 and n <= 8.00:
        nilaiFuzzy = (n - 8.00) / (8.00 - 7.28)
    elif n > 8.00 and n <= 8.56:
        nilaiFuzzy = 1
    elif n > 8.56 and n <= 9.28:
        nilaiFuzzy = (9.28 - n) / (9.28 - 8.57)
    else:
        nilaiFuzzy = 0
    return nilaiFuzzy


# Fuzzy Interference
def interference(fuzzifikasiPenghasilan, fuzzifikasiPengeluaran):
    rules = [
        [min(fuzzifikasiPenghasilan[0], fuzzifikasiPengeluaran[0]), "Mungkin"],
        [min(fuzzifikasiPenghasilan[0], fuzzifikasiPengeluaran[1]), "Mungkin"],
        [min(fuzzifikasiPenghasilan[0], fuzzifikasiPengeluaran[2]), "Ya"],
        [min(fuzzifikasiPenghasilan[0], fuzzifikasiPengeluaran[3]), "Ya"],
        [min(fuzzifikasiPenghasilan[1], fuzzifikasiPengeluaran[0]), "Tidak"],
        [min(fuzzifikasiPenghasilan[1], fuzzifikasiPengeluaran[1]), "Tidak"],
        [min(fuzzifikasiPenghasilan[1], fuzzifikasiPengeluaran[2]), "Mungkin"],
        [min(fuzzifikasiPenghasilan[1], fuzzifikasiPengeluaran[3]), "Mungkin"],
        [min(fuzzifikasiPenghasilan[2], fuzzifikasiPengeluaran[0]), "Tidak"],
        [min(fuzzifikasiPenghasilan[2], fuzzifikasiPengeluaran[1]), "Tidak"],
        [min(fuzzifikasiPenghasilan[2], fuzzifikasiPengeluaran[2]), "Mungkin"],
        [min(fuzzifikasiPenghasilan[2], fuzzifikasiPengeluaran[3]), "Mungkin"],
        [min(fuzzifikasiPenghasilan[3], fuzzifikasiPengeluaran[0]), "Tidak"],
        [min(fuzzifikasiPenghasilan[3], fuzzifikasiPengeluaran[1]), "Tidak"],
        [min(fuzzifikasiPenghasilan[3], fuzzifikasiPengeluaran[2]), "Tidak"],
        [min(fuzzifikasiPenghasilan[3], fuzzifikasiPengeluaran[3]), "Mungkin"],
    ]

    # inisialisasi array kemungkinan
    ya = []
    mungkin = []
    tidak = []

    # Looping memasukanan kemungkinan
    for i in range(len(rules)):
        if rules[i][1] == "Tidak":
            tidak.append(rules[i][0])
        elif rules[i][1] == "Mungkin":
            mungkin.append(rules[i][0])
        elif rules[i][1] == "Ya":
            ya.append(rules[i][0])
    return ya, mungkin, tidak


# clipping technique
def clipping(listHasil, parameter):
    for i in range(len(listHasil)):
        if listHasil[i] > parameter:
            listHasil[i] = parameter
        else:
            continue
    return listHasil


# rule output
# aturan untuk rejected
def rejected(n):
    nilaiOutput = 0
    if n <= 40:
        nilaiOutput = 1
    elif n > 40 and n <= 60:
        nilaiOutput = (60 - n) / (60 - 40)
    else:
        nilaiOutput = 0
    return nilaiOutput


# aturan untuk considered
def considered(n):
    nilaiOutput = 0
    if n > 40 and n < 60:
        nilaiOutput = (n - 40) / (60 - 40)
    elif n > 60 and n <= 80:
        nilaiOutput = (80 - n) / (80 - 60)
    elif n == 60:
        nilaiOutput = 1
    else:
        nilaiOutput = 0
    return nilaiOutput


# aturan untuk accepted
def accepted(n):
    nilaiOutput = 0
    if n >= 80:
        nilaiOutput = 1
    elif n >= 60 and n < 80:
        nilaiOutput = (n - 60) / (80 - 60)
    else:
        nilaiOutput = 0
    return nilaiOutput


# prepare list random untuk defuzzifikasi
def listDefuzzifikasiMamdani(listDefuzifikasi):
    listOutput = []
    for x in listDefuzifikasi:
        rejectedValue = rejected(x)
        consideredValue = considered(x)
        acceptedValue = accepted(x)
        listOutput.append([rejectedValue, consideredValue, acceptedValue])
    return listOutput


# membagi list random berdasarkan kategori
def listDefuzzifikasiClassificator(listAwal):
    listYa = []
    listTidak = []
    listMungkin = []
    for x in listAwal:
        for i in range(len(x)):
            if i == 0:
                listTidak.append(x[i])
            elif i == 1:
                listMungkin.append(x[i])
            else:
                listYa.append(x[i])
    return listYa, listTidak, listMungkin


# menyatukan list clipping
def joiningList(ya, mungkin, tidak, panjangHasil):
    listJoin = []
    for i in range(panjangHasil):
        listJoin.append([tidak[i], mungkin[i], ya[i]])
    return listJoin


# clipping technique
def clippingTechnique(parameter, listAwal):
    listClipping = []
    for i in range(len(listAwal)):
        if listAwal[i] > parameter:
            listClipping.append(parameter)
        else:
            listClipping.append(listAwal[i])
    return listClipping


# mencari miu bi
def miuBi(listClipping):
    listMiu = []
    for x in listClipping:
        listMiu.append(max(x))
    return listMiu


# Defuzzifikasi Mamdani
def defuzzifikasi(listDefuzzifikasi, listMiu):
    sumDefuzziMiu = 0
    sumMiu = 0
    for i in range(len(listDefuzifikasi)):
        sumDefuzziMiu += listDefuzzifikasi[i] * listMiu[i]
        sumMiu += listMiu[i]
    if sumMiu == 0:
        hasilAkhir = 0
    else:
        hasilAkhir = sumDefuzziMiu / sumMiu
    return hasilAkhir


# Defuzzifikasi Sugeno
def defuzzifikasiSugeno(ya, mungkin, tidak):
    if ya + mungkin + tidak == 0:
        sumValue = 0
    else:
        sumValue = (ya * 100) + (mungkin * 85) + (tidak * 50) // (ya + mungkin + tidak)
    return sumValue


################################ MAIN PROGRAM ######################################

# inisialisasi list
dataMahasiswa = []
dataPenghasilan = []
dataPengeluaran = []
listFuzzifikasiPenghasilan = []
listFuzzifikasiPengeluaran = []
listBantuan = []

# loading data
dataMahasiswa = pd.read_excel("Mahasiswa.xls")
dataPenghasilan = dataMahasiswa["Penghasilan"]
dataPengeluaran = dataMahasiswa["Pengeluaran"]

# Fuzzifikasi Penghasilan
for x in dataPenghasilan:
    rendahPenghasilan = penghasilanRendah(x)
    menengahBawahPenghasilan = penghasilanMenRendah(x)
    menengahAtasPenghasilan = penghasilanMenTinggi(x)
    tinggiPenghasilan = penghasilanTinggi(x)
    listFuzzifikasiPenghasilan.append(
        [
            rendahPenghasilan,
            menengahBawahPenghasilan,
            menengahAtasPenghasilan,
            tinggiPenghasilan,
        ]
    )

# Fuzzifikasi Pengeluaran
for x in dataPengeluaran:
    rendahPengeluaran = pengeluaranRendah(x)
    menengahBawahPengeluaran = pengeluaranMenRendah(x)
    menengahAtasPengeluaran = pengeluaranMenTinggi(x)
    tinggiPengeluaran = pengeluaranTinggi(x)
    listFuzzifikasiPengeluaran.append(
        [
            rendahPengeluaran,
            menengahBawahPengeluaran,
            menengahAtasPengeluaran,
            tinggiPengeluaran,
        ]
    )

listDefuzifikasi = [
    0,
    5,
    10,
    15,
    20,
    25,
    30,
    35,
    40,
    45,
    50,
    55,
    60,
    65,
    70,
    75,
    80,
    85,
    90,
    95,
    100,
]
listHasil = listDefuzzifikasiMamdani(listDefuzifikasi)
panjangListHasil = len(listHasil)
listYa, listTidak, listMungkin = listDefuzzifikasiClassificator(listHasil)

# Interferensi dan Defuzzifikasi
for i in range(len(dataMahasiswa)):
    ya, mungkin, tidak = interference(
        listFuzzifikasiPenghasilan[i], listFuzzifikasiPengeluaran[i]
    )
    parameterYa = max(ya)
    parameterMungkin = max(mungkin)
    parameterTidak = max(tidak)

    # Inisialisasi list Clipping
    listClipping = []
    listClippingYa = []
    listClippingMungkin = []
    listClippingTidak = []
    listMiu = []
    # Clipping Techniques
    listClippingYa = clippingTechnique(parameterYa, listYa)
    listClippingTidak = clippingTechnique(parameterTidak, listTidak)
    listClippingMungkin = clippingTechnique(parameterMungkin, listMungkin)
    listClipping = joiningList(
        listClippingYa, listClippingMungkin, listClippingTidak, panjangListHasil
    )
    # Cari Miu Bi
    listMiu = miuBi(listClipping)

    # Defuzzifikasi Mamdani
    nilaiAkhir = defuzzifikasi(listDefuzifikasi, listMiu)

    # Testing Defuzzifikasi Sugeno
    # nilaiAkhir = defuzzifikasiSugeno(parameterYa, parameterMungkin, parameterTidak)

    if nilaiAkhir == 0:
        continue
    else:
        listBantuan.append([round(nilaiAkhir, 3), i + 1])
listBantuan.sort(reverse=True)

listAkhir = []
for i in range(0, 20):
    listAkhir.append(listBantuan[i][1])

# simpan ke excel
dataExport = pd.DataFrame(listAkhir, columns=["Penerima Bantuan"])
dataExport.to_excel("Bantuan.xls", index=False, header=True)

