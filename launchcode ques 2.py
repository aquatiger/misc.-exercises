def permutate(string1, string2):
    newstring1 = string1.split()
    newstring2 = string2.split()
    newerstring1 = newstring1.sort()
    newerstring2 = newstring2.sort()
    
    if newerstring1 != newerstring2:
        return False
    else:
        return True
    
    

permutate(string1, string2)
