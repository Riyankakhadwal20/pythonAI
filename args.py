# Q.1: Using *args
def average_marks(*args):
    valid_marks = [mark for mark in args if mark >= 0]
    if len(valid_marks) == 0:
        return 0
    return sum(valid_marks)/len(valid_marks)
print(average_marks(75,80,0,90,0))

# Q.2: Using *kwargs
def filter_details(**kwargs):
    for key , value in kwargs.items():
        if isinstance(value,str):
            print(f"{key}={value}")
filter_details(name="Rahul" , age = 24 , city = "Chandigarh", height = 5.5, country ="India")