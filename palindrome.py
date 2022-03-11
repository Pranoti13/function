def palindrome(p):
    revno=0
    n=p
    while (p != 0):
        rem = p % 10
        revno = revno * 10 + rem
        p = p / 10

    if (revno == n):
        print("num is palindrome")
    else:
        print("num is not palindrome")


a=eval(input("enter no:"))
palindrome(a)