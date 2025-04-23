tasks = []

def show_menu():
    print("\n=== To-Do List ===")
    print("1. Показать все задачи")
    print("2. Добавить задачу")
    print("3. Удалить задачу")
    print("4. Выход")

def show_tasks():
    if not tasks:
        print("Список задач пуст.")
    else:
        print("\nВаши задачи:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Введите новую задачу: ")
    tasks.append(task)
    print(f"Задача '{task}' добавлена.")

def remove_task():
    show_tasks()
    if tasks:
        try:
            index = int(input("Введите номер задачи для удаления: ")) - 1
            if 0 <= index < len(tasks):
                removed_task = tasks.pop(index)
                print(f"Задача '{removed_task}' удалена.")
            else:
                print("Неверный номер задачи.")
        except ValueError:
            print("Пожалуйста, введите число.")

def main():
    while True:
        show_menu()
        choice = input("Выберите действие (1-4): ")
        
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()