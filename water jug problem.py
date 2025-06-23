def water_jug():
    a, b = 0, 0
    max_a, max_b = 4, 3
    steps = []
    while a != 2 and b != 2:
        if a == 0:
            a = max_a
            steps.append((a, b))
        elif b == max_b:
            b = 0
            steps.append((a, b))
        else:
            pour = min(a, max_b - b)
            a -= pour
            b += pour
            steps.append((a, b))
    for i, (x, y) in enumerate(steps):
        print(f"Step {i+1}: Jug A = {x}, Jug B = {y}")
water_jug()