# Простой калькулятор на Python

def show_menu():
    print("\n=== Калькулятор ===")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("5. Выход")

def get_numbers():
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        return num1, num2
    except ValueError:
        print("Пожалуйста, введите числовые значения.")
        return None, None

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Ошибка: деление на ноль!"
    return num1 / num2

def main():
    while True:
        show_menu()
        choice = input("Выберите операцию (1-5): ")

        if choice == "5":
            print("Программа завершена.")
            break

        if choice in ["1", "2", "3", "4"]:
            num1, num2 = get_numbers()
            if num1 is None or num2 is None:
                continue

            if choice == "1":
                result = add(num1, num2)
                print(f"Результат: {num1} + {num2} = {result}")
            elif choice == "2":
                result = subtract(num1, num2)
                print(f"Результат: {num1} - {num2} = {result}")
            elif choice == "3":
                result = multiply(num1, num2)
                print(f"Результат: {num1} * {num2} = {result}")
            elif choice == "4":
                result = divide(num1, num2)
                print(f"Результат: {num1} / {num2} = {result}")
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()