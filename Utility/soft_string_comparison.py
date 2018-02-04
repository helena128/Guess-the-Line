# Soft string comparison module

def SoftStringComparison(s1,s2):   
    return WhiteSpaceTrim(s1.lower(), s2.lower())

def WhiteSpaceTrim(s1, s2):
    return s1.strip()==s2.strip()
