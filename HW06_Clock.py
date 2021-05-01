from datetime import datetime
import time, os, random

def separator():
    count = 0
    r_with = '  \u2588\u2588   '
    r_without = '       '
    while True:
        sp = [r_with if i == count else r_without for i in range(7)]
        yield sp
        if count<6:
            count += 1
        else: 
            count = 0
gen_separ = separator()

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
    '9': (R1, R2, R2, R1, R8, R8, R1)
}

def form_displayed_time(str_t, dig_in_func, g_s, col_v):
    compiled_time = []
    for k in range(7):
        compiled_time.append(col_v)
        for i in str_t:
            if i.isdigit():
                compiled_time[k] += dig_in_func[i][k]
            else:
                compiled_time[k] += g_s[k]
        compiled_time[k] += '\033[0m'
    return compiled_time

def output_compiled_time(t):
    os.system('cls||clear')
    for k in range(7):
        print(t[k])
    print()

def main(color_list = ('\033[34m', '\033[31m', '\033[33m', '\033[32m', '\033[33m')):
    while True:
        sht = datetime.now().strftime('%X')
        colored = random.choice(color_list)
        cur_separ = next(gen_separ)
        fdt = form_displayed_time(sht, digits, cur_separ, colored)
        output_compiled_time(fdt)
        time.sleep(0.5)
main()