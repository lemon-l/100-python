'''
int (a,base = 2, 8, 10, 16) ----------表示将a转换为几进制
当传入的参数较多的时候就需要一个函数来简化
    def int2(a, base = 2| 8| 10| 16):
        return int(a, base)

----- int2('100004684')

****** functools.partial就是帮助我们创建一个偏函数，不用在自
------ 己定义int2，具体示例按如下所示
'''

import functools

int2 = functools.partial(int, base= 2)
print(int2('100000000'))