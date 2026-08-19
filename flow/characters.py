from flow import attributes as un
import copy


def validasi_karakter(nama_karakter):
    """
    Memvalidasi satu nama karakter.

    Mengembalikan True jika karakter tersedia.
    """

    nama_karakter = str(nama_karakter).lower()

    return nama_karakter in un.attribute_karakter


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


def atur_karakter_turn(nama_karakter, game_state):
    """
    Menentukan karakter yang akan bertindak pada turn saat ini.
    """

    nama_karakter = str(nama_karakter).lower()

    if nama_karakter not in game_state["tim_pemain"]:
        return {
            "berhasil": False,
            "log": "Karakter tidak ada di dalam tim."
        }

    karakter = game_state["tim_pemain"][nama_karakter]

    # Simpan karakter yang sedang mendapat giliran
    game_state["karakter_aktif"] = nama_karakter

    return {
        "berhasil": True,
        "karakter": nama_karakter,
        "log": f"{nama_karakter.capitalize()} dipilih."
    }