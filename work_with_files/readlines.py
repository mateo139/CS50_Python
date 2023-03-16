file = open("C:/Users/mlaska/Desktop/GitHub CS50/work_with_files/books.txt", "r")

lines = file.readlines()

for line in lines:
    print(line[0] + str(len(line)))


file.close()
