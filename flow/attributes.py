class Dasar_Karakter:
    def __init__(self, nama, hp, atk):
        self.nama = nama
        self.hp = hp
        self.max_hp = hp

        self.atk = atk
        self.atk_dasar = atk

        # Default: karakter tidak memiliki skill pasif.
        self.skill_pasif = False

    def menyerang(self, target):
        """
        Melakukan basic attack kepada target.
        """

        damage = self.atk
        hasil_serangan = target.menerima_serangan(damage)

        return {
            "berhasil": True,
            "aksi": "basic_attack",
            "karakter": self.nama,
            "damage": damage,
            "target": target.nama,
            "hasil_target": hasil_serangan
        }

    def menerima_serangan(self, damage):
        """
        Menerima damage dari target.
        """

        self.hp = max(0, self.hp - damage)

        if self.hp <= 0:
            return {
                "berhasil": True,
                "kalah": True,
                "karakter": self.nama,
                "hp": self.hp
            }

        return {
            "berhasil": True,
            "kalah": False,
            "karakter": self.nama,
            "hp": self.hp
        }

    def jalankan_pasif(self, **kwargs):
        """
        Menjalankan passive skill jika karakter memilikinya.
        """

        if not self.skill_pasif:
            return None

        fungsi_pasif = getattr(
            self,
            "gunakan_skill_pasif",
            None
        )

        if not callable(fungsi_pasif):
            return None

        return fungsi_pasif(**kwargs)

    def skill_aktif(self, **kwargs):
        """
        Menjalankan active skill karakter.

        Keputusan apakah pemain ingin menggunakan
        basic attack atau skill aktif dilakukan oleh
        layer game/UI, bukan oleh class karakter.
        """

        fungsi_skill = getattr(
            self,
            "gunakan_skill",
            None
        )

        if not callable(fungsi_skill):
            return {
                "berhasil": False,
                "aksi": "skill",
                "alasan": "tidak_memiliki_skill_aktif"
            }

        return fungsi_skill(**kwargs)

    def kurangi_cooldown(self):
        """
        Mengurangi cooldown karakter jika tersedia.
        """

        cooldown = getattr(self, "cooldown", 0)

        if cooldown > 0:
            self.cooldown -= 1

    def setup_statistik_awal(self):
        """
        Mengembalikan statistik karakter ke kondisi awal.
        """

        self.hp = self.max_hp
        self.atk = self.atk_dasar


class Elsa(Dasar_Karakter):
    def __init__(self, nama, hp, atk):
        super().__init__(nama, hp, atk)

        self.healing = 7
        self.skill_pasif = True

    def gunakan_skill_pasif(self, **kwargs):
        """
        Elsa memulihkan HP anggota tim yang masih hidup
        tetapi HP-nya belum penuh.
        """

        tim = kwargs.get("tim_pemain")

        if not tim:
            return {
                "berhasil": False,
                "aksi": "passive",
                "karakter": self.nama,
                "alasan": "tim_kosong"
            }

        pemulihan = []

        for anggota in tim.values():

            if 0 < anggota.hp < anggota.max_hp:
                hp_sebelum = anggota.hp

                anggota.hp = min(
                    anggota.hp + self.healing,
                    anggota.max_hp
                )

                pemulihan.append({
                    "karakter": anggota.nama,
                    "hp_sebelum": hp_sebelum,
                    "hp_sesudah": anggota.hp,
                    "healing": anggota.hp - hp_sebelum
                })

        return {
            "berhasil": True,
            "aksi": "passive",
            "karakter": self.nama,
            "efek": "healing",
            "jumlah_healing": self.healing,
            "target": pemulihan
        }


