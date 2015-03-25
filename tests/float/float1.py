# basic float
x = 1 / 2
print(x)

# /= operator
a = 1
a /= 2
print(a)

print(1.0 // 2)
print(2.0 // 2)

try:
    1.0 / 0
except ZeroDivisionError:
    print("ZeroDivisionError")

try:
    1.0 // 0
except ZeroDivisionError:
    print("ZeroDivisionError")

# can't convert list to float
try:
    float([])
except TypeError:
    print("TypeError")

# test constant float with more than 255 chars
x = 1.84728699436059052516398251149631771898472869943605905251639825114963177189847286994360590525163982511496317718984728699436059052516398251149631771898472869943605905251639825114963177189847286994360590525163982511496317718984728699436059052516398251149631771898472869943605905251639825114963177189
print("%.5f" % x)
