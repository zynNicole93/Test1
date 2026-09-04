i = 0
total = 0
m  = -1
while i != 'q':
     num = float(i)

     total = total + num

     i = input("请输入数字（每输入一个数字，按一下回车。完成所有输入后输入q结束输入）：")
     m += 1
if m == 0:
     print("无效输入。请在完成所有数字的输入后再输入q")



else:
  averagenum = total/m
  print("以上所有数字的平均数为："+ str(ave))


