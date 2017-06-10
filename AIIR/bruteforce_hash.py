# coding=utf8
#W tej chwili przygotowane jest o na samo sprawdzanie hashy bez rozproszenia obliczeń

#   Algorytm musi dostać 3 argumenty (w finalnej wersji będzie pięć)    
#       1: hash na podstawie którego mamy odgadnąć hasło    
#       2: zestaw znaków zawartych w szukanym haśle
#           Gdzie:
#               1 - wszystkie cyfry i litery (duże i małe)
#               2 - tylko cyfry
#               3 - tylko małe litery
#               4 - tylko duże litery
#               5 - duże i małe litery
#               6 - cyfry i małe litery
#               7 - cyfry i duże litery
#       3: maksymalna długość hasła
#
#
#   Przykładowe uruchomienie : python bruteforce_hash.py  06c030da77d4399528f1b6c3fbc0bc79 6 4


import sys
import hashlib

#Funkcja tworząca Hash
def MD5_hash( h_str ):
    md5h = hashlib.md5()
    md5h.update(h_str.encode('utf-8'))
    return md5h.hexdigest()

#Funkcja porównująca hash zadany w skrypcie z hashem konkretnego stringa
def Compare(str_1, Hash):
    if (MD5_hash(str_1) == Hash):
        print ('haslo %s' %str_1)
        return 1
    else :
        return 0

#wybranie słownika    
if (int(sys.argv[2]) == 1):
    dict_list = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
elif (int(sys.argv[2]) == 2):
    dict_list = '0123456789'
elif (int(sys.argv[2]) == 3):
    dict_list = 'abcdefghijklmnopqrstuvwxyz'
elif (int(sys.argv[2]) == 4):
    dict_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
elif (int(sys.argv[2]) == 5):
    dict_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
elif (int(sys.argv[2]) == 6):
    dict_list = '0123456789abcdefghijklmnopqrstuvwxyz'
elif (int(sys.argv[2]) == 7):
    dict_list = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
else :
    dict_list = ''


#zamiana zadanego hasha na małe litery (ponieważ funkcja MD5_hash generuje hashe z małymi literami)
hash_str = str(sys.argv[1]).lower()

for len in range(int(sys.argv[3])):
    list = itertools.product(dict_list, repeat=len+1)
    for item in list:
        item = ''.join(item)
        out = Compare(str(item), hash_str)
        if out:
            break