class Bruno(Dasar_Karakter):
    def __init__(self, nama, hp, atk):
        super().__init__(nama, hp, atk)

        self.cooldown = 0
        self.menangkis = False

    def gunakan_skill(self, **kwargs):
        """
        Mengaktifkan mode bertahan Bruno.

        Bruno tidak menyerang pada turn ini.
        Serangan monster berikutnya akan diblokir.
        """

        if self.cooldown > 0:
            return {
                "berhasil": False,
                "aksi": "skill",
                "karakter": self.nama,
                "skill": "menangkis",
                "alasan": "cooldown",
                "cooldown": self.cooldown
            }

        self.menangkis = True

        return {
            "berhasil": True,
            "aksi": "skill",
            "karakter": self.nama,
            "skill": "menangkis",
            "status": "menangkis_aktif"
        }

    def menerima_serangan(self, damage):
        """
        Bruno dapat membatalkan serangan monster
        ketika mode menangkis aktif.
        """

        if self.menangkis:

            self.menangkis = False
            self.cooldown = 3

            return {
                "berhasil": True,
                "kalah": False,
                "karakter": self.nama,
                "hp": self.hp,
                "damage_diterima": 0,
                "serangan_diblokir": True,
                "cooldown": self.cooldown
            }

        return super().menerima_serangan(damage)

    def setup_statistik_awal(self):
        super().setup_statistik_awal()

        self.cooldown = 0
        self.menangkis = False


class Joy(Dasar_Karakter):
    def __init__(self, nama, hp, atk):
        super().__init__(nama, hp, atk)

        self.suntik_daya_tahan = 20
        self.cooldown = 0
        self.skill_pasif = False

    def gunakan_skill(self, **kwargs):
        """
        Active skill Joy memberikan tambahan HP
        kepada seluruh anggota tim yang masih hidup.
        """

        tim = kwargs.get("tim_pemain")

        if self.cooldown > 0:
            return {
                "berhasil": False,
                "aksi": "skill",
                "karakter": self.nama,
                "skill": "suntikan",
                "alasan": "cooldown",
                "cooldown": self.cooldown
            }

        if not tim:
            return {
                "berhasil": False,
                "aksi": "skill",
                "karakter": self.nama,
                "skill": "suntikan",
                "alasan": "tim_kosong"
            }

        penerima = []

        for anggota in tim.values():
            if anggota.hp > 0:
                hp_sebelum = anggota.hp

                anggota.hp += self.suntik_daya_tahan

                penerima.append({
                    "karakter": anggota.nama,
                    "hp_sebelum": hp_sebelum,
                    "hp_sesudah": anggota.hp,
                    "healing": self.suntik_daya_tahan
                })

        self.cooldown = 4

        return {
            "berhasil": True,
            "aksi": "skill",
            "karakter": self.nama,
            "skill": "suntikan",
            "jumlah_healing": self.suntik_daya_tahan,
            "target": penerima,
            "cooldown": self.cooldown
        }

    def setup_statistik_awal(self):
        super().setup_statistik_awal()

        self.cooldown = 0


class Dewa(Dasar_Karakter):
    def __init__(self, nama, hp, atk):
        super().__init__(nama, hp, atk)

        self.cooldown = 3
        self.damage_dasar = atk
        self.damage_critical = 40
        self.skill_pasif = True

    def gunakan_skill_pasif(self, **kwargs):
        """
        Passive Dewa menentukan apakah basic attack
        pada turn ini menjadi critical attack.
        """

        if self.cooldown == 0:
            self.atk = self.damage_critical
            self.cooldown = 4

            return {
                "berhasil": True,
                "aksi": "passive",
                "karakter": self.nama,
                "efek": "critical",
                "damage": self.damage_critical
            }

        # Jika belum siap critical, kembalikan ATK
        # ke nilai dasarnya.
        self.atk = self.damage_dasar

        return {
            "berhasil": False,
            "aksi": "passive",
            "karakter": self.nama,
            "efek": None,
            "cooldown": self.cooldown
        }

    def setup_statistik_awal(self):
        super().setup_statistik_awal()

        self.cooldown = 3
        self.atk = self.damage_dasar


