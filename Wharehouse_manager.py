#! C:\Users\stefa\OneDrive\Desktop\Steve_Projects_Wharehouse_Software\myenv\Scripts\python.exes
# in PS usa il comando: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

from mymodules import * 
import maskpass


BC327 = BJT('BC327',0,0,'TO92','PNP','10mA',40,'contenitore A5')
BC337 = BJT('BC337',0,0,'TO92','NPN','10mA',40,'contenitore A5')

print(BC327.name)
print(BC327.quantity)
print(BC327.unitPrice)
print(BC327.package)
print(BC327.type)
print(BC327.Icmax)
print(BC327.location)

print('----------------------------------------------------------')
print('\t\tWhareouse software manager\n\t\tby Steve Projects')
print('----------------------------------------------------------')

#pwd=input('inserisci la password:\n')
pwd = maskpass.askpass()
DB=DataBase_SteveProjectWharehouse('localhost','GeneralKenobi',pwd,'SteveProjectsWharehouse')
#DB.find_by_name('BC327')