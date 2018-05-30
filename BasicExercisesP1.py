import glob
import os
import socket
import subprocess
# import sys
# print("Python version")
# print(sys.version)

# import datetime
# print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# def area(radius):
#     return 3.14*radius**2
# print(area(1.1))

# def returnList(str):
#     return tuple(str.split(","))
# print(returnList("3,5,7,23"))

# def reserseName(firs, last):
#     return last + " " + firs
# print(reserseName("alex", "cme"))

# exam_st_date = (11,12,2014)
# print( "The examination will start from : %i / %i / %i"%exam_st_date)
# print("FF + {} {} {}".format(*exam_st_date))

# def compute(n):
#     print(n+int(str(n)+str(n))+int(str(n)+str(n)+str(n)))
# compute(5)

# def retDoc(func):
#     print(func.__doc__)
# retDoc("abs")

# import calendar
# calendar.prmonth(2018, 5)

# def printDif(n):
#     if n > 17:
#         print(2*(n-17))
#     else:
#         print(abs(n-17))
# printDif(22)
# printDif(14)

# def sum3(a,b,c):
#     if a ==b ==c:
#         print(sum([a,b,c])*3)
#     else:
#         print(sum([a,b,c]))
# sum3(1,2,3)
# sum3(2,2,2)

# def oddEven():
#     a = int(input("add: "))
#     if a%2 == 0:
#         print("even")
#     else:
#         print("odd")
# oddEven()

# def count4(myl):
#     return myl.count(4)
# print(count4([1,2,3,4,5,4]))

# def list_count_4(nums):
#     dd = {}
#     for i in nums:
#         count = 0
#         for num in nums:
#             if num == i:
#                 count = count + 1
#                 dd[num]=count
#     return dd
# print(list_count_4([1,1,2,3,2]))

# def retStr(n, mys):
#     if len(mys)<2:
#         print(n * mys)
#     else:
#         print(n*mys[:2])
# retStr(2, 'abcdef')
# retStr(3, 'p')

# def checkVowel(cha):
#     if cha in ["a", "e", "i", "o", "u"]:
#         print("vowel")
#     else:
#         print("nv")
# checkVowel("a")
# checkVowel("y")

# def histogram(myl, cha):
#     for i in myl:
#         print(i*cha)
# histogram([2,3,6,5], "@")

# def printEvenLess237(myl):
#     for i in myl:
#         if i==237:
#             print(i)
#             break
#         else:
#             if i%2==0:
#                 print(i)
# numbers = [
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958,743, 527
#     ]
# printEvenLess237(numbers)

# a = set(["White", "Black", "Red"])
# b = set(["Red", "Green"])
# print(a)
# print(b)
# print(a.difference(b))
#
# def areaTriangle(b, h):
#     print(b*h/2)
# areaTriangle(20, 40)

# def GreatestCommonDivisor(a,b):
#     if a>b:
#         min=b
#     else:
#         min=a
#     for i in range(min,0,-1):
#         # print(i)
#         if a%i==0 and b%i==0:
#             print(i)
#             break
# GreatestCommonDivisor(12, 17)
# GreatestCommonDivisor(4, 6)
# GreatestCommonDivisor(13, 26)

# def leastCommonMultiple(a,b):
#     maxi = max(a,b)
#     while True:
#         if maxi % a == 0 and maxi % b == 0:
#             print(maxi)
#             break
#         maxi+=1
# leastCommonMultiple(12, 17) #204
# leastCommonMultiple(4, 6) #12
# leastCommonMultiple(13, 26) #26

# def sum3(a,b,c):
#     sumi = a+b+c
#     if a == b or a ==c or b==c:
#         sumi=0
#     print(sumi)
# sum3(2,3,4)
# sum3(2,2,4)
# sum3(2,3,3)
# sum3(2,3,2)

