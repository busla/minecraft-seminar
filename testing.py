from house import House

h1 = House('rauður', 2, 10, 25, 10)
h2 = House('blár', 5, 2, 50, 7)
h3 = House('grænn', 3, 100, 40, 4)
print(h1)
print(h2)
print(h3)


print(h1.paint('blár'))
print(h2.add_window(2))