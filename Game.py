import random

def guess_number():
    print("Привет! Добро пожаловать в игру!")
    
    # Уровни сложности
    difficulty = input("Выберите уровень сложности (легкий, средний, сложный): ").lower()
    
    # Устанавливаем диапазон и количество попыток в зависимости от выбранного уровня
    if difficulty == "легкий":
        range_min, range_max, max_attempts = 1, 50, 10
    elif difficulty == "средний":
        range_min, range_max, max_attempts = 1, 100, 8
    elif difficulty == "сложный":
        range_min, range_max, max_attempts = 1, 200, 6
    else:
        print("Неверный выбор, будем считать, что ты выбрал 'средний' уровень.")
        range_min, range_max, max_attempts = 1, 100, 8
    
    # Генерируем случайное число в указанном диапазоне
    number_to_guess = random.randint(range_min, range_max)
    attempts = 0

    print(f"Я загадал число от {range_min} до {range_max}. У тебя есть {max_attempts} попыток, чтобы угадать!")

    while attempts < max_attempts:
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
            print(f"Поздравляю! Ты угадал число {number_to_guess} за {attempts} попыток.")
            break
    else:
        print(f"Увы, ты не угадал число {number_to_guess} за {max_attempts} попыток.")

# Запуск игры
guess_number()
