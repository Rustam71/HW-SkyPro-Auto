class Address:
    index = 'index'
    city = 'city-name'
    street = 'street-name'
    house_num = 'number of house'
    apart_num = 'number of apart'

    def __init__(self, index, city, street, house_num, apart_num):
        self.sayIndex = index
        self.sayCity = city
        self.sayStreet = street
        self.sayHouse_Num = house_num
        self.sayApart_Num = apart_num

    def __str__(self):
        return f'{self.sayIndex}, {self.sayCity}, {self.sayStreet}, {self.sayApart_Num} - {self.sayApart_Num}'
