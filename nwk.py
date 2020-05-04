import os
import time
l = len(os.listdir(R'E:\temp\week8'))
while len(os.listdir(R'E:\temp\week8')) >= l:
    print(l)
    time.sleep(3)
os.system(r'shutdown /s /t 30')