def remove(list):
    #index postions
    # 1 2 3 4 5 6 7 8 9
    # 0 1 2 3 4 5 6 7 8
    pos=2 # to remove
    index=0 # current
    length=len(list)
    # till at least one element is left
    while length>0:
        # 0 = (2+0)%9=2......1st iteration
        # 2 = (2+2)%8=4......2nd iteration
        # so on...
        index=(pos+index)%length
        # pop the element at inex postion
        print(list.pop(index))
        # decrease the size of length 
        length-=1
        
nums=[1,2,3,4,5,6,7,8,9]
remove(nums)