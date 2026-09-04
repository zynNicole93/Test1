#无限项平均数求和，按q终止，不要报错，使用sum 函数
at = 0
numbers = []

while at != "q" :
    a = float(at)
    numbers.append(a)
    at = input("请输入数字：")

num = len(numbers) - 1
total = sum(numbers)
#test()
if num == 0 :
     print("完成全部输入后再填q")
else:

  ave = total /num
  res = str(ave)
  print(f"平均数为{res}")

num = len(numbers)
total = sum(numbers)