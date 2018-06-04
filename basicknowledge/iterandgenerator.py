'''
遍历就是迭代
迭代器对象：是一个可以记住遍历的位置的对象
            从集合的第一个元素开始访问，直到所有的元素被访问完结束，只能往前不会后退
两个基本方法：iter()和next()
字符串、列表、元组对象都可用于创建迭代器，可用for语句或next()函数来遍历

'''

# 1、字符创创建迭代器对象
str1 = 'liangdianshui'
iter1 = iter ( str1 )

# 2、list对象创建迭代器
list1 = [1,2,3,4]
iter2 = iter ( list1 )

# 3、tuple(元祖) 对象创建迭代器
tuple1 = ( 1,2,3,4 )
iter3 = iter ( tuple1 )

# for 循环遍历迭代器对象
for x in iter1 :
    print ( x , end = ' ' )

print('\n------------------------')

# next() 函数遍历迭代器
while True :
    try :
        print ( next ( iter3 ) )
    except StopIteration :
        break



'''
生成器generator:一边循环一边计算的机制
使用了yield的函数被称为生成器
与普通函数不同的是：生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器
在调用生成器运行的过程中，每次遇到yield时函数会暂停并保存当前所有的运行信息，返回yield的值，并在
下一次执行next()方法时从当前位置继续运行

'''
#遍历生成器的元素 (一个列表生成式的 [] 改成 ())
gen= (x * x for x in range(10))
print(gen)

def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

# 引用函数
for x in fibon(1000000):
    print(x , end = ' ')


