import re
#Функции
###################################################
def TaskSelection():
    print("Выберите номер задачи:\n"
          "1 - Проверка пароля.\n"
          "2 - Тип места в плацкартном вагоне.\n"
          "3 - Проверка високостности года.\n"
          "4 - Смешивание цветов.\n"
          "5 - Соединение слов в строку.")
    number = input()
    match number:
        case "1":
            PasswordVerification()
        case "2":
            TypeOfPlace()
        case "3":
            CheckingTheLeapYear()
        case "4":
            MixingColors()
        case "5":
            ConnectingWordsToAString()
        case _:
            print("Введен неправильный номер.")
            TaskSelection()

###################################################
def PasswordVerification():
    print('Введите пароль.')
    FirstPas = input()
    pattern = re.fullmatch(r"[A-Za-z0-9\-_\\/\%!\?=()\+]{8,}", FirstPas)
    if pattern == None:
        print('Пароль не принят! (Пароль либо слишком короткий или содержит запрещенные символы.)')
        PasswordVerification()
    print('Подтвердите пароль.')
    SecondPas = input()
    if FirstPas == SecondPas:
        print('Пароль принят.')
        exit()
    else:
        print('Пароль не принят! (Пароли не совпадают.)')
        PasswordVerification()

###################################################
def TypeOfPlace():
    Number = input('Введите номер вашего места в плацкарте: ')
    pattern = re.fullmatch(r"[0-9]{1,2}", Number)
    if pattern and int(Number) > 0 and int(Number) <= 54:
        Number = int(Number)
        if Number < 37 and Number % 2:
            print('Ваше место - в купе внизу.')
        elif Number < 37 and Number % 2 == 0:
            print('Ваше место - в купе наверху.')
        elif Number % 2:
            print('Ваше место - боковое внизу.')
        else:
            print('Ваше место - боковое наверху.')
    else:
        print('Введен неправильный номер!')
        TypeOfPlace()

###################################################
def CheckingTheLeapYear():
    Number = input('Введите год: ')
    pattern = re.fullmatch(r"[0-9]{1,4}", Number)
    if pattern:
        Number = int(Number)
        if ((Number % 4 == 0) and not (Number % 100 == 0)) or (Number % 400 == 0):
            print('Год', Number, ' - високосный.')
        else:
            print('Год', Number, ' - невисокосный.')
    else:
        print('Введен неправильный год!')
        CheckingTheLeapYear()

###################################################
def MixingColors():
    print('Введите первый цвет.')
    FirstColor = input()
    print('Введите второй цвет.')
    SecondColor = input()
    FColor = FirstColor.lower()
    SColor = SecondColor.lower()
    if (FColor == 'красный' and SColor == 'синий') or (FColor == 'синий' and SColor == 'красный'):
        print('При смешении красного и синего получится фиолетовый')
    elif (FColor == 'красный' and SColor == 'желтый') or (FColor == 'желтый' and SColor == 'красный'):
        print('При смешении красного и желтого получится оранжевый')
    elif (FColor == 'синий' and SColor == 'желтый') or (FColor == 'желтый' and SColor == 'синий'):
        print('При смешении синего и желтого получится зеленый')
    else:
        print('Введен неправильный цвет!')
        MixingColors()

###################################################
def ConnectingWordsToAString():
    print('Введите количество слов.')
    Number = input()
    pattern1 = re.fullmatch(r"[0-9]{1,}", Number)
    if pattern1:
        Number = int(Number)
    else:
        ConnectingWordsToAString()

    counter = 1
    str = ''
    while counter <= Number:
        print('Введите ', counter, ' слово.')
        Word = input()
        pattern2 = re.fullmatch(r"[A-Za-zА-Яа-яЁё\-]{1,}", Word)
        if pattern2:
            counter = counter + 1
            str = str + Word + ' '
    print(str.rstrip())
###################################################

#Основная программа
TaskSelection()







