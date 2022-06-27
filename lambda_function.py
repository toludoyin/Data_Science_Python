
# anonymous fuunction
list(map(lambda number: number ** 8, range(5)))
list(filter(lambda x: x>8,range(15)))

stocks = ['Amazon', 'Netflix', 'Google', 'Facebook','Apple']
list(map(lambda x: x[0] == 'G' and x[-1] == 'e', stocks))

list(filter(lambda x: x[0] == 'A', stocks))