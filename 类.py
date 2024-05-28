class shape: 
    def __init__(self,name):
        self.name=name
    def Name(self):
        print("这是{}".format(self.name))
class long(shape):
    def __init__(self,name,a,b):
        shape.__init__(self,name)
        self.a=a
        self.b=b
    def Name(self):
        shape.Name(self)
        print("{}，面积为{}".format(self.name,self.a*self.b))
class v_long(shape):
    def __init__(self,name,a,b,c):
        shape.__init__(self,name)
        self.a=a
        self.b=b
        self.c=c
    def Name(self):
        shape.Name(self)
        print("{}，面积为{}".format(self.name,self.a*self.b*self.c))
p1=shape('长')
p1.Name()
s1=long("长方形",2,3)
s1.Name()
v1=v_long("长方体",1,2,6)
v1.Name()