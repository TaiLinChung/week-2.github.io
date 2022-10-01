# print("莊岱霖第二週python作業")


# print("要求一")

# def calculate(min, max, step):
# # 請用你的程式補完這個函式的區塊                              #時間複雜度
#     total=0                                                #賦予total變數值1 ，時間複雜度為1
#     for num in range(min,max+1,step):                      #迴圈內初始num為min會執行1次，時間複雜度為1，
#         # print(num)                                       #                           判定迴圈計數是否達到max+1，step增加動作，
#         total=total+num                                    #                           以及內部的total=total+num各會執行N次
#     print(total)                                           #print(total) 會執行1次，時間複雜度為1，  
                                                             #所以每呼叫一次函式複雜度為O(2+3N+1)=O(N)
# calculate(1, 3, 1) # 你的程式要能夠計算 1+2+3，最後印出 6
# calculate(4, 8, 2) # 你的程式要能夠計算 4+6+8，最後印出 18
# calculate(-1, 2, 2) # 你的程式要能夠計算 -1+1，最後印出 0






# print("要求二")

# def avg(data):
# # 請用你的程式補完這個函式的區塊                                      #時間複雜度
#     # print(data)
#     # print(data["employees"][0]["manager"])
#     # print(len(data["employees"]))   # 取得list內的資料長度
#     total=0                                                       #變數賦予值，時間複雜度=1
#     numFalse=0                                                    #變數賦予值，時間複雜度=1
#     for i in range(len(data["employees"])):                       #將i作為變數，輪巡len(data["employees"])，時間複雜度=n
#         # print(data["employees"][i]["manager"])
#         if data["employees"][i]["manager"]==False:                #每次進入迴圈都做判斷，時間複雜度=n
#             total=total+data["employees"][i]["salary"]            #每次進入迴圈都做加總，時間複雜度=n
#             numFalse=numFalse+1                                   #每次進入迴圈都做加總，時間複雜度=n
#     print(total/numFalse)                                         #跳出迴圈後print，時間複雜度=1
                                                                    #所以每呼叫一次函式複雜度為O(2+4N+1)=O(N)

# avg({
#     "employees":[

#     {

#         "name":"John",
#         "salary":30000,
#         "manager":False

#     },

#     {

#         "name":"Bob",
#         "salary":60000,
#         "manager":True

#     },

#     {

#         "name":"Jenny",
#         "salary":50000,
#         "manager":False

#     },

#     {

#         "name":"Tony",
#         "salary":40000,
#         "manager":False

#     }

#     ]
# }) # 呼叫 avg 函式







# print("要求三")           #動作原理                               #時間複雜度
# def func(a):              #Step1，定義函式func                    #每次呼叫就定義一次，時間複雜度=1
#     def func2(b,c):       #Step2，定義函式func2並將a值傳入等待      #每次呼叫就定義一次，時間複雜度=1
#         # print(a,b,c)
#         print(a+b*c)      #Step4，加總並print出來                  #時間複雜度=1
#     return func2          #Step3，回傳func2的位址到func讓其呼叫     #每次呼叫就會做一次，時間複雜度=1
                                                                    #所以每呼叫一次函式複雜度為O(4)=O(1)
# func(2)(3, 4) # 你補完的函式能印出 2+(3*4) 的結果 14
# func(5)(1, -5) # 你補完的函式能印出 5+(1*-5) 的結果 0
# func(-3)(2, 9) # 你補完的函式能印出 -3+(2*9) 的結果 15
# # 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果











# print("要求四")                               #時間複雜度
# def maxProduct(nums):                        #每次呼叫就定義一次，時間複雜度=1
# # 請用你的程式補完這個函式的區塊
#     max=nums[0]*nums[1]                      #每次呼叫就會做一次，時間複雜度=1
#     for i in range(len(nums)):               #定義變數i做輪巡，時間複雜度=1+2*N
#         # print(nums[i])
#         for j in range(i+1,len(nums),+1):    #在上個回圈內，定義變數j做輪巡，時間複雜度=N*(1+2*N)=N+2*N*N
#             # print(nums[j])
#             if nums[i]*nums[j]>=max:         #時間複雜度=1*N*N
#                 max=nums[i]*nums[j]          #時間複雜度=1*N*N
#     print(max)                                #所以每呼叫的時間複雜度O(2+1+2*N+N+4*N*N)=O(N*N)

# maxProduct([5, 20, 2, 6]) # 得到 120
# maxProduct([10, -20, 0, 3]) # 得到 30
# maxProduct([10, -20, 0, -3]) # 得到 60
# maxProduct([-1, 2]) # 得到 -2
# maxProduct([-1, 0, 2]) # 得到 0
# maxProduct([5,-1, -2, 0]) # 得到 2
# maxProduct([-5, -2]) # 得到 10





# print("要求五")                               #時間複雜度
# def twoSum(nums, target):                    #每次呼叫就定義一次，時間複雜度=1
#     # your code here
#     listans=[]                               #每次呼叫就定義一次，時間複雜度=1
#     for i in range(len(nums)):               #定義變數i做輪巡，時間複雜度=N
#         # print(nums[i])
#         for j in range(i+1,len(nums),+1):    #在回圈內做輪巡，時間複雜度=N*(1+2*N)=N+2*N*N
#             if nums[i]+nums[j]==target:      #時間複雜度=N*N
#                 listans.append(i)            #時間複雜度=N*N
#                 listans.append(j)            #時間複雜度=N*N

#     return listans                           #時間複雜度=1
# result=twoSum([2, 11, 7, 15], 9)             #所以每呼叫的時間複雜度O(2+N+N+5*N*N+1)=O(N*N)
# print(result) # show [0, 2] because nums[0]+nums[2] is 9






# print("要求六")                                   #時間複雜度
# def maxZeros(nums):                               #每次呼叫就定義一次，時間複雜度=1
# # 請用你的程式補完這個函式的區塊
#     lenmax=0                                      #每次呼叫就定義一次，時間複雜度=1
#     leninside=0                                   #每次呼叫就定義一次，時間複雜度=1
#     for elem in nums:                             #定義變數做輪巡，時間複雜度=N
#         if elem==0:                               #時間複雜度=N
#             leninside=leninside+1                 #時間複雜度=N
#             if leninside>lenmax:                  #時間複雜度=N
#                 lenmax=leninside                  #時間複雜度=N
#         else:
#             leninside=0                           #時間複雜度=N
#     print(lenmax)                                 #時間複雜度=1
# maxZeros([0, 1, 0, 0]) # 得到 2                   #所以每呼叫的時間複雜度O(3+6N+1)=O(N)
# maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
# maxZeros([1, 1, 1, 1, 1]) # 得到 0
# maxZeros([0, 0, 0, 1, 1]) # 得到 3
