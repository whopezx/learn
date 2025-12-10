import module_b


# def factory():
#     print('module_b running factory functiona')
#     return module_b.B()

class A:
    pass

def factory():
    return module_b.B()
