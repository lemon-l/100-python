# 读文本文件
'''
def main():
        f = None
        try:
            f = open('G:\\test.txt', 'r', encoding='utf-8')
            print(f.read())
        except FileNotFoundError:
            print('无法打开指定的文件!')
        except LookupError:
            print('指定了未知的编码!')
        except UnicodeDecodeError:
            print('读取文件时解码错误!')
        finally:
            if f:
                f.close()

if __name__ == '__main__':
    main()
'''

# 也可以用上下文语法，通过with关键字指定文件对象的上下文环境并在离开
# 上下文环境时释放文件资源
'''
def main():
    try:
        with open('G:\\test.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')


if __name__ == '__main__':
    main()
'''


# 几种读文件的不同方式
'''
import time


def main():
    # 一次性读取整个文件内容
    with open('G:\\test.txt', 'r') as f:
        print(f.read())

    # 通过for-in循环逐行读取
    with open('G:\\test.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
        print()

    # 读取文件按行读取到列表中
    with open('G:\\test.txt') as f:
        lines = f.readlines()
    print(lines)
    

if __name__ == '__main__':
    main()
'''