#hum ek calculator ka code likh rhe h ... 
def add(a,b):
    return a+b




def sub(a,b):return a-b

result1 = add(4,5)
result2 = sub(4,1)

print(result1, result2)

#now, iss code m koi problem nhi h ... run krke dekho ... 
#python app.py 
#result aa rhe h ... 

#problem yha p h ki ye code properly likha hua nhi h ... python code writing 
#ki guideline ko ye code violate kr rha h ... 
#abb hum ispe linting check lgayenge and usme pta lagg jayega ki kya kya problems h ... 
#hum without ci pipeline b bta skte h linting check ko ... 

#terminal -> pip install flake8
#terminal --> flake8 app.py
#flake 8 aapko bta dega ... 

#but hum ci pipeline k through krenge ... 
