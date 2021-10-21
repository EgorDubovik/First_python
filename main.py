import numpy as nm

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def multiply(a, b):
    return nm.dot(a, b)


if __name__ == '__main__':
    print_hi('Yahor')
    b = nm.array([1, 2, 3])
    a = nm.array([
        [1, 2, 3],
        [4, 5, 2]
    ])
    c = multiply(a, b)
    print(c)


