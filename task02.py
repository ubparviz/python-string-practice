import random

ism = input("Ismingizni kiriting: ")
sharif = input("Sharifingizni kiritng: ")
raqam = random.randint(1, 100)

print(f"""Sizga quyidaga "user name"larni taklif qilaman:   
        {ism}.{sharif}
        {ism}\\_{sharif}
        {ism[0]}{sharif}{raqam}
        {ism}{sharif[0]}"""  )