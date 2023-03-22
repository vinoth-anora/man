# def binarysearch(list, element, low, high):                                 # def a binarysearch as a function with arguments of list,element,low,high
#     while low<=high:                                                        #check the conditon
#         global mid                                                         #declare global variable mid
#         mid=(low+high)//2                                                   #calculate mid
#         if list[mid]==element:                                              #check the mid element equal to search element return mid
#          return mid
#         elif list[mid]<element:                                              #check if this conditon true
#             low=mid+1
#         elif list[mid]>element:                                               #or check this condition
#             high=mid-1
#     return -1                                                                  #else return -1
# list=[11,22,33,1,2,3,4,5,6,7,8,10]  #create a list
# for i in range(len(list)):
#     for j in range(i+1,len(list)):
#         if list[i]>list[j]:
#             list[i],list[j]=list[j],list[i]
# print(list)
#
#
# element=int(input("enter the element to search:"))                             #get the input to search
# result=binarysearch(list,element,0,len(list)-1)                                #pass the arguments to a function
# if result!=-1:                                                                 #check the result is not equal to -1
#     print("the index of the search  element is: ",result)                      #print the index of that number
# else:
#     print(list[mid], "is value", "and", "the closest index of the target:", mid)#otherwise take the mid-1 value of that search element as index




