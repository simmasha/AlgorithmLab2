def Enumeration(Points: list, Rectangles: list):
    counts = []
    for p in Points:
        count = 0
        for r in Rectangles:
            if (r.x1 <= p.x < r.x2) and (r.y1 <= p.y < r.y2): count += 1
        counts.append(count)
    print(*counts)


