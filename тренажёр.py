from random import randint
import time
import tkinter as tk
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np  # библиотека для классических массивов
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure



window = tk.Tk()
window.title("Тренажёер")
window.geometry("1280x720")


class Task:
    def __init__(self, name, problem, answer, difficult):
        self.name = name
        self.problem = problem
        self.answer = answer
        self.difficult = difficult

    def check(self, s_answer):
        if s_answer == self.answer:
            return True
        else:
            return False

    def challenge(self):
        # Контейнер для хранения результата
        self.result = None

        # Удаляем предыдущие элементы, если они есть
        for widget in window.winfo_children():
            widget.destroy()

        # Текст задачи
        text2 = Text(window, padx=0, pady=0, width=50, height=5, bg='grey', fg='black', wrap=WORD)
        text2.insert("1.0", self.problem)
        text2.config(state=DISABLED)  # Делаем текст только для чтения
        text2.pack(pady=10)

        # Поле ввода
        entry = Entry(window, width=20, font=('Arial', 14))
        entry.pack(pady=10)

        # Функция для обработки ответа
        def submit_answer():
            try:
                s_answer = int(entry.get())
                self.result = self.check(s_answer)  # Проверяем правильность ответа
                result_text = "Правильно!" if self.result else "Неправильно!"
            except ValueError:
                result_text = "Введите числовое значение!"

            # Отображение результата
            result_label.config(text=result_text)

            if self.result is not None:  # Закрываем интерфейс, если ответ дан
                window.quit()

        # Кнопка подтверждения
        submit_button = Button(window, text="Проверить ответ", command=submit_answer)
        submit_button.pack(pady=10)

        # Метка для результата
        result_label = Label(window, text="", font=('Arial', 14), fg='green')
        result_label.pack(pady=10)

        # Запускаем главный цикл окна
        window.mainloop()

        # Возвращаем результат после завершения ввода
        return self.result


class Prototype:
    def __init__(self, number, level):
        self.number = number
        self.tasks = []
        self.level = level

    def add_task(self, task):
        self.tasks.append(task)

    def give_tasks(self):
        success = []

        for i in range(0, 2):

            num_task = randint(0, len(self.tasks) - 1)
            while self.tasks[num_task].difficult > self.level:
                num_task = randint(0, len(self.tasks) - 1)
            success.append(int(self.tasks[num_task].challenge()))
        return sum(success) / 3


class User:
    def __init__(self):
        self.prototypes = []
        self.results = {'Таблица истинности': 0, 'Упрощение': 0, 'Доказательства': 0}
        self.day = -1
        self.history = []

    def introtest(self):
        current_res = []
        for prototype in self.prototypes:
            current_res.append(prototype.give_tasks())
        self.results['Таблица истинности'] = current_res[0]
        self.results['Упрощение'] = current_res[0]
        self.results['Доказательства'] = current_res[0]
        self.history.append(current_res)
        self.day += 1
        for i in range(len(self.prototypes)):
            self.prototypes[i].level += current_res[0]

    def day_test(self):
        current_res = []
        for prototype in self.prototypes:
            current_res.append(prototype.give_tasks())
        self.results['Таблица истинности'] = current_res[0]
        self.results['Упрощение'] = current_res[0]
        self.results['Доказательства'] = current_res[0]
        self.history.append(current_res)
        self.day += 1
        for i in range(len(self.prototypes)):
            self.prototypes[i].level += current_res[0]

    def full_work(self):
        # Удаляем предыдущие элементы, если они есть
        for widget in window.winfo_children():
            widget.destroy()

        # Приветственный текст
        text = Text(window, width=70, height=10, bg='grey', fg='black', wrap=WORD, font=('Arial', 14))
        text.insert(
            "1.0",
            "Здравствуйте! Это тренажёр по арифметике. Сейчас Вам будет предложено пройти вступительный тест, "
            "а затем 5 дней Вы будете получать задачи для тренировки."
        )
        text.config(state=DISABLED)  # Делаем текст только для чтения
        text.pack(pady=20)

        # Кнопка для начала вступительного теста
        def start_introtest():
            text.pack_forget()  # Убираем текст приветствия
            button.pack_forget()  # Убираем кнопку
            self.introtest()  # Выполняем вступительный тест

            # Текст после вступительного теста
            text_block = Text(window, width=70, height=10, bg='grey', fg='black', wrap=WORD, font=('Arial', 14))
            text_block.insert(
                "1.0",
                f"Вы прошли вступительный тест. Ваш уровень {self.prototypes[0].level}! "
                "Далее будет дневной тест. Приходите завтра."
            )
            # Отображение графика
            history_task1 = [self.history[i][0] for i in range(5)] if len(self.history) >= 5 else [0] * 5
            fig = Figure(figsize=(6, 4), dpi=100)
            ax = fig.add_subplot(111)
            ax.plot([1, 2, 3, 4, 5], history_task1, marker='o')
            ax.set_xlabel('Дни')
            ax.set_ylabel('Успешность')
            ax.set_title('Прогресс по теме "Таблица истинности"')

            canvas = FigureCanvasTkAgg(fig, master=window)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            text_block.config(state=DISABLED)  # Делаем текст только для чтения
            text_block.pack(pady=20)

            # Кнопка для начала дневных тестов
            def start_day_tests():
                text_block.pack_forget()  # Убираем текст вступительного теста
                start_button.pack_forget()  # Убираем кнопку
                for i in range(5):
                    self.day_test()
                    print(f"Прошёл день {self.day} из 5! Ваш уровень {self.prototypes[0].level} из 3")
                window.quit()  # Завершаем приложение

            # Кнопка для начала дневных тестов
            start_button = Button(window, text="Начать дневные тесты", command=start_day_tests)
            start_button.pack(pady=20)

        # Кнопка для начала вступительного теста
        button = Button(window, text="Начать вступительный тест", command=start_introtest)
        button.pack(pady=20)

        window.mainloop()


task1 = Task('задачка1', '2+3', 5, 0)
task2 = Task('задачка2', '10-4', 6, 0)
task3 = Task('задачка3', '5*4', 20, 1)
task4 = Task('задачка4', '6*8', 48, 1)
task5 = Task('задачка5', '125/5', 25, 2)
proto1 = Prototype(0, 0)
proto1.add_task(task1)
proto1.add_task(task2)
proto1.add_task(task3)
proto1.add_task(task4)
proto1.add_task(task5)
proto2 = Prototype(1, 0)
proto2.add_task(task1)
proto2.add_task(task2)
proto2.add_task(task3)
proto2.add_task(task4)
proto2.add_task(task5)
proto3 = Prototype(2, 0)
proto3.add_task(task1)
proto3.add_task(task2)
proto3.add_task(task3)
proto3.add_task(task4)
proto3.add_task(task5)

user = User()
user.prototypes = [proto1, proto2, proto3]
user.full_work()

dict = {0: 'Таблица истинности', 1: 'Упрощение', 2: 'Доказательства'}


def show_progress(n):
    history_task1 = [user.history[i][n] for i in range(5)]
    fig, ax = plt.subplots()  # Create a figure containing a single Axes.
    ax.bar(['день 1', 'день 2', 'день 3', 'день 4', 'день 5'], history_task1)  # Plot some data on the Axes.
    ax.set_xlabel('дни')
    ax.set_ylabel('успешность')
    ax.set_title(f'Прогресс по теме {dict[n]}')
    plt.show()  # Show the figure.


for i in range(3):
    show_progress(i)
