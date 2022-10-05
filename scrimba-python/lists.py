friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]
            
print(friends)
""" print(friends[1])
print(friends[2:4])
print(len(friends))
print(friends.index('Eric'))
print(friends.count('Eric'))
friends.sort()
print(friends)
friends.reverse()
print(friends) 

print(sum(cars))
print(min(cars))

print(max(friends))  # letter T

friends.append('Francis')
print(friends)

friends.insert(1,'TerryG')
print(friends)
friends[1]='Joey'
print(friends) 

friends.extend(cars)
print(friends) """

friends.pop() # remove the last by default
print(friends)
friends.remove("Terry")
print(friends)
friends.pop(0)
print(friends)

""" clears list 
friends.clear()  """

""" del friends

Traceback (most recent call last): NameError: name 'friends' is not defined
!Error: Unknown error

del friends[2] -> prints ['John', 'Michael', 'Eric', 'Graham']

 """
new_friends = list(friends)
print(new_friends)


