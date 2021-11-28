import time
from hashlib import md5
from random import choice
import concurrent.futures


total_workers = 100
start_time = time.time()
with concurrent.futures.ProcessPoolExecutor(max_workers=total_workers) as executor:
    while True:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("00000"):
            print(s, h)
            break
end_time = time.time()
print(end_time - start_time)
