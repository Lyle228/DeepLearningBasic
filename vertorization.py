import numpy as np
import time

size = 1000000

a = np.random.rand(size)
b = np.random.rand(size)

tic = time.time()
c = np.dot(a, b)
toc = time.time()

print("벡터화: " + str(1000*(toc-tic)) + "ms")

c = 0
tic = time.time()
for i in range(size):
    c += a[i] * b[i]
toc = time.time()

print("반복문: " + str(1000*(toc-tic)) + "ms")

# 사이즈 백만 기준으로 벡터곱은 평균 1ms
# 반복문을 이용한 곱은 평균 300ms로 큰 성능차이를 보임.