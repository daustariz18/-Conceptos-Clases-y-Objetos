def suma():
    # instrucciones de la funcion
    num1 = 5
    num2 = 7
    print(num1+num2)
    return  # (opcional)


def suma2(num1, num2):
    # instrucciones de la funcion
    resultado = num1+num2
    return resultado


almacena_resultado = suma2(3, 4)
suma()
suma2(3, 4)
print(almacena_resultado)


# listas

mylist = ['maria', 'pepe', 'marta', 'antonio']
mylist.append('Diego')
mylist.remove('maria')
mylist.extend(['edgar', 'ana', 'luis'])
mylist.reverse()
print(mylist)


# tuplas

mytuple = ('Diego', 'Edgar', 'Aylin', 'Lucia')
print(mytuple)
list = list(mytuple)
print(list)
tuple = tuple(list)
print(tuple)


# diccionario

mydict = {'Colombia': 'Bogota',
          'Argentina': 'Buenos Aires',
          'Brazil': 'Brasilia',
          'Peru': 'Lima',
          'Ecuador': 'Quito',
          'Chile': 'Santiago',
          'Paraguay': 'Asuncion',
          'Bolivia': 'La Paz',
          'Venezuela': 'Caracas',
          'Uruguay': 'Montevideo'
}
del mydict['Chile']
print(mydict)
