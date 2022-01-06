# Реализовать программы кодирования и декодирования:
# 1)Методом Цезаря (ключ = порядковый номер студента по списку группы);
# 2)Полибианским квадратом (в начале пишется фамилия и имя студента);
# 3)Методом Вижинера (ключ = фамилия и имя студента).
# Otroshenko Tsisia 

def encryptionCaesar (str, key=1):
    result =''
    alpha = ' -.,abcdefghijklmnopqrstuvwxyz' # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    for c in str:
        result += alpha[(alpha.index(c) + key) % len(alpha)]
    print("Encription Caesar -", result)
    return result

def decryptionCaesar (str, key=1):
    result =''
    alpha = ' -.,abcdefghijklmnopqrstuvwxyz' # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    for c in str:
        result += alpha[(alpha.index(c) - key) % len(alpha)]
    print("Decription Caesar -", result)
    return result

def encryptionPolibia (str):
    result =[]
    alpha = ['otrshe', 'nkaibc', 'dfgjlm', 'pquvwx', 'yz -.,']
    for c in str:
        for i in range(len(alpha)):
            if c in alpha[i]:
                result.append([i,alpha[i].index(c)])
                break
    result = list(map(lambda x: chr(x[0]+48)+chr(x[1]+48), result))
    result = ''.join(result)
    print("Encription Polibia -", result)
    return result

def decryptionPolibia (str):
    result =''
    alpha = ['otrshe', 'nkaibc', 'dfgjlm', 'pquvwx', 'yz -.,']
    for i in range(0,len(str), 2):
        result+=alpha[int(str[i])][int(str[i+1])]
    print("Decription Polibia -", result)
    return result

def encriptionVigenere(str, key):
    result =''
    alpha = ' -.,abcdefghijklmnopqrstuvwxyz' # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    for i in range(len(str)):
        shift = ord(key[i%len(key)])-ord('a')
        result += alpha[(alpha.index(str[i]) + shift)% len(alpha)]
    print("Encription Vigenere -", result)
    return result

def decriptionVigenere(str, key):
    result =''
    alpha = ' -.,abcdefghijklmnopqrstuvwxyz' # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    for i in range(len(str)):
        shift = ord(key[i%len(key)])-ord('a')
        result += alpha[(alpha.index(str[i]) - shift)% len(alpha)]
    print("Encription Vigenere -", result)
    return result

# str = input("Input string: ")
str = 'ewerybody wants to be my enemy'
str = str.lower()
str = encryptionCaesar(str,24)
str = decryptionCaesar(str,24)
str = encryptionPolibia(str)
str = decryptionPolibia(str)
str = encriptionVigenere(str, 'otrshenkai')
str = decriptionVigenere(str, 'otrshenkai')