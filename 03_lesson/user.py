class User:
    first_name = ('name')
    last_name = ('surname')

    def __init__(self, name, surname, namesur):
        self.username = name
        self.usersur = surname
        self.namesur = namesur

    def SayName(self):
        print("My name is", self.username)

    def SaySurname(self):
        print('My surname is', self.usersur)

    def SayNamesur(self):
        print('My name and surname is', self.namesur)


