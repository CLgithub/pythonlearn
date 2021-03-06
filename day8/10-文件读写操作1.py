#coding=utf-8
'''
1.打开文件 f=open('文件名','访问模式')
访问模式：
	r:以只读方式打开文件，文件的指针讲会放在文件的开头，这是默认模式
	w:以写入方式打开文件，如果该文件已经存在，则将其覆盖，如果该文件不存在，则创建新文件，相当于shell命令的>
	a:以追加写入方式打开文件，如果该文件已经存在，文件指针将会放在文件的结尾，也就是说，新的内容将会别写入已有内容之后，如果该文件不存在，则创建新文件，相当于shell命令的>>
	rb:以只读模式二进制格式打开文件，文件的指针将会放在文件的开头，这是默认模式
	wb:以写入方式二进制格式打开文件，如果该文件已经存在，则将其覆盖，如果该文件不存在，则创建新文件
	ab:以追加写入模式二进制格式打开文件，如果该文件已经存在，文件指针将会放在文件的结尾，也就是说，新的内容将会别写入已有内容之后，如果该文件不存在，则创建新文件
	r+:以读写方式打开文件，文件指针将会放在文件开头,文件必须存在
	w+
	a+
	rb+
	wb+
	ab+

2.关闭文件 f.close()

3.向文件中写如数据
f.writer("testData") 向文件f中写入testData数据
4.读取文件中的数据
f.read(x) 依次读取文件f中的x个字符并返回，操作指针指向下一个位置,如果没有写x则全读出来
5.另外两种读取文件的方式
	f.readline() 以行的方式读取文件内容并返回，指针向下一行移动
	f.readlines() 以行的方式读取文件内容并以列表形式返回
'''

file1=open('file1','w+')
file2=open('file1','w+')
file3=open('file1','w+')
file4=open('file1','r+')

c=file1.write("test\nabc\n123")
print("向文件file1中写入了%d个字符"%c)

file1.close()
#r=file2.read(2) #如果文件file1本身还在被其他地方打开，并且修改过没有关闭，是读不到内容的
for x in file2.read():
    print(x)

line=file3.readline()
print("读取一行%s"%line)
lines=file3.readlines()
print("读取所有行=%s"%lines)
#while 
file2.close()
file3.close()
file4.close()
