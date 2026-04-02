from flow import utils as ut

def cerita_karakter():
    deskripsi_elsa = "-- elsa --\nelsa merupakan seorang gadis manis yang suka membantu teman-temannya dan bercita cita menjadi dokter yang manis pula.\nstatistik:\nhp: 75\natk: 5\nkemampuan:  dapat menambah hp rekan tiap ronde sebanyak 7"

    deskripsi_bruno ="-- bruno --\ndia seorang anak kuat yang hobi nge-gym dan suka melakukan aktifitas fisik berat.\nstatistik:\nhp: 150\natk: 12\nkemampuan:  punya barbel raksasa yang dapat menangkis serangan monster apapun dengan tidak melakukan penyerangan saat ronde berlangsung"

    deskripsi_dewa = "-- dewa --\nseorang anak yang suka mengotak atik barang dan belajar teknologi,dia pernah merakit drone kamikaze berbasis AGI untuk menghancurkan rumah tetangganya karna dia mengira tetangganya menciptakan nuklir,namun ternyata tidak ada apapun setelah diperiksa disana...\nstatistik:\nhp: 85\natk: 30\nkemampuan:  karna marsya menyuruhnya membawa peralatan siaga untukjaga-jaga (marsya suka dengan dewa jir...hahaha),dewa membawa banyak drone kamikaze untuk berpetualang ke antah-brantah yang jauh disana.\npasif: damage dasar tertinggi dalam tim"

    deskripsi_joy =  "-- joy --\nayah joy seorang ilmuan gila yang tergila gila pada kekebalan dan daya tahan tubuh. semenjak ibu joy meninggal dunia karna terpeleset dari lantai kamar mandi. joy mengambil suntikan eksperimen ayah nya secara diam-diam untuk dibawa (ku harap joy masih hidup setelah kembali dari petualangan dan menjelaskan pada ayahnya apa yang terjadi agar ayahnya tidak semakin gila...).\nstatistik:\nhp: 90\natk: 10\nkemampuan:  joy menyuntikan zat yang membuat semua temannya di dalam petualangan mendapatkan hp tambahan sebanyak 20. (waktu tunggu 3 babak)"

    deskripsi_mikasa ="-- mikasa --\nmikasa seorang anak yatim piatu yang dulunya terlantar di alun-alun kota. keluarga dewa mengadopsinya dan menganggapnya sebagai anak sendiri dan jadi saudara angkat bagi dewa. tidak tau kenapa, tapi mikasa sangat kuat dan lincah saat bertengkar dengan bruno dan hampir mengalahkannya demi dewa saat dewa berselisih dengan bruno dulu, padahal dia tidak pernah latihan fisik sangat keras seperti bruno.\nstatistik:\nhp: 90\natk: 10\nkemampuan:  saat bersama dewa, poin serangan mikasa bertambah sebanyak 10 poin dan saat hp dewa berada di bawah 30, seluruh poin serangan marsya meningkat sebanyak 100 persen"

    def prolog_karakter(karakter, durasi = 0.5):
        ut.print_story(karakter)
        print()
        ut.time.sleep(durasi)

    prolog_karakter(deskripsi_elsa)
    prolog_karakter(deskripsi_bruno)
    prolog_karakter(deskripsi_dewa)
    prolog_karakter(deskripsi_joy)
    prolog_karakter(deskripsi_mikasa)