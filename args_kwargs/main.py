# args
def add(*numbers):
    total=0
    totalValues=[]
    for number in numbers:
        total+=number
        totalValues.append(total)
    print(totalValues)


# add(10,20,30)

#kwargs
def student_infor(**kwargs):
    for key,values in kwargs.items():
        print(key,values)

# student_infor(name='lasantha',age=24,dept='IT')

def details(**infor):
    for keys,values in infor.items():
        print(keys,values)
        


details(name='lasantha',age=32)


