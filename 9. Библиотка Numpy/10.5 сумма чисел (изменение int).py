import numpy as np

x = np.int32(2147483548)
y = np.int32(2147471336)

print(f'сумма в int32: {x+y}')
print('')
print(f'сумма в int64: {np.int64(x)+np.int64(y)}')

