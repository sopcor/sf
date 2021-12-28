znaki=[',','.','-','(',')','#',':',';','—','  ']
txt='Хотя он поначалу может быть\nи не очевиден, если вы не голландец ' +\
'(шутка про Guido van Rossum\n — одного из первых разработчиков Python)'
for znak in znaki: txt=txt.replace(znak,'') 
#for number in str(range(10)): txt=txt.replace(number,'')

txtlist=txt.split()
print("Общее количество слов = ",len(txtlist))

txt=txt.replace('\n',' ')
txtbezspace=txt.replace('\n','')
print('Общее количество букв = ',len(txtbezspace))


print(txt)