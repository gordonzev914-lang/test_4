
def caesar(text,scep):
    s=[]
    for i in text:
        num1=ord(i)
        num2=num1+scep
        if num2>=122:
            num3=num2-25
        else:
            num3=num2    
        s.append(chr(num3))
    string1="".join(s)
    return {"decrpted":string1.strip("'")}  

def basec1(test):
    return "hi from test"



def basec2(name):
    return f"hello {name}"



        

