def f21(lis):
    if(lis[0]==1990):
        if(lis[2]==1995):
            return 12
        elif(lis[2]==2008):
            if(lis[4]=='sage'):
                return 11
            elif(lis[4]=='less'):
                return 10
            elif(lis[4]=='cobol'):
                if(lis[3]=='cobol'):
                    return 9
                elif(lis[3]=='sass'):
                    return 8
                elif(lis[3]=='meson'):
                    return 7
        elif(lis[2]==1967):
            return 6
    elif(lis[0]==1991):
        return 5
    elif(lis[0]==1983):
        if(lis[3]=='cobol'):
            return 4;
        elif(lis[3]=='sass'):
            return 3
        elif(lis[3]=='meson'):
            if(lis[2]==1995):
                return 2
            elif lis[2]==2008:
                return 1
            elif lis[2]==1967:
                return 0
print(f21([1990,1998,1995,'cobol','cobol']))
