import sys
from cx_Freeze import setup, Executable

setup(
    name = "Hello Demo",
    version = "0.1",
    description = "A demo of using cx_Freeze",
    executables = [Executable("hello.py", base=None)])
