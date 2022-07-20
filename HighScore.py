score = input("Enter scores:").split()
n = len(score)
high_score = 0
for i in range(0, n):
    if int(score[i]) > int(high_score):
        high_score = score[i]
print(high_score)