# def add_numbers(a, b):
#     if not (isinstance(a, int) and isinstance(b, int)):
#          raise TypeError("Inputs must be integers")
#     return a + b
# print(add_numbers(10, 20))
# print(add_numbers('1', 20))

# def interest(amt, inte, y):
#     for i in range(y):
#         amt+=inte*amt/100
#     print(amt)
# interest(10000, 3.5, 7)

# import os.path
# open('abc.txt', 'w')
# print(os.path.isfile('abc.txt')) #Check whether a file exists using Python

# import struct
# print(struct.calcsize("P") * 8) # Check whether Python shell is executing in 32bit or 64bit mode on OS
# import platform
# import os
# print(os.name)
# print(platform.system())
# print(platform.release())

# import site
# print(site.getsitepackages()) #Locate Python site-packages

# from subprocess import call
# call(["ls", "-l"]) Linux call ext command

# import os
# print("Current File Name : ",os.path.realpath(__file__))

# import multiprocessing
# print(multiprocessing.cpu_count())

# for i in range(0, 10):
#     print('*', end="")#Print without newline or space
# print("\n")

# import cProfile
# def sum():
#     print(1+2)
# cProfile.run('sum()')

# import sys
# def eprint(*args, **kwargs):
#     print(*args, file=sys.stderr, **kwargs) # Print to stderr
# print("sampleNoError")
# eprint("abc", "efg", "xyz", sep="--")

# print(os.environ)
# print(os.environ['PATH'])

# import getpass
# print(getpass.getuser()) #Get the current username

# import socket #Find local IP addresses using Python's stdlib
# print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1],
#                    [[(s.connect(('8.8.8.8', 53)),s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET,socket.SOCK_DGRAM)]][0][1]]) if l][0][0])

# import time
# def sum_of_n_numbers(n):
#     start_time = time.time()
#     s = 0
#     for i in range(1,n+1):
#         s = s + i
#     end_time = time.time()
#     return s,end_time-start_time
# n = 5
# print("\nTime to sum of 1 to ",n," and required time to calculate is :",sum_of_n_numbers(n))

# def sumOfN(n):
#     print(n*(n+1)/2)
# sumOfN(5)

# def absolute_file_path(path_fname):
#     import os
#     return os.path.abspath(path_fname)

# import os.path, time
# print("Last modified: %s" % time.ctime(os.path.getmtime("temp.py")))
# print("Created: %s" % time.ctime(os.path.getctime("temp.py")))

# print("Your body mass index is: ", round(70 / (1.75 * 1.75), 2))

# files = glob.glob("*.txt")
# files.sort(key=os.path.getmtime)
# print("\n".join(files))

# import sys
# print("This is the name/path of the script:"),sys.argv[0]
# print("Number of arguments:",len(sys.argv))
# print("Argument List:",str(sys.argv))
# # The command executed in command prompt:
# # prashanta@server:~$ python test.py arg1 arg2 arg3

# import sys
# import textwrap
# module_name = ', '.join(sorted(sys.builtin_module_names))
# print(textwrap.fill(module_name, width=70))

# import logging
# import logging.handlers
# log = logging.getLogger(__name__)
# log.setLevel(logging.DEBUG)
# handler = logging.handlers.SysLogHandler(address = '/dev/log')
# formatter = logging.Formatter('%(module)s.%(funcName)s: %(message)s')
# handler.setFormatter(formatter)
# log.addHandler(handler)
# def hello():
#     log.debug('this is debug')
#     log.critical('this is critical')
# hello()

#TODO logging

# import sys
# str1 = "one"
# str2 = "four"
# str3 = "three"
# print()
# print("Memory size of '"+str1+"' = "+str(sys.getsizeof(str1))+ " bytes") #size of an object in bytes
# print("Memory size of '"+str2+"' = "+str(sys.getsizeof(str2))+ " bytes")
# print("Memory size of '"+str3+"' = "+str(sys.getsizeof(str3))+ " bytes")
# print()

# import sys
# print(sys.getrecursionlimit())

