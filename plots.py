import tkinter as tk
from тренажёр import *
# Данные для вывода
texts = ["Первый вопрос: 2 + 2 = ?", "Второй вопрос: 5 * 3 = ?", "Третий вопрос: 10 - 4 = ?"]
current_index = 0


def handle_submit():
    global current_index
    # Получаем введённый текст
    user_answer = answer_entry.get()
    print(f"Ответ пользователя: {user_answer}")  # Для проверки (можно убрать)

    # Очищаем поле ввода
    answer_entry.delete(0, tk.END)

    # Переходим к следующему тексту (если есть)
    if current_index < len(texts) - 1:
        current_index += 1
        question_label.config(text=texts[current_index])
    else:
        question_label.config(text="Тренажёр завершён!")
        answer_entry.config(state=tk.DISABLED)  # Отключаем поле ввода
        submit_button.config(state=tk.DISABLED)  # Отключаем кнопку


# Создаём главное окно
window = tk.Tk()
window.title("Простое окно")  # Устанавливаем заголовок окна
window.geometry("800x600")  # Задаём размер окна (ширина x высота)

# Добавляем метку с текстом
question_label = tk.Label(window, text=texts[current_index], font=("Arial", 18))
question_label.pack(pady=20)

# Добавляем поле ввода
answer_entry = tk.Entry(window, font=("Arial", 16))
answer_entry.pack(pady=10)

# Добавляем кнопку
submit_button = tk.Button(window, text="Ответить", font=("Arial", 16), command=handle_submit)
submit_button.pack(pady=10)

# Запускаем главное окно
window.mainloop()
