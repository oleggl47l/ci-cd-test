from calaculator import Calculator


def main():
    calc = Calculator()

    print("=== Мини-калькулятор ===")
    print("1. Сложение")
    print("2. Деление")
    print("3. Проверка простого числа")
    choice = input("Выберите действие (1/2/3): ")

    if choice == "1":
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        print(f"Результат: {calc.add(a, b)}")

    elif choice == "2":
        a = float(input("Введите делимое: "))
        b = float(input("Введите делитель: "))
        try:
            print(f"Результат: {calc.divide(a, b)}")
        except ZeroDivisionError as e:
            print(f"Ошибка: {e}")

    elif choice == "3":
        n = int(input("Введите число: "))
        if calc.is_prime_number(n):
            print(f"{n} — простое число ✅")
        else:
            print(f"{n} — НЕ простое число ❌")

    else:
        print("Неверный выбор!")

if __name__ == "__main__":
    main()
