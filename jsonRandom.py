import random, json

data_set =" "
f = open("PrincipiosDeSoftware.txt", "w+")
for j in range(500):
    d = random.randrange(0, 9)
    a = random.uniform(0, 100)

    data_set = "temperature: " + str(d) + ", "
    f.write(data_set)
    data_set = "temperature: " + str(a) + ", "
    print(data_set)
    f.write(data_set)
f.close()
