from random import randrange, randint, sample


def display(balls):
    """
    输出列表中的双色球号码
    """
    # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
    # 同时列出数据和数据下标，一般用在 for 循环当中。
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')

    '''
    #在格式化整数和浮点数时可以指定是否补0和整数与小数的位数。
    
    可以在"%"和字母之间插进数字表示最大场宽。 

　　%3d 表示输出3位整型数,不够3位右对齐。 

　　%9.2f 表示输出场宽为9的浮点数,其中小数位为2,整数位为6,小数点占一位,不够9位右对齐。
    （注意：小数点前的数字必须大于小数点后的数字。小数点前的数值规定了打印的数字的总宽度。
    如果忽略了（如：.2f），则意味着总宽度无限制。）

　　%8s 表示输出8个字符的字符串,不够8个字符右对齐。
    '''
    print('%02d' % ball, end=' ')
    print()


def random_select():
    """
    随机选择一组号码
    """
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    # sample函数用来实现从列表中选择不重复的n个元素
    selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls


def main():
    n = int(input('机选几注: '))
    for _ in range(n):
        display(random_select())


if __name__ == '__main__':
    main()
