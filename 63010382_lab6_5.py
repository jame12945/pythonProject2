def asteroid_collision(asts):
    if len(asts) == 1:
        return asts

    results = asteroid_collision(asts[1:])

    if len(results) > 0 and asts[0] > 0 and results[0] < 0:


        if asts[0] == abs(results[0]):
            if len(results) > 1:
                return results[1:]
            elif len(results) == 1:
                return []

        elif asts[0] > abs(results[0]):
            return asteroid_collision([asts[0]] + results[1:])

        elif asts[0] < abs(results[0]):
            return results

    else:

        return [asts[0]] + results


x = input("Enter Input : ").split(",")
x = list(map(int, x))
print(asteroid_collision(x))
