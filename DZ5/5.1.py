from winreg import DeleteValue
doc = input("Введите текст: ").split()
print(''.join(list(filter(lambda word: 'абв' not in word, doc))))