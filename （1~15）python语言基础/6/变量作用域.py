#查找变量的顺序：局部作用域-嵌套作用域-全局作用域-内置作用域
#global 知识函数变量来自与全局作用域，nonlocal指示来自于嵌套作用域

'''
def foo():
    b = 'hello'

    def bar():  # Python中可以在函数内部再定义函数
        c = True
        print(a)
        print(b)
        print(c)

    bar()
    # print(c)  # NameError: name 'c' is not defined


if __name__ == '__main__':
    a = 100
    # print(b)  # NameError: name 'b' is not defined
    foo()
'''

def foo():
    global a # 不加global关键字出来的结果是200 100
    a = 200
    print(a)  # 200


if __name__ == '__main__':
    a = 100
    foo()
    print(a)  # 100
