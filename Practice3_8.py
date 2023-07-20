letters_keys = [] #Список букв(ключи)
values = [] #Список bool значений для каждой буквы
string_of_letters = ""

for i in range(65, 90 + 1):        # Добавляем заглавные буквы в строку
    string_of_letters += chr(i)

for let in string_of_letters:
    letters_keys.append(let)  #Добавляем каждую букву в список ключей
for num in range(1,26 + 1):
    values.append(num)

dictionary = dict(zip(letters_keys,values)) #Из двух списков формируем словарь
print(dictionary)