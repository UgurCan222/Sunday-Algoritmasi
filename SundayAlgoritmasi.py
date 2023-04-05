metin = 'abcadabadccdbabd'
desen = 'cadab'

def sunday_algoritması(metin, desen):
    n = len(metin)  # metnin uzunluğu
    m = len(desen)  # desenin uzunluğu
    i = 0  # metin indeksi
    j = 0  # desen indeksi
    while i < n:
        if metin[i] == desen[j]:
            if j == m - 1:
                return i - m + 1  # desen bulundu
            j += 1
            i += 1
        else:
            if i + m < n:
                k = m - 1
                while k >= 0 and metin[i + k] != desen[k]:
                    k -= 1
                i = i + m - k
                j = 0
            else:
                break
    return -1  # desen bulunamadı

print(sunday_algoritması(metin, desen))  