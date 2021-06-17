import numpy as np

# n = np.zeros(10)
# n[5] = 5
# print(n)

print('********')

arr = np.arange(0,50)
# arr = arr[1:20:2]
# arr = arr[::-1]
np.sort(arr)
print(arr)

print('********')

# print(type(arr))

new_arr = np.arange(9).reshape(3,3)
print(new_arr)
print(new_arr.shape)

print('********')

arr = np.random.random((4, 4))
print(arr)


print('********')

arr_min = arr.min()
arr_max = arr.max()
print("Minimum Value: ", arr_min)
print("Maximum Value: ", arr_max)
print("Mean Value: ", arr.mean())


print('********')

# multiply two matrix

a = np.array([[1, 0, 3],
              [0, 1, 5]])
b = np.array([[4, 1],
              [2, 2],
              [5, 6]])
x = np.matmul(a, b)
y = np.matmul(b, a)
# print(x.shape)
# print(y.shape)
print(a.shape)




