jawaban = []


def prime_check(angka=int(input("MASUKKAN ANGKA: "))):
    for i in range(1, angka + 1):
        if angka % i == 0:
            jawaban.append(i)

    if angka == 1 or angka == 0:
        print("PRIME")


    elif jawaban[0] == 1 and jawaban[1] == angka:
        print("PRIME")

    else:
        print("Not PRIME")


prime_check()