a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] # izveido skaitļu sarakstu

num = int(input("Choose a number: ")) #liek izvēlēties skaitlio un to ievadīt

new_list = [] # izveido tukšu sarakstu

for i in a: # pārbauda katru elementu sarakstā a
    if i < num: #pārbauda vai elements ir mazāks par izvēlēto skaitli
        new_list.append(i) # izveido jaunu sarakstu kurā ir visi skaitļi kas ir mazāki par num

print(new_list) # izprintē no jauna izveidoto sarakstu