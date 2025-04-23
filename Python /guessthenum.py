import random

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("\n=== Игра 'Угадай число' ===")
    print(f"Я загадал число от 1 до 100. У тебя {max_attempts} попыток на игру!")

    while attempts < max_attempts:
        try:
            guess = int(input("Введи свое число: "))
            attempts += 1

            if guess == secret_number:
                print(f"Поздравляю! Ты угадал число {secret_number} за {attempts} попыток!")
                return True
            elif guess < secret_number:
                print("Мое число больше. Попробуй еще!")
            else:
                print("Мое число меньше. Попробуй еще!")
        except ValueError:
            print("Пожалуйста, введи целое число.")

    print(f"\nИгра окончена! Ты исчерпал {max_attempts} попыток. Загаданное число было {secret_number}.")
    return False

def main():
    while True:
        play_game()
        play_again = input("\nХочешь сыграть еще раз? (да/нет): ").lower()
        if play_again != "да":
            print("Спасибо за игру! До свидания!")
            break

if __name__ == "__main__":
    main()