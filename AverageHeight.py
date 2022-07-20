heights = input("Enter a list of heights:").split()
total = 0
for i in range (0,len(heights)):
    total = total + int(heights[i])
num = len(heights)
average = total / num
print(f"The average height is: {average}")