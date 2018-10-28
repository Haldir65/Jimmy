class TestClass(object):
  val1 = 100
   
  def __init__(self):
    self.val2 = 200
   
  def fcn(self,val = 400):
    val3 = 300
    self.val4 = val
    self.val5 = 500


def make_classes():
  inst1 = TestClass()
  inst2 = TestClass()

  print (TestClass.val1) # 100
  print (inst1.val1)   # 100

  inst1.val1 = 1000 
  print (inst1.val1)   # 1000
  print (TestClass.val1) # 100

  TestClass.val1 =2000
  print (inst1.val1)   # 1000
  print (TestClass.val1) # 2000

  print (inst2.val1)   # 2000   

  inst3 = TestClass() 
  print (inst3.val1)   # 2000   


if __name__ == '__main__':
  inst = TestClass()
  print(TestClass.val1)
  print(inst.val1)
  print(inst.val2)

  # print(inst.val3)
  ## AttributeError


  inst.fcn(800)
  print(inst.val4)  
  print(inst.val5)

  make_classes()

 

