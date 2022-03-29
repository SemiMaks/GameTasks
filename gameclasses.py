class Game():
    def __init__(self, noOfQuestions=0):
        self.noOfQuestion = noOfQuestions
        print('Создание объекта noOfQuestion')

        @property
        def noOfQuestions(self):
            print('Getter method')
            return self._noOfQuestion

        @noOfQuestions.setter
        def noOfQuestions(self, value):
            if value < 1:
                self._noOfQuestion = 1
                print('Минимальное допустимое значение = 1')
                print('Количество вопросов приравнивается к 1')
            elif value > 10:
                self._noOfQuestions = 10
                print('Максимальное допустимое значение 10')
                print('Количество вопросов приравнивается к 10')
            else:
                self._noOfQuestion = value


class Mathagame:
    pass


class BinaryGame:
    pass
