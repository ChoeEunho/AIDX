import time
import math                       #속도 테스트

star = time.time()
math.factorial(1000000)
end = time.time()

print(f"{end - start:.5f} sec")        