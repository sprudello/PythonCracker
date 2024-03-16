# PythonCracker
 
This is a password cracker which utilises your NVIDIA GPU. 

Works on Visual Studio 2022 and Windows 10 Pro
Externally you have to install CUDA Toolkit
You have to insall numpy and pycuda, if there are any errors finding those packages or pycuda is doing weird stuff, try to fix it via system variables. (Has worked for me)

Here are some things if you haven't added them to your system variables, it eventually doesn't work

INCLUDE="C:\Program Files (x86)\Windows Kits\10\Include\10.0.10240.0\ucrt"
CUDA_PATH="C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4"
CUDA_PATH_V12_4="C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4"
PATH="C:\Program Files\Microsoft Visual Studio\2022\Enterprise\VC";"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\bin";"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\";"C:\Program Files\Microsoft Visual Studio\2022\Enterprise\VC\Tools\MSVC\14.39.33519\bin\Hostx64\x64"
