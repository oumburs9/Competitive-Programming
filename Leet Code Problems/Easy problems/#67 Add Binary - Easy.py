def sumTwoBin(str1, str2):
    res = []
    car = 0
    for i in str1:
        for j in str2:

            if (int(i) == 1 and int(j) == 1):
                    car = 1  
                    res.append(0)  
            elif ((int(i) == 0 and int(j) == 1) or (int(i) == 1 and int(j) == 0)):
                # c = 1
                if(car==1):
                    res.append(0)
                    car = 1
                    continue
                res.append(1)
            else:
                if(car==1):
                    res.append(1)
                    car = 0
                    continue
                res.append(0)

    print({str1, str2})
    return res


res = sumTwoBin('1101', '1011')
print(res)
