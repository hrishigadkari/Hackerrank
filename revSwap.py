def revswap(s):
    s = s.swapcase()
    words = s.split(' ')
    str = []
    for word in words:
        str.insert(0, word)
        
    
    print(" ". join(str))

print("Enter a string")
s = input() 
revswap(s)