from sys import argv


script_name, fOneName, fTwoName = argv
with open(fOneName, 'r') as f1:
    circleInfo = f1.readlines()

x_0, y_0 = circleInfo[0].strip().split(' ')
circle_r = float(circleInfo[1].strip())

with open(fTwoName, 'r') as f2:
    pointInfo = f2.readlines()


def check_point(x, y):
    left_res = (float(x) - float(x_0))**2 + (float(y) - float(y_0))**2
    if left_res == circle_r**2:
        return 0
    elif left_res > circle_r**2:
        return 2
    elif left_res < circle_r**2:
        return 1


for point in pointInfo:
    x, y = point.strip().split(' ')
    point_pos = check_point(x, y)
    print(point_pos)