# def concStrings(*args):
#     cs = ""
#     for i in args:
#         cs+=i
#     print(cs)
# def concStrings2(*args):
#     return "".join(args)
# concStrings("aa","bb","dd","ss")
# print(concStrings2("aa","bb","dd","ss"))

# num = [2,3,4]
# for i in num:
#     if i > 1:
#         print('c')
#         continue
#     else:
#         print('b')
#         break

# def countStr2(st, n):
#     occ = 0
#     for i in st:
#         if i==n:
#             occ+=1
#     print(occ)
# countStr2("trymeme", "e")
# print("trymeme".count("e"))

# print(ord('A'))

# str = 'a123'
# # # str = '123'
# # try:
# #     i = float(str)
# # except (ValueError, TypeError):
# #     print('\nNot numeric')
# # print()

# import traceback
# def f1():return abc()
# def abc():traceback.print_stack()
# f1()

# import time
# print(time.ctime())

# host_name = socket.gethostname()
# print(host_name)
# import platform
# print(platform.uname())

# print(os.path.basename('/users/system1/student1/homework-1.py')) #Extract the filename from a given path

# print(os.path.splitext("test.txt"))

# # anonymous function
# from functools import reduce
#
# myl = [0,15,25,30]
# print([x for x in myl if x%15==0])
# div_15 = list(filter(lambda x: x %15==0, myl))
# print(div_15)
#
# items = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x**2, items))
# print(squared)
#
# product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
# print(product)

# import glob
# file_list = glob.glob('*.*') #Make file lists from current directory using a wildcard
# print(file_list)

# items = [1, 2, 3, 4, 5, -8, -1]
# poz_no = list(filter(lambda x: x > 0, items))
# print(poz_no)

# items = [1, 2, 3, 4, 5, -8, False]
# print(all(items))
# print(any(items))

# print('The total order amount comes to %.2f' % 212.374) #Display a floating number in specified numbers

# print('%.6s' % "1234567890") #Format a specified string to limit the number of characters to 6

# str1 = 'A8238i823acdeOUEI'
# print(any(c.islower() for c in str1))

# str1 = "122.22"
# print("Original String: ", str1)
# str1 = str1.rjust(8, '0')
# str1 = str1.ljust(10, '0')
# print(str1)


# from timeit import default_timer
# def timer(n):
#     start = default_timer()
#     # some code here
#     for row in range(0,n):
#         print(row)
#     print(default_timer() - start)
# timer(5)
# timer(15)

# inp = list(map(int, input().split())) #Input two integers in a single line
# print(inp)

# d = {'Red': 'Green'}
# print(d.items())
# (c1, c2), = d.items()
# print(c1)
# print(c2)

# import socket
# addr = '127.0.0.256'
# # addr = '192.168.98.1'
# try:
#     socket.inet_aton(addr) #Valid an IP address
#     print("Valid IP")
# except socket.error:
#     print("Invalid IP")

# print(bin(50))
# print(format(50, '08b'))
# print(format(50, '010b'))

# print(hex(30))
# print(format(30, '2x'))

# x = "d"
# if isinstance(x, int) or isinstance(x, str):
#     print("int or str")

# def sumCubeInt(n):
#     sum = 0
#     for i in range(1,n):
#         sum+=pow(i,3)
#     print(sum)
# sumCubeInt(4)
#
# def sumCubeInt2(n):
#     product = reduce((lambda x: x **3), range(n))
#     print(product)
# sumCubeInt(4)

# def distinctPairOfNumbersProductOdd(args): #Find a distinct pair of numbers whose product is odd from a sequence of integer values
#     for i in args:
#         for j in args:
#             if i != j:
#                 product = i * j
#                 # print(product)
#                 if product%2!=0:
#                     print("yes", i, j)
#                     break
# distinctPairOfNumbersProductOdd([2, 4, 6, 8])
# distinctPairOfNumbersProductOdd([2, 6, 1, 7, 8])