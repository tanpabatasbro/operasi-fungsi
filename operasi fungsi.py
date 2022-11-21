def kuadrat(input_angka):
    output_kuadrat = input_angka**2
    return output_kuadrat
y = kuadrat(3)
print(y)
print(kuadrat(7))
z = 10 + kuadrat(7)
print(z)

#fungsi tambah dengan  returnn
def fungsi_tambah(angka_1,angka_2):
    return angka_1 + angka_2
a = fungsi_tambah(10,7)
print(a)



#fungsi (+,-,*,/)
def operasi_mtk(angka_1,angka_2):
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2

    return tambah,kurang,kali,bagi
k,l,m,n = operasi_mtk(3,5)

print(f"hasil tambah = {k}")
print(f"hasil kurang = {l}")
print(f"hasil kali = {m}")
print(f"hasil bagi = {n}")
