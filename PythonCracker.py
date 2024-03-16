      
import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule
import numpy as np

import sys
for path in sys.path:
    print (path)
   

# CUDA kernel to compare strings
cuda_code = """
__global__ void string_compare(char *str1, char *str2, bool *result)
{
    int idx = threadIdx.x + blockIdx.x * blockDim.x;
    result[idx] = (str1[idx] == str2[idx]);
}
"""

# Compile the CUDA code
mod = SourceModule(cuda_code)

# Get the kernel function
string_compare_kernel = mod.get_function("string_compare")

def compare_strings_on_gpu(str1, str2):
    str1 = np.array(list(str1), dtype=np.str)
    str2 = np.array(list(str2), dtype=np.str)
    result = np.zeros_like(str1, dtype=np.bool)

    # Allocate device memory
    str1_gpu = cuda.mem_alloc(str1.nbytes)
    str2_gpu = cuda.mem_alloc(str2.nbytes)
    result_gpu = cuda.mem_alloc(result.nbytes)

    # Copy data to device memory
    cuda.memcpy_htod(str1_gpu, str1)
    cuda.memcpy_htod(str2_gpu, str2)

    # Set up grid and block dimensions
    block_size = 256
    grid_size = (len(str1) + block_size - 1) // block_size

    # Execute the kernel
    string_compare_kernel(str1_gpu, str2_gpu, result_gpu, block=(block_size, 1, 1), grid=(grid_size, 1))

    # Copy the result back to the host
    cuda.memcpy_dtoh(result, result_gpu)

    # Check if all characters match
    return all(result)

# Example usage
user_password = "password123"
password = "password123"
result = compare_strings_on_gpu(user_password, password)
print(result)