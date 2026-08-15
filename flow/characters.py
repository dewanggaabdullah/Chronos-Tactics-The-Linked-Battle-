from flow import attributes as un
import copy


KARAKTER_VALID = [
    "elsa",
    "bruno",
    "dewa",
    "joy",
    "mikasa"
]


def pemilihan_karakter(*nama_karakter):
    """
    Membuat tim pemain berdasarkan nama karakter.

    Setiap karakter disalin dengan deepcopy agar
    perubahan status selama permainan tidak mengubah
    data karakter asli di attributes.py.
    """

    tim_pemain = {}

    for nama in nama_karakter:
        nama = str(nama).lower()

        if nama in un.attribute_karakter:
            tim_pemain[nama] = copy.deepcopy(
                un.attribute_karakter[nama]
            )

    return tim_pemain


def validasi_karakter(nama_karakter):
    """
    Memvalidasi satu nama karakter.

    Mengembalikan True jika karakter tersedia.
    """

    nama_karakter = str(nama_karakter).lower()

    return nama_karakter in KARAKTER_VALID


def tambah_karakter_ke_tim(nama_karakter, tim_pemain):
    nama_karakter = str(nama_karakter).lower()

    if not validasi_karakter(nama_karakter):
        return {
            "berhasil": False,
            "pesan": "Karakter tidak ditemukan."
        }

    if nama_karakter in tim_pemain:
        return {
            "berhasil": False,
            "pesan": "Karakter sudah ada di dalam tim."
        }

    karakter = un.attribute_karakter[nama_karakter]

    tim_pemain[nama_karakter] = copy.deepcopy(karakter)

    return {
        "berhasil": True,
        "pesan": f"{nama_karakter} berhasil ditambahkan."
    }