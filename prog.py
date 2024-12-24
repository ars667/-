import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Данные для графика
days = [1, 2, 3, 4, 5]
results = [3, 5, 7, 6, 8]

# Функция для отображения графика
def show_plot():
    # Создаём график с помощью Matplotlib
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.plot(days, results, marker='o', color='b', label="Результаты")
    ax.set_title("Результаты по дням")
    ax.set_xlabel("День")
    ax.set_ylabel("Результат")
    ax.legend()
    ax.grid()

    # Встраиваем график в окно tkinter
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=20)

# Создаём главное окно
window = tk.Tk()
window.title("Tkinter с графиком")
window.geometry("800x600")

# Кнопка для отображения графика
plot_button = tk.Button(window, text="Показать график", command=show_plot, font=("Arial", 16))
plot_button.pack(pady=20)

# Запуск приложения
window.mainloop()
