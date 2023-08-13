def asteroid_collision(asts):
    #Code Here
    left = asts[:1]
    right = asts[1:]
    return check_collision(left,right)
        
def check_collision(left,right):
    if len(right) == 0:
        return left
    if len(left) == 0:
        return check_collision([right[0]],right[1:])

    if left[-1] < 0:
        return left + check_collision([right[0]],right[1:])
    elif left[-1] > 0:
        if right[0] > 0:
            return check_collision(left + [right[0]],right[1:])
        if left[-1] > -right[0]:
            return check_collision(left,right[1:])
        elif left[-1] < -right[0]:
            return check_collision(left[:-1],right)
        else:
            return check_collision(left[:-1],right[1:])

x = input("Enter Input : ").split(",")
x = list(map(int,x))

print(asteroid_collision(x))