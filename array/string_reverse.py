class Str_reverse:
    def __init__(self, data):
        self.strdata = data

    def strReverse(self):
        length = len(self.strdata)
        if( type(self.strdata) != str or length < 2 ):
            return self.strdata
        
        new_str=''
        for i in self.strdata:
            length -= 1
            new_str += self.strdata[length]
        return new_str

        

strRevObj = Str_reverse("hello world")


print(strRevObj.strReverse())