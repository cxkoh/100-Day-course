height = float(input("height: "))
weight = int(input("weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3m")

bmi = weight/height ** 2
print(bmi)