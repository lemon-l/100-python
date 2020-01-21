'''
1. except语句不是必须的，finally语句也不是必须的，但是二者必须要有一个
   ，否则就没有try的意义了。
2. except语句可以有多个，Python会按except语句的顺序依次匹配你指定的异
   常，如果异常已经处理就不会再进入后面的except语句。
3. except语句可以以元组形式同时指定多个异常，参见实例代码。
4. except语句后面如果不指定异常类型，则默认捕获所有异常，你可以通过
   logging或者sys模块获取当前异常。
5. 如果要捕获异常后要重复抛出，请使用raise，后面不要带任何参数或信息。
6. 不建议捕获并抛出同一个异常，请考虑重构你的代码。
7. 不建议在不清楚逻辑的情况下捕获所有异常，有可能你隐藏了很严重的问题。
8. 尽量使用内置的异常处理语句来替换try/except语句，比如with语句，
   getattr()方法。

网址：https://segmentfault.com/a/1190000007736783
'''
def div(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Error: b should not be 0 !!")
    except Exception as e:
        print("Unexpected Error: {}".format(e))
    else:
        print('Run into else only when everything goes well')
    finally:
        print('Always run into finally block.')


# tests
div(2, 0)
div(2, 'bad type')
div(1, 2)

# Mutiple exception in one line
try:
    print(a / b)
except (ZeroDivisionError, TypeError) as e:      #医院组形势指定多个异常
    print(e)

# Except block is optional when there is finally
try:
    open(database)
finally:
    close(database)

# catch all errors and log it
try:
    do_work()
except:
    # get detail from logging module
    logging.exception('Exception caught!')

    # get detail from sys.exc_info() method
    error_type, error_value, trace_back = sys.exc_info()
    print(error_value)
    raise
