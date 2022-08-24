p1 = "graviola"
p2 = "maracujá"
chainsaw = len(p1)
part1 = slice(0,len(p1)//2)
part2 = slice(len(p1)//2, len(p1))
p3 = p1[part1] + p2 + p1[part2]
print(p3)