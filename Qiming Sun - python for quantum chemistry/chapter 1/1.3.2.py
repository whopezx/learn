# 这个文件需要重命名为以英文字母或下划线开头，否则不能通过pytest的测试
# 下面函数本来是有return 0的返回值，但是pytest还会有警告提示不需要这个return
# 看来pytest很严格地遵循python编程的要求。
def test_pytest():
    print('this is a test function')
    