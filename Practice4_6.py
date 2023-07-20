import codecs
string = str(input("Введите строку латинскими символами"))
print(codecs.encode(string, "rot13"))
