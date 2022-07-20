row_1 = ["1", "2", "3"]
row_2 = ["4", "5", "6"]
row_3 = ["7", "8", "9"]
map = [row_1 , row_2 , row_3]
row = int(input("Enter row: \n"))
column = int(input("Enter column: \n"))
map[row-1][column-1] = "x"

print(f"{row_1}\n{row_2}\n{row_3}\n")