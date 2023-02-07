for x in range(50):
    for y in range(50):
        for z in range(50):

            if x + 2 * y + 3 * z == 61 and x + y + 3 * z == 50 and z + y == 18:
                print(x + y + z + 2)