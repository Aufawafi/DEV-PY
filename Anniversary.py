import time
import os
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_heart(size):
    for i in range(size):
        for j in range(size+1):
            if (i == 0 and j % 3 != 0) or (i == 1 and j % 3 == 0) or (i - j == 2) or (i + j == size + 2):
                print("❤", end="")
            else:
                print(" ", end="")
        print()

def animate_text(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)  # Mengurangi waktu delay untuk animasi yang lebih cepat
    print()

def main():
    nama_pacar = input("Masukkan nama pacarmu: ")
    tahun = input("Berapa tahun anniversary kalian? ")
    ukuran_hati = int(input("Masukkan ukuran hati (angka ganjil, misalnya 5, 7, atau 9): "))
    
    messages = [
        f"Selamat anniversary yang ke-{tahun}, {nama_pacar}! ❤",
        f"{nama_pacar}, cintaku padamu tumbuh setiap hari. 💖",
        f"Terima kasih telah mewarnai hidupku selama {tahun} tahun ini, {nama_pacar}! 🌈",
        f"{tahun} tahun bersamamu terasa seperti mimpi indah, {nama_pacar}. 😊",
        f"Aku bersyukur memilikimu dalam hidupku, {nama_pacar}. Happy anniversary! 🙏"
    ]
    
    while True:
        clear_screen()
        print_heart(ukuran_hati)
        time.sleep(1)
        
        clear_screen()
        animate_text(random.choice(messages))
        time.sleep(2)
        
        choice = input("Tekan Enter untuk melihat pesan lain, atau ketik 'q' untuk keluar: ")
        if choice.lower() == 'q':
            break
    
    print(f"\nTerima kasih, {nama_pacar}. Aku mencintaimu! ❤")

if __name__ == "__main__":
    main()