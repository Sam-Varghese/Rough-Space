from itertools import combinations

number = list(input("Kindly enter the number: "))

counter = 1

answer = []

while counter < len(number)+1:
    comb = combinations(number, counter)
    for i in list(comb):
        num = "".join(i)

        answer.append(int(num))

    counter += 1

print(list(set(answer)))
