import webbrowser
import time
start=raw_input("enter the time in H:M:S")
#use to get the present time tuple 
actual=time.strftime('%I:%M:%S')
url=raw_input("enter he sitename")
actual_url="https://www."+url+".com"
print actual
while(actual!=start):
    actual=time.strftime('%I:%M:%S')
if(actual==start):
    print 'okay lets start'
    webbrowser.open(actual_url)
    
    

