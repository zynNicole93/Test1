#计算平均数，数字总量上限为无限，输入q结束，不要报错
# def test():
#     print(str(total))
#     print(str(num))
#     print(str(at))
at = 0
total = 0
num = -1
while at != "q" :
    a = float(at)
    total = total + a
    at = input("请输入数字：")

    num += 1
#test()
if num == 0 :
     print("完成全部输入后再填q")
else:

  ave = total /num
  res = str(ave)
  print(f"""平均数为{res}""")
#finish! conguaduations!