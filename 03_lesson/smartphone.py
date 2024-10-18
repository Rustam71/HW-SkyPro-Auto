class Smartphone:
    Phone_model = 'Model'
    Phone_Brand = 'Brand'
    Num = 'Number'

    def __init__(self, brand, model, number):
        self.sayBrand = brand
        self.sayModel = model
        self.sayNumber = number

    def SayBrand(self):
        print('Phone brand is', self.sayBrand)

    def SayModel(self):
        print('Phone model is', self.sayModel)

    def SayNumber(self):
        print('Number is ', self.sayNumber)

    def SayAll(self):
        print(self.sayBrand, '-', self.sayModel, '.', self.sayNumber)
