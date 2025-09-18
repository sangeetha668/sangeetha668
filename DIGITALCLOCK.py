'''import time
import sys
h=3
m=56
s=0
while(True):
    sys.stdout.write(f"\r{h:02d} :{m:02d}:{s:02d}")
    sys.stdout.flush()
    time.sleep(1)
    s=s+1
    if(s==60):
        s=0

        m=m+1
    if(m==60):
        m=0
        s=0
i        h=h+1
    if(h==12):
        m=0
        s=0
        h=0'''
a ='A'
b=(chr(ord(a)+3)) 
print(str(ord(a))+str(ord (b)))                     
