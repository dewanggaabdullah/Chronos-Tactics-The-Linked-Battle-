def proses_aksi(aksi):
    if aksi == "audio":
        return {
            "menu": "settings",
            "fitur": "audio",
            "status": "Fitur Audio masih dalam tahap pengembangan."
        }

    if aksi == "grafis":
        return {
            "menu": "settings",
            "fitur": "grafis",
            "status": "Fitur Grafis masih dalam tahap pengembangan."
        }

    return {
        "menu": "settings",
        "status": "Pengaturan tidak dikenal."
    }