class Mikasa(Dasar_Karakter):
    def __init__(self, nama, hp, atk):
        super().__init__(nama, hp, atk)

        self.bonus_serangan = 10
        self.mode_ngamuk = False
        self.skill_pasif = True
        self.sudah_depresi = False
        self.bersama_dewa = False

    def gunakan_skill_pasif(self, **kwargs):
        """
        Passive Mikasa bergantung pada kondisi Dewa
        di dalam tim pemain.

        Kondisi:
        1. Dewa hidup  -> Mikasa mendapat +10 ATK.
        2. Dewa kritis -> Mikasa masuk mode ngamuk.
        3. Dewa pulih  -> mode ngamuk berakhir.
        4. Dewa mati/tidak ada -> Mikasa depresi.
        """

        tim = kwargs.get("tim_pemain", {})

        dewa = None

        for karakter in tim.values():
            if karakter.nama.lower() == "dewa" and karakter.hp > 0:
                dewa = karakter
                break

        # ==================================================
        # DEWA MASIH HIDUP
        # ==================================================

        if dewa:

            # Mikasa kembali mendapatkan hubungan dengan Dewa.
            if not self.bersama_dewa:
                self.atk += self.bonus_serangan
                self.bersama_dewa = True

            # Jika sebelumnya depresi, pulihkan status depresi.
            if self.sudah_depresi:
                self.atk *= 2
                self.sudah_depresi = False

            # ==================================================
            # DEWA KRITIS
            # ==================================================

            if dewa.hp < 30 and not self.mode_ngamuk:
                self.atk *= 2
                self.mode_ngamuk = True

                return {
                    "berhasil": True,
                    "efek": "ngamuk",
                    "karakter": self.nama,
                    "log": (
                        f"{self.nama} mengamuk karena "
                        f"{dewa.nama} dalam kondisi kritis!"
                    )
                }

            # ==================================================
            # DEWA PULIH
            # ==================================================

            if dewa.hp >= 30 and self.mode_ngamuk:
                self.atk //= 2
                self.mode_ngamuk = False

                return {
                    "berhasil": True,
                    "efek": "ngamuk_berakhir",
                    "karakter": self.nama,
                    "log": (
                        f"{self.nama} kembali tenang karena "
                        f"{dewa.nama} tidak lagi kritis."
                    )
                }

        # ==================================================
        # DEWA MATI / TIDAK ADA
        # ==================================================

        else:

            # Kalau sebelumnya masih bersama Dewa,
            # lepaskan bonus +10 ATK.
            if self.bersama_dewa:
                self.atk -= self.bonus_serangan
                self.bersama_dewa = False

            # Matikan mode ngamuk jika masih aktif.
            if self.mode_ngamuk:
                self.atk //= 2
                self.mode_ngamuk = False

            # Terapkan depresi hanya sekali.
            if not self.sudah_depresi:
                self.atk //= 2
                self.sudah_depresi = True

                return {
                    "berhasil": True,
                    "efek": "depresi",
                    "karakter": self.nama,
                    "log": (
                        f"{self.nama} mengalami depresi "
                        f"karena Dewa telah gugur."
                    )
                }

        return {
            "berhasil": False,
            "efek": None,
            "karakter": self.nama
        }

    def setup_statistik_awal(self):
        super().setup_statistik_awal()

        self.mode_ngamuk = False
        self.sudah_depresi = False
        self.bersama_dewa = False


class Monster(Dasar_Karakter):
    def __init__(self, nama, hp):
        super().__init__(nama, hp, 0)

        self.daftar_atk = [40, 15, 17, 13]
        self.index_serangan = 0

    def menyerang(self, target):
        """
        Monster menyerang target menggunakan pola
        damage yang sudah ditentukan.
        """

        if self.hp <= 0:
            return {
                "berhasil": False,
                "log": f"{self.nama} sudah kalah."
            }

        damage = self.daftar_atk[self.index_serangan]

        hasil = target.menerima_serangan(damage)

        self.index_serangan += 1

        if self.index_serangan >= len(self.daftar_atk):
            self.index_serangan = 0

        return {
            "berhasil": True,
            "monster": self.nama,
            "target": target.nama,
            "damage": damage,
            "hasil_serangan": hasil
        }

    def setup_statistik_awal(self):
        self.hp = self.max_hp
        self.index_serangan = 0


elsa = Elsa("Elsa", 75, 5)
bruno = Bruno("Bruno", 150, 9)
dewa = Dewa("Dewa", 85, 15)
joy = Joy("Joy", 90, 10)
mikasa = Mikasa("Mikasa", 90, 10)

attribute_karakter = {
    "elsa": elsa,
    "bruno": bruno,
    "dewa": dewa,
    "joy": joy,
    "mikasa": mikasa
}