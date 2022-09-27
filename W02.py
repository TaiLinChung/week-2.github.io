print("莊岱霖第二週python作業")


print("要求一")

def calculate(min, max, step):
# 請用你的程式補完這個函式的區塊
    total=0
    for num in range(min,max+1,step):
        # print(num)
        total=total+num
    print(total)

calculate(1, 3, 1) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8, 2) # 你的程式要能夠計算 4+6+8，最後印出 18
calculate(-1, 2, 2) # 你的程式要能夠計算 -1+1，最後印出 0






print("要求二")

def avg(data):
# 請用你的程式補完這個函式的區塊
    # print(data)
    # print(data["employees"][0]["manager"])
    # print(len(data["employees"]))   # 取得list內的資料長度
    total=0
    numFalse=0
    for i in range(len(data["employees"])):
        # print(data["employees"][i]["manager"])
        if data["employees"][i]["manager"]==False:
            total=total+data["employees"][i]["salary"]
            numFalse=numFalse+1
    print(total/numFalse)


avg({
    "employees":[

    {

        "name":"John",
        "salary":30000,
        "manager":False

    },

    {

        "name":"Bob",
        "salary":60000,
        "manager":True

    },

    {

        "name":"Jenny",
        "salary":50000,
        "manager":False

    },

    {

        "name":"Tony",
        "salary":40000,
        "manager":False

    }

    ]
}) # 呼叫 avg 函式







print("要求三")
def func(a):
    def func2(b,c):
        # print(a,b,c)
        print(a+b*c)
    return func2

func(2)(3, 4) # 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5) # 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9) # 你補完的函式能印出 -3+(2*9) 的結果 15
# 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果








print("要求四")
def maxProduct(nums):
# 請用你的程式補完這個函式的區塊
    max=nums[0]*nums[1]
    for i in range(len(nums)):
        # print(nums[i])
        for j in range(i+1,len(nums),+1):
            # print(nums[j])
            if nums[i]*nums[j]>=max:
                max=nums[i]*nums[j]
    print(max)

maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([10, -20, 0, -3]) # 得到 60
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([5,-1, -2, 0]) # 得到 2
maxProduct([-5, -2]) # 得到 10





print("要求五")
def twoSum(nums, target):
    # your code here
    listans=[]
    for i in range(len(nums)):
        # print(nums[i])
        for j in range(i+1,len(nums),+1):
            if nums[i]+nums[j]==target:
                listans.append(i)
                listans.append(j)

    return listans
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9






print("要求六")
def maxZeros(nums):
# 請用你的程式補完這個函式的區塊
    lenmax=0
    leninside=0
    for elem in nums:
        if elem==0:
            leninside=leninside+1
            if leninside>lenmax:
                lenmax=leninside
        else:
            leninside=0
    print(lenmax)
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3