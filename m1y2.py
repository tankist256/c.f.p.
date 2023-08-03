import random

# Символы, из которых может состоять пароль пользователя
allowed_characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# Запрос у пользователя длины пароля
password_length = int(input("Введите длину пароля: "))

# Переменная для хранения сгенерированного пароля
generated_password = ""

# Генерация пароля с помощью цикла и random.choice
for _ in range(password_length):
    generated_password += random.choice(allowed_characters)

print("Сгенерированный пароль:", generated_password)
