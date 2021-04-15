var_1 = int(input("Введите первое число a: "))
var_2 = int(input("Введите второе число b: "))
var_3 = int(input("Введите третье число c: "))
res = var_1 and var_2 and var_3 and 'Нет нулевых значений.'
print(res)
res = var_1 or var_2 or var_3 or 'Введены все нули.' 
print(res)
if var_1 > (var_2 + var_3):
    print(f'разность суммы a - b - c = {var_1 - var_2 - var_3}')
elif var_1 < (var_2 + var_3):
    print(f'разность суммы  b + c - а = {var_2 + var_3 - var_1}')
if var_1 > 50 and (var_2 > var_1 or var_3 > var_1):
    print('Вася')
if var_1 > 5 and (var_2 == 7 and var_3 == 7):
    print('Петя')