my_dict = {'Dima': 2001, 'Vika': 1999, 'Vova': 1989}
print(my_dict)
print(my_dict['Vika'])
my_dict['Vika'] = 2002
print(my_dict)
my_dict['Katya'] = 2002
print(my_dict)
print(my_dict.get('Ira'))
my_dict.update({'Gosha': 2007, 'Pasha': 2015})
print(my_dict)
del my_dict['Vova']
print(my_dict)

my_set = {1, 2, 3, 'a', 'b', 2, 3, 4, 5, 'String', True, ('b', 'c')}
print(my_set)
my_set.update(("cello", "violin"))
print(my_set)
print(my_set.discard(2))
print(my_set)