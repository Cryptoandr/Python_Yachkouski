from datetime import datetime
import time
import os

def get_time(): 
    cur_time = datetime.now()
    return cur_time.strftime('%X')

def separator():
    count = 0
    r_with = '  \u2588\u2588  '
    r_without = 'w    w'
    sp = ['=', '=', '=', '=', '=', '=', '=']
    while True:
        for i in range(7):
            if i == count:
                sp[i] = r_with
            else:
                sp[i] = r_without
        yield sp
        if count<6:
            count += 1
        else: 
            count = 0

gen_separ = separator()
color_var = '\033[31m'
# digts elements
R1 = '\u2588\u2588\u2588\u2588\u2588 '
R2 = '\u2588   \u2588 '
R3 = '\u2588\u2588\u2588   ' 
R4 = '  \u2588   '
R5 = '   \u2588  '
R6 = ' \u2588    '
R7 = '\u2588     '
R8 = '    \u2588 '
R9 = '      '

digits = {
    '0': (R1, R2, R2, R2, R2, R2, R1),
    '1': (R3, R4, R4, R4, R4, R4, R1),
    '2': (R1, R8, R8, R1, R7, R7, R1),
    '3': (R1, R8, R8, R1, R8, R8, R1),
    '4': (R2, R2, R2, R1, R8, R8, R8),
    '5': (R1, R7, R7, R1, R8, R8, R1),
    '6': (R1, R7, R7, R1, R2, R2, R1),
    '7': (R1, R8, R8, R5, R4, R6, R7),
    '8': (R1, R2, R2, R1, R2, R2, R1),
    '9': (R1, R2, R2, R1, R8, R8, R1),
    ':': next(gen_separ)
}

for i in digits.get(':'):
    print (i)

# for f in range(7):
#     rt = digits.get(':')
#     for i in rt:
#         print(i, end ='')
#     print()

# def form_displayed_time(str_t, dig, col_v):
#     compiled_time = []
#     dig[':'] = separator()
#     for k in range(7):
#         compiled_time.append(col_v)
#         for i in str_t:
#             compiled_time[k] += dig[i][k]
#         compiled_time[k] += '\033[0m'
#     return compiled_time

# def output_compiled_time(t):
#     os.system('cls||clear')
#     for k in range(7):
#         print(t[k])
#     print()

# def main():
#     while True:
#         sht = get_time()
#         fdt = form_displayed_time(sht, digits, color_var)
#         output_compiled_time(fdt)
#         time.sleep(1)
# main()