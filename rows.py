print("How many rows should i have?")
rows = int(input())
print("How many columns should i have?")
columns = int(input())

print("Here i go:")
for count in range(rows):
    for number in range(columns):
        print(":-)", end="  ")
    print("\n")

print("Done")
