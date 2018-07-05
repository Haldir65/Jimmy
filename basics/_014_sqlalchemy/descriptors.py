# -*- coding: UTF-8 -*-
class Meter(object):
    # """
    # 对于单位"米"的描述器
    # """
 
    def __init__(self, value=0.0):
        self.value = float(value)
 
    def __get__(self, instance, owner):
        return self.value
 
    def __set__(self, instance, value):
        self.value = float(value)
 
 
class Foot(object):
    # """
    # 对于单位"英尺"的描述器
    # """
 
    def __get__(self, instance, owner):
        return instance.meter * 3.2808
 
    def __set__(self, instance, value):
        instance.meter = float(value) / 3.2808
 
 
class Distance(object):
    # """
    # 用米和英寸来表示两个描述器之间的距离
    # """
    meter = Meter(10)
    foot = Foot()


class Example():
    def __init__(self):
        self.name = "example stuff"
    def prints(self,*args,**kwargs):
        print('stuffs')    

# def main():
#     # d = Distance()
#     # print(d.foot)
#     # print(d.meter)
#     ex = Example()
#     name_exists = hasattr(ex,"name")
#     print(" Example has attribute %s" %(hasattr(ex,"name"))
#     # print(" Example has attribute %s" %(hasattr(ex,"prints"))


def main():
    pass
    ex = Example()
    name_exists = hasattr(ex,"name")
    print(" Example has attribute %s" % hasattr(ex,"name"))
    print("Example has function %s" % hasattr(ex,"prints"))
    f = getattr(ex,"prints",None)
    f()
    f = getattr(ex,"non_existing",None)
    # # print(" Example has attribute %s" %(hasattr(ex,"prints"))

if __name__ == '__main__':
    main()