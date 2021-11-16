import memory_views
import numpy as np

narr = np.arange(27, dtype=np.dtype("i")).reshape((3, 3, 3))
print(narr)
print(memory_views.sum3d(narr))
