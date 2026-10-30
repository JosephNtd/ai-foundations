import numpy as np

np.random.seed(42)
arr =  np.random.standard_normal((10000, 384))
print(arr[0].shape, arr[:, 0].shape)
print(arr.shape, arr.nbytes, arr.nbytes / 1000000)
arr_temp = arr.astype(np.float32)
print(arr_temp.nbytes / 1000000)

reshape_arr = arr[0].reshape(1, 384)
print(reshape_arr.shape)
