from pynput import keyboard
import copy

def menu_interaktif(history, ut):
    posisi_awal = history.current 
    status = {"berjalan": True, "konfirmasi": False}

    def on_press(key):
        if key == keyboard.Key.left:
            if history.current and history.current.prev:
                history.current = history.current.prev
                render_layar()
        elif key == keyboard.Key.right:
            if history.current and history.current.next:
                history.current = history.current.next
                render_layar()
        elif key == keyboard.Key.enter:
            status["konfirmasi"] = True
            # turn_terpilih adalah node linked list yang ditunjuk user
                    
            # KUNCI OPTIMASI: Potong masa depan agar tidak menumpuk!
            if history.current:
                history.current.next = None
                history.tail = history.current
                    
                status["berjalan"] = False
                return False # keluar dari listener
        elif key == keyboard.Key.esc:
            status["konfirmasi"] = False
            status["berjalan"] = False
            history.current = posisi_awal 
            return False

    def render_layar():
        ut.bersihkan_terminal()
        print("=== CHRONOS TIME REWIND MANAGEMENT ===")
        print("Gunakan panah [<-] dan [->] untuk melihat riwayat turn.")
        print("Tekan [Enter] untuk konfirmasi kembali ke waktu ini, atau [Esc] untuk batal.\n")
        
        # Cetak Garis Timeline
        node_bantu = history.head
        timeline_str = ""
        while node_bantu:
            if node_bantu == history.current:
                timeline_str += f" [ Turn {node_bantu.nomor_turn} (CURRENT) ] <->"
            else:
                timeline_str += f" Turn {node_bantu.nomor_turn} <->"
            node_bantu = node_bantu.next
        print(timeline_str.rstrip(" <->"))
        print("-" * 50)
        
        # Preview Data
        curr = history.current
        print(f"PREVIEW KONDISI TURN {curr.nomor_turn}:")
        print(f" Monster HP: {curr.data_monster.hp}")
        print(" Tim Pemain:")
        for nama, char in curr.data_tim.items():
            print(f"  - {nama}: HP {char.hp}")

    render_layar()

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

    if status["konfirmasi"]:
        return history.konfirmasi_rewind()
    return None
