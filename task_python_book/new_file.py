import time, random

time.sleep(1)

print("Надпись после паузы 5 сек")

i = 0
while i != 5:
    i += 1
    print(i)

digit = random.randint(1,60)
lists = [1, 2, 3, 4, 5, 6, 7, 8, digit]
random.shuffle(lists)
print(lists)

for num in range(5):
    print("Hello PyCharm!")