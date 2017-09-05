
""""""""""""""""""""""""""""""
''' Variable length Banner '''
''''''''''''''''''''''''''''''
Name = 'BANNER'
nameVar = []
lenName = len(Name) + 2


for x in range(0,lenName):
	nameVar.append('*')

print(''.join(nameVar))
print('*' + Name + '*')
print(''.join(nameVar))
