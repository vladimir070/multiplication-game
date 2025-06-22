import random

# Создаем список вопросов и ответов
questions = []
for i in range(2, 10):
    for j in range(2, 10):
        question = f"{i} * {j} = ?"
        answer = str(i * j)
        questions.append((question, answer))

# Основной цикл игры
while True:
    # Выбираем случайный вопрос
    question, correct_answer = random.choice(questions)

    # Вывод вопроса
    print(question)

    # Получение ответа от пользователя
    user_answer = input("Ваш ответ (или 'q' для выхода): ")

    # Проверка выхода
    if user_answer.lower() == 'q':
        break

    # Проверка ответа
    if user_answer == correct_answer:
        print("Правильно!")
    else:
        print(f"Неправильно. Правильный ответ: {correct_answer}")

print("Игра окончена!")
