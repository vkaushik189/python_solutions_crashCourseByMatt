friends = ['kaushik', 'ujwal', 'sohail']

#3.1
print(friends[0])
print(friends[1].title())
print(friends[-1])
print('------------------------------------')

#3.2
for friend in friends:
    print( friend + " is one of my friends.")
print('------------------------------------')

#3.3
vehicles = ['car', 'bike', 'tesla']
print('I would like to own a ' + vehicles[-1].title())
print('------------------------------------')

#3.4
invitees = ['musk', 'bezos', 'gates']
for invitee in invitees:
    print("Hey " + invitee + ", you're invited")
print('------------------------------------')

#3.5
print(invitees[-1] + " won't be making it")
invitees[-1] = 'tyson'
for invitee in invitees:
    print("Hey " + invitee + ", you're invited")
print('------------------------------------')

#3.6
print("Good news!, we have space for 3 more people")
invitees.insert(0, 'mark')
invitees.insert(int(len(invitees)/2), 'spiegel')
invitees.append("cook")
for invitee in invitees:
    print("Hey " + invitee + ", you're invited")
print('------------------------------------')

#3.7
print("sorry folks, we only have space for a total of 2 people")
print(invitees)
print(invitees.__len__())
if len(invitees) == 2:
    breakpoint();
else:
    for invitee in invitees:
        last_name = invitees.pop()
        print("You're not invited " + last_name)
print(invitees)
print(len(invitees) )

del invitees[2]
del invitees[1]
del invitees[0]
print(invitees)

#if invitees.__len__() > 4:
#   for invitee in invitees:
#        last_name = invitees.pop()
#        print("You're not invited " + last_name)

#3.8
places = ['la', 'ny', 'hawaii', 'mars', 'andromeda']
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
print(places.reverse())
print(places)
print(places.reverse())
print(places)
print(places.sort())
print(places)
print(places.sort(reverse=True))
print(places)

#3.9
print(len(places))
