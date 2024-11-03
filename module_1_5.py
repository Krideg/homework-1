immutable_var = 1 , 2 , 3 , 4
print(type(immutable_var))
print (immutable_var)
#immutable_var[0] = ('One')
#print(immutable_var)
#нельзя изминить так как не подерживает обращение по элементам, но можно изменить если хранит списки
mutable_lis = [1 , 2 , 3 , 4]
print(mutable_lis)
mutable_lis[0] = ('One')
print(mutable_lis)