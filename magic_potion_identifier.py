def is_magical_potion(power):

    if power < 0: 
        return "NO"

    if power == 0: 
      return "NO"

    low = 1
    high = power

    while low <= high:
        mid = (low + high) // 2
        cube = mid * mid * mid

        if cube == power:
            return "YES"
        elif cube < power:
            low = mid + 1
        else:
            high = mid - 1

    return "NO"



power = 132651201231
result = is_magical_potion(power)
print(result)

