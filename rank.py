def getRank(data):
    n = len(data)

    for i in range(n):
        for j in range(0, n-i-1):

            if data[j][1] < data[j+1][1]:
                data[j], data[j+1] = data[j+1], data[j]
            elif data[j][1] == data[j+1][1] and data[j][2] > data[j+1][2] :
                data[j] , data[j+1] = data[j+1] , data[j]
            else:
                continue
      
    return data

def printData(data):
    rank = 1
    score = 0
    time = 0
    for i in range(len(data)):
        if rank != 1 and score == data[i][1] and time == data[i][2] :
            data[i].insert(0 , rank-1)
        else:
            data[i].insert(0 , rank)
        score = data[i][2]
        time = data[i][3]
        data[i].pop()   
        rank += 1
    return data

if __name__ == '__main__':
    data = [['adam' , 120, 144],['Stephan' , 109, 101],['Brian' , 101, 121],['Ben' , 113, 87],
    ['laura' , 109, 119],['roger' , 109, 101],['Mike' , 98, 198],['lily' , 104, 107],
    ['shane' , 104, 107],['mark' , 107, 97]]
    data = getRank(data)
    result = printData(data)
    print(result)
