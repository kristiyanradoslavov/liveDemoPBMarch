from project.animal import Animal


class Lion(Animal):

    def __init__(self, name, gender, age, money_for_care=60):
        super().__init__(name, gender, age, money_for_care)
