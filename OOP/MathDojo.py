class MathDojo(object):
    def __init__(self):
        self.result = 0

    def add(self, *args):
        for arg in args:
            if type(arg) is list or type(arg) is tuple:
                for x in arg:
                    self.result += x
            else:
                self.result += arg
        return self

    def subtract(self, *args):
        for arg in args:
            if type(arg) is list or type(arg) is tuple:
                for x in arg:
                    self.result -= x
            else:
                self.result -= arg
        return self

md = MathDojo()
print md.add(2).add(2,5).subtract(3,2).result
print(md.add([1], 3,4).add([3,5,7,8], (2,4.3,1.25)).subtract(2, [2,3], [1,1,2.3]).result)
