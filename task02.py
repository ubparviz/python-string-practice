import random

ism = input("Ismingizni kiriting: ")
sharif = input("Sharifingizni kiritng: ")
raqam = random.randint(1, 100)

print(f"""Sizga quyidaga "user name"larni taklif qilaman:   
        \n{ism}.{sharif}
        \n{ism}\\_{sharif}
        \n{ism[0]}{sharif}{raqam}
        \n{ism}{sharif[0]}"""  )