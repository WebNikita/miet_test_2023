def main():
    while True:
        user_input = input("Введите ID проекта или 'СТОП', для выхода: ")
        if user_input.lower() == "стоп":
            break
        elif not user_input.isdigit():
            print("Вы ввели строку, допускается только ввод числа, повторите попытку!")

main()