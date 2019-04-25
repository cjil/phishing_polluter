list_items = [i for i in range(1,10000000)]
for i in list_items[0:100]:
    print(i)

generator_items = (i for i in range(1,10000000))
for i in range(1,100):
    print(next(generator_items))