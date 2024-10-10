#import random
#num=random.randint(1,6)
#print(num)

import random
import time

how_many_numbers_you_need = 100
for i in range(how_many_numbers_you_need):
    num = random.randint(1, 6)
    print(num)
    time.sleep(2) #   #in seconds