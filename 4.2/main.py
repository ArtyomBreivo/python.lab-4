#Класс House
#1. Создайте класс House
#2. Создайте метод init ( и определите внутри него два динамических свойства: area и price.
#Свои начальные значения они получают из параметров метода init
#3. Создайте метод final price0, который принимает в качестве параметра размер скидки
#и возвращает цену с учетом данной скидки.

#Класс SmallHouse
#1. Создайте класс SmallHouse, унаследовав его функционал от класса House
#2. Внутри класса SmallHouse переопределите метод init_О так, чтобы он создавал объект
#с площадью 40м2

#Класс Human
#1. Реализуйте приватный метод ke_deal0, который будет отвечать за техническую реализацию
#покупки дома: уменьшать количество денег на счету и присваивать ссылку на только что
#купленный дом. В качестве аргументов данный метод принимает объект дома и его цену.
#2. Реализуйте метод buy house0, который будет проверять, что у человека достаточно денег
#для покупки, и совершать сделку. Если денег слишком мало - нужно вывести предупреждение в консоль.
#Параметры метода: ссылка на дом и размер скидки

class House:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    def final_price(self, discount):
        return self.price * (1 - discount / 100)

class SmallHouse(House):
    def __init__(self):
        House.__init__(self, area=40, price=100000)

class Human:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.house = None
    def no_deal(self, house, price):
        if self.money >= price:
            self.money -= price
            self.house = house
            print(f"{self.name} купил дом за {price} и теперь живет в {self.house.area} м2 доме.")
        else:
            print(f"{self.name}, у вас недостаточно денег для покупки дома.")

    def buy_house(self, house, discount):
        final_price = house.final_price(discount)
        self.no_deal(house, final_price)
if __name__ == "__main__":
  house1 = House(area=150, price=300000)
  small_house = SmallHouse()

  person1 = Human("Alice", 250000)
  person2 = Human("Bob", 80000)

  person1.buy_house(house1, discount=10)
  person2.buy_house(small_house, discount=5)




