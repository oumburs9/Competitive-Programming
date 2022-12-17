def robotRetun(str1):
    x=y=0
    for i in str1:
        if(i == 'U'):
            y +=1
        if(i == 'D'):
            y -=1
        if(i == 'R'):
            x +=1
        if(i == 'L'):
            x -=1
        
    return x ==0 and y == 0
res = robotRetun('UUDRLDRL')
print(res)
    