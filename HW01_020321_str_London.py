phrase = "Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. А у нас управдом — друг человека!"
lenth_phrase = len(phrase)
print("Длина выражения - " + str(lenth_phrase) + " симолов.\nФраза с заглавными буквами:")
b = phrase.title()
print(b + "\n")
print("Фраза срочными буквами \n" + phrase.lower())
print(f'Фраза содержит {phrase.count("нд")} - "нд",  {phrase.count("ам")} - "ам" и {phrase.count("о")} - "о"')
print("Доп. упражнения \n")
print( f"замена подстроки: Лондон на Воронеж \n {phrase.replace('Лондон', 'Воронеж')}" )
c = '***+London+***'
print(F"Использование  str.lstrip(*) : {c.lstrip('*')}")
print(F"Использование  str.rstrip(*) : {c.rstrip('*')}")
print(F"Использование str.strip(+*) : {c.strip('+*')}")