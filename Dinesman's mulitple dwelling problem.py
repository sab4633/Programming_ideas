f = open("dines.txt", "r")
names = f.readline().split(", ")
print(names[4])
floors = len(names)
last = names[floors-1].split(" ")
names[floors-1] = last[1]
print(names)
print()
solution = [0,0,0,0,0]
not_first = []
not_second = []
not_third = []
not_fourth = []
not_fifth = []

not_fifth.append(names[0])
not_first.append(names[1])
not_fifth.append(names[2])
not_first.append(names[2])
not_first.append(names[3])
not_second.append(names[3])
not_third.append(names[4])
not_fifth.append(names[1])
not_third.append(names[2])
not_second.append(names[4])
not_fourth.append(names[4])
not_third.append(names[1])
not_fourth.append(names[0])
not_fourth.append(names[3])
not_second.append(names[0])
not_third.append(names[3])

solution[2] = names[0]
not_first.append(names[0])
solution[0] = names[4]
solution[4] = names[3]
solution[3] = names[2]
solution[1] = names[1]



count = []
print(not_fifth)
print(not_fourth)
print(not_third)
print(not_second)

print(not_first)
print()
print(solution)








#rint(f.readline())