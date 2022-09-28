for x in range(3):
        for y in range(3):
            for z in range(3):
                print(not (x or y or z) == (not x and not y and not z))
                print(x, y, z)