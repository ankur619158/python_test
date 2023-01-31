def getWin(data):
    continuty = True
    count = 0
    result_count = 0
    index = 0
    for i in data:
        if continuty == False:
            if count >= result_count:
                result_count = count
            continuty = True
            count = 0
        if i == 'W':
            count = count +1
        else:
            continuty = False
    if count > result_count:
        return count
    else:
        return result_count

if __name__ == '__main__':
    # data = ['W', 'L' 'W','W','L','W','W','W', 'L', 'L', 'W', 'W', 'W']
    data = ['W','W','L','L','L','L', 'W', 'W','W','L','L','L']
    result = getWin(data)
    print("W"+str(result))