class House:
    def __init__(self, name, number_of_floor):
        self.new_floor = None
        self.name = name
        self.number_of_floor = int(number_of_floor)
    def go_to(self, new_floor):
        self.new_floor = int(new_floor)
        for i in range(1, new_floor):
            print(i)
        if new_floor > self.number_of_floor or new_floor < 1:
            print('-Такого этажа не существует-')
        else:
            print(f'Мы поедем на {new_floor} этаж')
H1 = House('ЖК Кирпичи', '23')
print(f'Название объекта недвижимости - {H1.name}, этажность здания - {H1.number_of_floor}')
H1.go_to(12)




