# myNum = input() # takes input
# listOfNums = list(map(int, myNum)) # converts input to list
# countNum = listOfNums.count(4) # counts req chars
# print("Answer:", countNum) # outputs the nums of chars

inp = int(input())
count = 0
while inp:
    if inp % 10 == 4:
        count += 1
    inp = inp // 10 
print(count) 