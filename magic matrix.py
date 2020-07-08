magic = None


def check_magic(magic_arr, magic_order):
    global magic
    sum1 = sum(magic_arr[0])
    # print(magic_arr[0][1])
    # check for row sum euality(iteration over rows)
    for i in range(magic_order):
        sum_row = sum(magic_arr[i])
        if sum1 != sum_row:
            magic = False
            break
    else:
        magic = True

    #check for column sum equality (iteration over columns
    for j in range(magic_order):
        sum_list_col = []
        for i in range(magic_order):
            # print(magic_arr[i][j])
            sum_list_col.append(magic_arr[i][j])
        sum_col = sum(sum_list_col)
        if sum1 != sum_col:
            magic = False
            break
    else:
        magic = True


    # diagonal sum euality (principle diagonal)

    sum_list_col = []
    for i in range(magic_order):
        for j in range(magic_order):
            sum_list_col.append(magic_arr[i][j])


    if sum(sum_list_col) == sum1:
        magic = True
    else:
        magic = False

    #diagonal sum equality (opposite to principle diagonal)
    sum_list_col = []
    for i in range(magic_order):
        for j in range(magic_order):
            sum_list_col.append(magic_arr[magic_order-i-1][magic_order-j-1])

        if sum(sum_list_col) == sum1:
            magic = True
        else:
            magic = False



        if magic:
            print('magic')



num_rows = int(input("enter number of your magic matrix"))
nums_of_magic = []
for i in range(num_rows):
    nums = input('enter your {i + 1}th line')
    nums_of_magic.append([int(x) for x in nums.split()])

check_magic(nums_of_magic, num_rows)
