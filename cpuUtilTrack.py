import pandas as pd
import psutil
import time

profileTime = int(input("How long to profile for? (ms):"))
cpuUtil = []

for i in range(0,profileTime):
    cpuUtil.append(psutil.cpu_percent(percpu=True))
    time.sleep(0.001)
    
for x in enumerate(cpuUtil):
    
    
print(cpuUtil)
'''
TODO: Frequency monitoring
'''