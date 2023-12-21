def area(L,W):
    return float(L*W)

def perimeter(L,W):
    return float(L+W+L+W)

def volume(L,W,H):
    return float(L*W*H)

def surfaceArea(L,W,H):
    return float((L*W*2) + (L*H*2) + (W*H*2))

assert area(10, 10) == 100
assert area(0, 9999) == 0
assert area(5, 8) == 40
assert perimeter(10, 10) == 40
assert perimeter(0, 9999) == 19998
assert perimeter(5, 8) == 26
assert volume(10, 10, 10) == 1000
assert volume(9999, 0, 9999) == 0
assert volume(5, 8, 10) == 400
assert surfaceArea(10, 10, 10) == 600
assert surfaceArea(9999, 0, 9999) == 199960002
assert surfaceArea(5, 8, 10) == 340
