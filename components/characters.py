from components import attributes as un
import copy


def validasi_karakter(nama_karakter):
    nama_karakter = str(nama_karakter).lower()

    return nama_karakter in un.attribute_karakter


def pemilihan_karakter(*nama_karakter):
    tim_pemain = {}

    for nama in nama_karakter:
        nama = str(nama).lower()

        if nama in un.attribute_karakter:
            tim_pemain[nama] = copy.deepcopy(
                un.attribute_karakter[nama]
            )

    return tim_pemain