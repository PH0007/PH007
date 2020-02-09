import time
from ctypes import *


def main():
    result = cdll.LoadLibrary("-CDll3.so")
    result.main()


if __name__ == "__main__":
    main()
