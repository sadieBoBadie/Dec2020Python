def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
# y = a() # pause, go to line 1 execute function
# print(y)

# GLOBAL
#   var      val
#    y       a() -> 10

#  a() (called on line 9)
#   var      val
#    x        b() -> 5
#    returns   10

#  b() called on line 3
#   var       val
#  returns     5

# console
#  1
#  3
#  5
# 10


#6
def a(b,c):
    print(b+c)

#      None   +   None     
print(a(1,2) + a(2,3))

# var             val
#  a(1, 2)         ? ### undefined? 3?

# function call line 36 - a(1, 2)
# var      val
#   b       1
#   c       2

# func call line 36 - a(2, 3)
#   var         val
#    b          2
#    c          3


# console:
#  3
#  5
