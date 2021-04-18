def login_decor(inp_function):
    def check_login():
        login = input('Ты кто? ')
        if login == "Админ" or login == "Admin":
            print('Допуск есть')
            inp_function()
        else:
            print('Нет доступа')
    return check_login
@login_decor
def count(sum = 1000):
    print(f'На счете находится {sum} единиц')
count()
