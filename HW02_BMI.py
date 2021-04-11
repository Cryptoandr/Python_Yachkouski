print('Давайте рассчитаем Ваш индекс массы тела.')
height = int(input("Введите Ваш рост в сантиметрах: "))
weight = int(input("Введите Ваш вес в килограммах: "))
bmi = int(weight/(height**2)*10000)
print(f'Ваш индекс массы тела {bmi}' )
indict = '20=============================50'
scale = indict[:bmi-19] + '|' + indict[bmi-18:]
print(scale)
