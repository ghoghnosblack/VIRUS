class Student:
  
    # Initializing class named Student
    def __init__(self):
        print('The class named Student was created.')
  
    # Calling destructor
    def __del__(self):
        print('The destructor is called. Student is deleted.')
  
sObj = Student() 
del sObj
class Student:
  
   # Initializing class named Student
    def __init__(self):
        print('The class named Student was created.')
  
    # Calling destructor
    def __del__(self):
        print('The destructor is called. Student is deleted.')
def Create_obj():
    print('*** Creating Object ***')
    s_Object = Student()
    print('***End of Function***')
    return s_Object
  
print('***Calling Create_obj()***')
myObj = Create_obj()
print('***Program Ends***')

import requests
url = 'https://rubika.ir/api/' 
data = {
    'message': 'https://hamyargps.com/blog/remote-rubika-hack'
    'massage2': 'https://www.techtarget.com/whatis/definition/dark-web'
    'massage3': 'https://tacklorix-report-fata.neocities.org'
    'massage4': 'https://tacklorix-report-fata.neocities.org'
    'massage5': 'https://www.hacker-pschorr.com/'
}
response = requests.post(url, json=data)
if response.status_code == 200:
    print("پیام با موفقیت ارسال شد.")
else:
    print("خطا در ارسال پیام:", response.status_code, response.text)