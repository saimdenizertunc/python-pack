# Given a signed 32-bit integer x, returns x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then returns 0.


def reverse(x: int):
    if (x < 0):
        b = str(x)
        if (int(b[1:][::-1]) > 2**31):
            return 0
        return (int(b[1:][::-1])*(-1))

    a = str(x)
    if (int(a[::-1]) > 2**31):
        return 0
    return int(a[::-1])
