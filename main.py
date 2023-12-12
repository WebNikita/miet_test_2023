student_data = [
    {"name": "Андрей", "surname": "Попов", "grade": 5, "project_id": "1"},
    {"name": "Степан", "surname": "Васильев", "grade": None, "project_id": "2"},
    {"name": "Владимир", "surname": "Хадаров", "grade": 4, "project_id": "3"}
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

    grades = [student.get("grade") for student in data]

    average_grade = calculate_average_grade(grades)

    for student in data:
        if student["grade"] is None:
            student["grade"] = average_grade

    return data

def main():
    clear_data = process_student_data(student_data)
    print(clear_data)

main()






