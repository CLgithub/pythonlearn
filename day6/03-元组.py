#coding=utf-8
'''
元组
  元组与列表类似，不同之处在于元组不能被修改，元组的定义使用小括号()，列表使用中括号[]
  但可以从新定义
'''
tuple1=('a','bb',"cc",123)
print(tuple1)
#拆包
a,b,c,d=tuple1
print("a=%s b=%s c=%s d=%s"%(a,b,c,d))
