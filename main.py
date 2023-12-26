import csv

student_data = [
    {"name": "Андрей", "surname": "Попов", "grade": 5, "project_id": "1"},
    {"name": "Степан", "surname": "Васильев", "grade": None, "project_id": "2"},
    {"name": "Владимир", "surname": "Хадаров", "grade": 4, "project_id": "3"},
    {"name": "Влад", "surname": "Хадаров", "grade": 2, "project_id": "4"},
    {"name": "Глеб", "surname": "Орлов", "grade": 1, "project_id": "5"},
    {"name": "Семен", "surname": "Архатов", "grade": 3, "project_id": "6"},
]

def calculate_average_grade(grades):
    """
    Вычисляем среднюю оценку из списка оценок

    Args:
    grades (list): Список оценок.

    Returns:
    float: Средняя оценка.
    """

    valid_grades = [grade for grade in grades if grade is not None]

    return round(sum(valid_grades)/len(valid_grades), 3) if valid_grades else 0 

def process_student_data(data):
    """
    Обрыбытывает данные студентов, заменяя отсутствующие оценки средним значением.

    Args:
    data (list of dict): Список словарей, каждый из которых содержит данные студента.

    Returns:
    list of dict: Обработаный список с даными студентов.
    """

    grades = [student["grade"] for student in data]

    average_grade = calculate_average_grade(grades)

    for student in data:
        if student["grade"] is None:
            student["grade"] = average_grade

    return data

def save_to_csv(data, filename):
    """
    Записываем данны в CSV формате в файл.

    Args:
    data (list of dict): Список словарей, каждый из которых содержит данные студента.
    filename (str): Имя файла для сохранения.
    """

    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def insertion_sort(array, key):
    """
    Алгоритм сортировки вставками.

    Args:
        array (list of dict): Список словарей, каждый из которых содержит данные студента.
        key (str): Ключ по которому будет идти сортировка.

    Returns:
        list of dict: Остортированный список словарей.
    """

    for i in range(1, len(array)):
        current_value = array[i]
        position = i

        while position > 0 and array[position - 1 ][key] > current_value[key]:
            array[position] =  array[position - 1]
            position -= 1
        
        array[position] = current_value
    
    return array[::-1]

def get_top_students(array, count = 3):
    """
    Получаем топ студентов по оценкам.

    Args:
        array (list of dict): Отсортированый список словарей по убыванию оценок, каждый из которых содержит данные студента.
        count (int): Кол-во студентов которые попадают в топ.

    Returns:
        list of dict: Список словарей с топ студентами.
    """

    return array[:count]

def read_csv(file_path):
    """
    Читаем данны из файла в CSV формате.

    Args:
        file_path (str): Путь к файлу.
    
    Returns:
        list of dict: Список словарей с топ студентами.
    """

    student_data = []

    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            student_data.append(row)
            
    return student_data
    
def main():
    # clear_data = process_student_data(student_data)
    
    student_data_from_csv = read_csv("student.csv")

    sort_student_data_from_csv = insertion_sort(student_data_from_csv, "grade")
    top_students = get_top_students(sort_student_data_from_csv)

    place = 1
    for student in top_students:
        print(f"{place} место: {student['name'][0]}. {student['surname']}")
        place += 1

    # save_to_csv(clear_data, "student.csv")

    # for student in clear_data:
    #     if student["name"] == "Владимир" and student["surname"] == "Хадаров":
    #         vladimir_grade = student["grade"]
    #         vladimit_project_id = student["project_id"]

    # print(f"Ты получил: {vladimir_grade}, за проект - {vladimit_project_id}")

main()






