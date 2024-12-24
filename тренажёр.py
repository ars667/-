from random import randint


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
        print(self.problem)
        s_answer = int(input('Введите ответ:'))
        return self.check(s_answer)


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
        print(
            'Здравствуйте! Это тренажёр по арифметике. Сейчас Вам будет предложено пройти вступительный тест,'
            '\nа затем 5 дней Вы будете получать задачи для тренировки.')
        self.introtest()
        print(
            f'Вы прошли вступтительный тест. Ваш уровень {self.prototypes[0].level}! Далее будет дневной тест. Приходите завтра')
        for i in range(5):
            self.day_test()
            print(f"Прошёл день {self.day} из 5! Ваш уровень {self.prototypes[0].level} из 3")

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

dict = {0:'Таблица истинности', 1:'Упрощение', 2:'Доказательства'}
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





