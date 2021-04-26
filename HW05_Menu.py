users_list = [
    ['Trump', 180, 110, 'm'],
    ['Abama', 186, 100, 'm'],
    ['Klinton', 178, 74, 'm']
]

def show_choos_menu():
    print("""\nMenu:    1. List    2. Create   3. Read    4. Update   5. Delete   6. Exit """)
    while True:
        choosing_item = input('Make your choice: ')
        if (len(choosing_item) != 0) and choosing_item.isdigit() and (7 > abs(int(choosing_item))) and (int(choosing_item) != 0):
            break
        print('Your choice is wrong. Try again.')
    return int(choosing_item)       

def list_user():
    print()
    print("User name\tHight (sm)\tWeight (kg)\tGender")
    print("-------------------------------------------------------")
    for i in users_list:
        for j in i:
            print(j, end='\t\t')
        print('')

def create_user():
    new_user = []
    ASKING = {
        0: 'Input User name: ',
        1: 'Input hight in sm: ',
        2: 'Input weight in kg: ',
        3: 'Input gender "m" or "f": '
    }
    for i in ASKING:
        curr_input = input(ASKING[i])
        if curr_input.isdigit():
            new_user.append(int(curr_input)) 
        else:
            new_user.append(curr_input) 
    users_list.append(new_user)

def read_user():
    nick_for_info = input('Input the user name for looking his detail information : ')
    print("User name\tHight (sm)\tWeight (kg)\tGender\t\tBMI\t Scale")
    for i in users_list:
        if nick_for_info == i[0]:
            for j in i:
                print(j, end='\t\t')
            bmi = count_bmi(i[1], i[2])
            delta = (bmi  - 25) * i[1]**2 / 10000
            break
    print(bmi, end='\t')
    print(indicate_bmi(bmi))
    if bmi < 19:
        delta = (19 - bmi) * i[1]**2 / 10000
        recom = 'У Вас недостаток веса. Рекомендуем набрать как мминимум ' + str(delta) + ' кг.'
    elif bmi <= 25:
        recom = 'У Вас все в порядке с весом.'
    elif bmi < 30:
        recom = 'У Вас избыточный вес. Не мешало бы сбросить ' + str(delta) + ' кг.'
    elif bmi < 35:
        recom = 'У Вас ожирение 1-ой степени. До нормального веса Вам нужно сбросить ' + str(delta) + ' кг.'
    elif bmi < 40:
        recom = 'У Вас ожирение 2-ой степени. До нормального веса Вам нужно сбросить ' + str(delta) + ' кг.'
    elif bmi >= 40:
        recom = 'У Вас ожирение 2-ой степени. До нормального веса Вам нужно сбросить ' + str(delta) + ' кг.'
    print(f'Ваш индекс массы тела - {bmi}. {recom}')

def update_user():
    user_for_update = input('Input an user name for update: ')
    k = int(0)
    while k <= len(users_list):
        if user_for_update == users_list[k][0]:
            users_list[k][0] = input('Input new user name : ')
            users_list[k][1] = input('Input new user height : ')
            users_list[k][2] = input('Input new user weight : ')
            break
        else:
            k = k + 1

def delete_user():
    user_for_delete = input('Input an user name for delete : ')
    i = int(0)
    while i <= len(users_list):
        if user_for_delete == users_list[i][0]:
            users_list.pop(i)
            break
        else:
            i += 1
    print(f'User {user_for_delete} has deleted.')

ACTIONS = {
    1: list_user,
    2: create_user,
    3: read_user,
    4: update_user,
    5: delete_user,
}

def select_action(ans):
    return ACTIONS.get(ans)

def count_bmi(height: int, weight: int):
    return int(weight/(height**2)*10000)

def indicate_bmi(bmi):
    correct_place_ind = 16
    if bmi < 19:
        correct_place_ind = 17
    ind = '===20=============================50'
    scale = ind[:bmi - correct_place_ind] + '|' + ind[bmi - correct_place_ind + 1:]
    return '\033[34m' + scale[:2] + '\033[32m' + scale[2:10] + '\033[33m' + scale[10:14] + '\033[31m' + scale[14:] + '\033[0m'

def main():
    while True:
        answer = show_choos_menu()
        if answer == 6:
            break
        action = select_action(answer)
        action()

main()

#import random
#a = random.choice('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_/\|')
#print(a)
