print('Давайте рассчитаем Ваш индекс массы тела.')
height = int(input("Введите Ваш рост в сантиметрах: "))
weight = int(input("Введите Ваш вес в килограммах: "))
gender = input("Введите Ваш пол в виде муж/жен: ")
gender = 'молодой человек' if gender == 'муж'  else "девушка"
bmi = int(weight/(height**2)*10000)
correct_place_ind = 16
if bmi < 19:
    delta = (19 - bmi) * height**2 / 10000
    correct_place_ind = 17
    recom = 'У Вас, ' + gender + ', недостаток веса. Рекомендуем набрать как мминимум ' + str(delta) + ' кг.'
elif bmi <= 25:
    recom = 'У Вас, ' + gender + ', все в порядке с весом.'
elif bmi < 30:
    delta = (bmi  - 25) * height**2 / 10000
    recom = 'У Вас, ' + gender + ', избыточный вес. Не мешало бы сбросить ' + str(delta) + ' кг.'
elif bmi < 35:
    delta = (bmi - 25) * height**2 / 10000
    recom = 'У Вас, ' + gender + ', ожирение 1-ой степени. До нормального веса Вам нужно сбросить ' + str(delta) + ' кг.'
elif bmi < 40:
    delta = (bmi - 25) * height**2 / 10000
    recom = 'У Вас, ' + gender + ', ожирение 2-ой степени. До нормального веса Вам нужно сбросить ' + str(delta) + ' кг.'
elif bmi >= 40:
    delta = (bmi-25) * height**2 / 10000
    recom = 'У Вас, ' + gender + ', ожирение 2-ой степени. До нормального веса Вам нужно сбросить ' + str(delta) + ' кг.'
print(f'Ваш индекс массы тела - {bmi}. {recom}')
ind = '===20=============================50'
scale = ind[:bmi - correct_place_ind] + '|' + ind[bmi - correct_place_ind + 1:]
print('\033[34m' + scale[:2] + '\033[32m' + scale[2:10] + '\033[33m' + scale[10:14] + '\033[31m' + scale[14:] + '\033[0m')
