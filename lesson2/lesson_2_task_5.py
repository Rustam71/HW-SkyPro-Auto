month_to_season = int(input("Введите номер месяца: "))

if month_to_season < 3:
    print('Время года: Зима')
else:
    if 3 <= month_to_season < 6:
        print('Время года: Весна')
    else:
        if 6 <= month_to_season < 9:
            print('Время года: Лето')
        else:
            if 9 <= month_to_season < 12:
                print('Время года: Осень')
            else:
                if month_to_season == 12:
                    print('Время года: Зима')
                else:
                    if month_to_season > 12:
                        print("Такого месяца не существует!")
