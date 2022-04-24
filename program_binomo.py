from primitif_function import *
from F02_register import register
from F03_login import login
from F04_tambah_game import tambah_game
from F05_ubah_game import ubah_game
from F06_ubah_stock import ubah_stock
from F07_list_game_toko import list_game_toko
from F08_buy_game import buy_game
from F09_list_game import list_game
from F12_topup import topup
from F14_help import help
from F15_load import load
from F16_save import save
from F17_exit import exit

from B02_magic_shell import kerang_ajaib

import os
import sys
import time

path_folder = load()

if path_folder == None:
    print()
elif path_folder != None:
    print("Mohon tunggu")
    # sys.stdout.write("Loading")
    # sys.stdout.flush()
    # time.sleep(3)
    # for i in range(3):
    #     sys.stdout.write('.')
    #     sys.stdout.flush()
    #     time.sleep(1)

    print("\nSelamat datang di antarmuka \"Binomo\"")

    # Pembuatan memori
    arrGame = buat_tabData(os.path.join(path_folder, 'game.csv'))
    arrUser = buat_tabData(os.path.join(path_folder, 'user.csv'))
    arrRiwayat = buat_tabData(os.path.join(path_folder, 'riwayat.csv'))
    arrKepemilikan = buat_tabData(os.path.join(path_folder, 'kepemilikan.csv'))
    
    # Inisialisasi
    isLogin = False; exitGame = False; pengguna = ['id', 'username', 'nama', 'password', 'role', 'saldo']

    while not(exitGame): 
        user_input = input(">>> ")

        if isLogin :
            if validasi_input(user_input, pengguna[4]) :
                if user_input == "register":
                    arrUser = register(arrUser)

                elif user_input == "tambah_game":
                    arrGame = tambah_game(arrGame)
                    pass

                elif user_input == "ubah_stok":
                    arrGame = ubah_stock(arrGame)

                elif user_input == "topup":
                    arrUser = topup(arrUser)
                
                elif user_input == "ubah_game":
                    arrGame = ubah_game(arrGame)

                elif user_input == "buy_game":
                    arrGame, arrUser, arrKepemilikan, arrRiwayat = buy_game(pengguna[0], arrGame, arrUser, arrKepemilikan, arrRiwayat)

                elif user_input == "list_game":
                    list_game(arrKepemilikan,arrGame,pengguna[0])
                
                elif user_input == "search_my_game":
                    # search_my_game()
                    # pakai arrKepemilikan dan arrGame
                    pass

                elif user_input == "riwayat":
                    # riwayat()
                    # pakai arrRiwayat 
                    pass

                elif user_input == "list_game_toko":
                    list_game_toko(arrGame)

                elif user_input == "search_game_at_store":
                    # search_game_at_store()
                    # pakai arrGame
                    pass
            
                elif user_input == "save":
                    save(arrGame, arrUser, arrRiwayat, arrKepemilikan)

                elif user_input == "exit":
                    exit(pengguna[2],arrGame, arrUser, arrRiwayat, arrKepemilikan)
                    exitGame = True

                elif user_input == "help":
                    help(isLogin,pengguna[4])
                
                elif user_input == "kerangajaib":
                    kerang_ajaib()

        else:
            if user_input == "login":
                pengguna = login(pengguna,arrUser)
                if pengguna != ['id', 'username', 'nama', 'password', 'role', 'saldo']:
                    isLogin = True
            elif user_input == "help":
                help(isLogin,pengguna[4])
            else:
                print("Masukan anda tidak dikenali.\nKetik \"help\" untuk panduan penggunaan BINOMO")
