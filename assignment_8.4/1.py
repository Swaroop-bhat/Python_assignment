def positive(coordinates):
    if not coordinates:
        return []
    min_x = min(coordinates, key=lambda c: c[0])[0]
    min_y = min(coordinates, key=lambda c: c[1])[1]
    print(min_x)
    print(min_y)
    poscoordinates=[]
    for x, y in coordinates:
        x = x - min_x
        y = y - min_y
        poscoordinates.append((x, y))
    return poscoordinates

coordinates = [(1, -2), (-2, 4), (-1, -1), (-8, -3), (0, 4), (10, -3)]
res = positive(coordinates)
print(res)
