palabra = input("Digite la palabra: ")

dict = {}
for x in palabra:
   if x in dict:
    dict[x] = dict[x] + 1
   else:
          dict[x]=1
print (dict) 