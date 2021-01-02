class DayNames:
    def __init__(self,dataval=None, *args):
        # super(DayNames, self).__init__(*args))
        self.dataval=dataval
        self.nextval=None

e1=DayNames('Monday')
e2=DayNames('Tuesday')
e3=DayNames('Wednesday')

e1.nextval=e3
e3.nextval=e2

thisvalue=e1

while thisvalue:
    print(thisvalue.dataval)
    thisvalue=thisvalue.nextval

# print(e1.dataval)
# print(e2.dataval)
# print(e3.dataval)