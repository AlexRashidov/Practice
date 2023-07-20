letters_keys = [] #Список букв(ключи)
bool_values = [] #Список bool значений для каждой буквы
string_of_letters = ""

for i in range(65, 90 + 1):        # Добавляем заглавные буквы в строку
    string_of_letters += chr(i)
for i in range(97,122 + 1):        # Добавляем строчные буквы в строку
    string_of_letters += chr(i)

for let in string_of_letters:
    letters_keys.append(let)  #Добавляем каждую букву в список ключей
    if let in "AEIOUYaeiouy": #Проверка на гласные буквы
        bool_values.append(True)
    else: bool_values.append(False)

dictionary = dict(zip(letters_keys, bool_values)) #Из двух списков формируем словарь
print(dictionary)