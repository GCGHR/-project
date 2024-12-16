import random


def guess_number():
    # Генерируем случайное число от 1 до 100
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Привет! Я загадал число от 1 до 100. Попробуй угадать!")

    while True:
        # Ввод пользователя
        user_guess = input("Введите число: ")

        # Проверяем, является ли введённое значение числом
        if not user_guess.isdigit():
            print("Пожалуйста, введите целое число.")
            continue

        user_guess = int(user_guess)
        attempts += 1

        # Проверяем, угадал ли пользователь
        if user_guess < number_to_guess:
            print("Загаданное число больше.")
        elif user_guess > number_to_guess:
            print("Загаданное число меньше.")
        else:
            print(f"Поздравляю! Ты угадал число {
                  number_to_guess} за {attempts} попыток.")
            break


# Запуск игры
guess_number()
