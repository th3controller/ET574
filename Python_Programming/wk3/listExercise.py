# Michael Garcia, ET574
# List exercise

#a
print("Python")
print('')

#b
str = "python"
print(str)
print(str[0])
print(str[-1])
print(str[:])
print('')

#c
strNum = '0, 1, 2, 3, 4, 5, 6, 7, 8, 9'
print(strNum[1])
print(strNum[-3])
print('')

#d
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n)
print(n[0], n[1], n[9])
print(n[3:])
print(n[:5]) #range from beginning to index[5-1]
print(n[-5:-1])
print(len(n))
print(n[ :len(n)])
print('')

# e
print(strNum[1]+strNum[-3])
print(n[-3])
print(n[1] + n[-3])
print('')

# f
n[0] = 'apple'
n[9]='cherry'
n.insert(3, 'banana')
print(f"Do you like {n[0].upper()} or {n[3].upper()}?")
n.append(11)
n.append('orange')
print(n)
print('')

#g
old = n.pop(0)
print(f"My {old} is gone.")
print (n)
old = n.pop()
print(f"My {old} is gone.")
print (n)
print('')
del n[2]
print (n)
n.remove('cherry')
print (n)
