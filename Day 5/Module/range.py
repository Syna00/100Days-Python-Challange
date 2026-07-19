#Range function with for loops :
#option 1
for n in range(1,11):
    print(n)
#option 2
for p in range(1,11,3):
    print(p)

#Gauss Theory option 1
total = 0
for number in range(1, 101, 1): 
    total += number
    # total = total + number
print(total)

#Gauss Theory option 2 (simplify)
print(sum(range(1, 101, 1)))

