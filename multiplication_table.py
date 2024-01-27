# create a multiplication table from 1 to 10

# nested loop to generate multiplication table
table = [[i * j for j in range(1, 11)] for i in range(1, 11)]

# add a new line after each row to improve readability
for row in table:
    print(" ".join(map(str, row)))
