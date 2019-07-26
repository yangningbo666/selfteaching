while True:
    try:
        number_temp = input()
        number = int(number_temp)
        num_list = []
        for i in  range(number):
            num1 = input()
            num1 = num1.split('')
            num_temp1 = int(num1[0])
            num_temp2 = int(num1[1])
            num_list.append((num_temp1, num_temp2))
        num_list = sorted(num_list)
        num_list = num_list[::-1]
        boundry_list = []
        boundry_list.append(num_list[0])
        tmp = num_list[0][1]
        for i in range(1, len(num_list)):
            if num_list[i][1] > tmp:
                boundry_list.append(num_list[i])
                tmp = boundry_list[i][1]
        boundry_list=boundry_list[::-1]
        for i in range(len(boundry_list)):
            print(boundry_list[i][0],end="")
            print(boundry_list[i][1])
    except:
        break