import random

def play_game(min_number, max_number, attempts, starting_capital):
    capital = starting_capital

    print(f"Добро пожаловать в игру! Ваш начальный капитал: {capital} монет.")
    print(f"Попробуйте угадать число от {min_number} до {max_number}.")

    for attempt in range(attempts):
        if capital <= 0:
            print("У вас закончились деньги! Игра окончена.")
            break

        print(f"У вас {capital} монет.")


        while True:
            try:
                bet = int(input(f"Сделайте ставку (на сколько монет?): "))
                if bet <= 0:
                    print("Ставка должна быть положительным числом.")
                    continue
                if bet > capital:
                    print("Недостаточно монет для такой ставки.")
                    continue
                break
            except ValueError:
                print("Ошибка: Введите число!")

        random_number = random.randint(min_number, max_number)

        while True:
            try:
                guess = int(input(f"Угадайте число от {min_number} до {max_number}: "))
                break
            except ValueError:
                print("Ошибка: Введите целое число!")

        if guess == random_number:
            print(f"Поздравляю! Вы угадали число {random_number}.")
            capital += bet
        else:
            print(f"Увы, вы не угадали. Загаданное число было {random_number}.")
            capital -= bet

        if capital <= 0:
            print("У вас больше нет монет. Игра завершена.")
            break

    print(f"Конец игры! Ваш капитал: {capital} монет.")


print('сделал изменения на ветке hw_5')