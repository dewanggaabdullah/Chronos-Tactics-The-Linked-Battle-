class TurnNode:
    def __init__(self, nomor_turn, data_tim, data_monster):
        self.nomor_turn = nomor_turn
        
        # Kita pakai copy agar data yang disimpan adalah rekaman asli saat turn itu, bukan referensi objek yang terus berubah
        import copy

        self.data_tim = copy.deepcopy(data_tim)
        self.data_monster = copy.deepcopy(data_monster)

        self.next = None  # Menunjuk ke turn setelahnya
        self.prev = None  # Menunjuk ke turn sebelumnya (buat rewind!)

class TurnHistory:
    def __init__(self):
        self.head = None
        self.current = None  # Pointer untuk memantau kita lagi di turn mana sekarang

    def catat_turn(self, nomor_turn, tim, monster):
        new_node = TurnNode(nomor_turn, tim, monster)

        if not self.head:
            self.head = new_node
            self.current = new_node
        else:
            # Sambungkan turn baru di ujung current saat ini
            self.current.next = new_node
            new_node.prev = self.current
            self.current = new_node  # maju ke turn terbaru 

    def konfirmasi_rewind(self):
        # Begitu turn dipilih, potong masa depan dari titik ini
        if self.current:
            self.current.next = None
        return self.current

    def rewind(self):
        # mundur 1 turn ke belakang jika ada turn sebelumnya
        if self.current and self.current.prev:
            self.current = self.current.prev

            # Putus turn setelahnya karena kita udah nulis timeline baru
            self.current.next = None 
            return self.current

        return None
