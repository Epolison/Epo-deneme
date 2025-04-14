import random

def random_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password

passworld_length = int(input("lütfen şifre uzunluğunu girin:"))



print("Güçlü Rastgele Şifre:", random_password(passworld_length))
