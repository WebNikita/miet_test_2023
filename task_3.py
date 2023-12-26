import csv


def find_student(file_path,project_id):
    """
    Функция для поиска студента который выполнял проект с определенным ID.
    В функции реализован линейный алгоритм поиска.

    Args:
        file_path (str): Имя файла для чтения.
        project_id (str): ID проекта.
    """

    flag = False
    
    try:
        with open(file_path, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["project_id"] == project_id:
                    flag = True
                    print(f"Проект № {project_id} делал: {row['name'][0]}.{row['surname']} он(а) получил(а) оценку - {row['grade']}")
        if not flag:
            print("Ничего не найдено.")    
    except FileNotFoundError:
        print("[ERROR] Файл не найден")

def main():
    """
    Главная функция. Функция обрабатывает ввод пользователя.
    """

    while True:
        user_input = input("Введите ID проекта или 'СТОП', для выхода: ")
        if user_input.lower() == "стоп":
            break
        elif not user_input.isdigit():
            print("Вы ввели строку, допускается только ввод числа, повторите попытку!")
        else:
            find_student("student.csv",user_input)

main()