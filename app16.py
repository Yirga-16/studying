# courses = ['History', 'Math', 'Physics', 'CompSci']
# courses.append('Art')
# courses.insert(0, 'Chemistry')
# courses2 = ['Education', 'Biology']
# courses.extend(courses2)
# courses.pop()
# nums = [1, 5, 2, 4, 3]
# num = sorted(nums)


# # for index, course in enumerate(courses, start=1):
# #     print(index, course)
# # course_str = ', '.join(courses)
# # new_list = course_str.split(' - ')
# # print(new_list)

# tuple1 = ('History', 'Math', 'Physics', 'CompSci')
# set1 = {'History', 'Math', 'Physics', 'CompSci'}
# art_courses = {'History', 'Art', 'Math', 'Design'}
# print(set1.intersection(art_courses))

# student = {'name': 'John', 'age': 25, 'courses': ['Math', 'ComSci']}
# student.update({'name': 'Yirga', 'age':36, 'courses': ['Power Electronics', 'Python', 'Physics']})

# for key, value in student.items():
#     print(key, value)


# language = 'Python'
# if language == 'Python':
#     print('The language is Python')
# elif language == 'JavaScript':
#     print('The Language is JavaScript')
# else:
#     print('Other Language')

# user = 'Admin'
# logged_in = False
# if user == 'Admin' and logged_in:
#     print('Admin page')
# else:
#     print('Bad Creds')
# nums = [1, 2, 3, 4, 5]
# for num in nums:
#     if num == 3:
#         print('Found!')
#         continue
#     print(num)
# for num in nums:
#     for letter in 'abc':
#         print(num, letter)
# for i in range(1, 10, 2): #start, end, step 
#     print(i)

# x = 0 
# while x < 11:
#     if x == 5:
#         continue
#     print(x)
#     x += 1 


# def hello_func(greeting, name):
#     return '{}!, {}'. format(greeting, name)

# message = hello_func('Hello', 'Yirga')
# print(message)

# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)

# student_info('info', 25, name='Yirga', age=36, Courses=['Physics', 'Electrical'])


# import my_module as mm 
# courses = ['History', 'Math', 'Physics', 'CompSci']
# index =(courses, 'Math')
# print(index)

# def func():
#     print("This is my first OOP")

# func()

# import sys 
# sys.path.append('Location.......') 

# import random 
# import math 
# import datetime
# import os
# courses = ['History', 'Math', 'Physics', 'CompSci']
# random_course = random.choice(courses)
# print(random_course)
# abs = math.cos(90)
# print(abs)
# today = datetime.date.today()
# print(today)

# print(os.getcwd())


# '''LEGB , Local, Enclosing, Global, Built-in'''
# x = 'global x'

# def test():
#     global x
#     #y = 'local y'
#     x = 'local x'
#     #print(y)
#     print(x)

# test()
# #print(x) # is working
# #print(y) # is not working 

# import builtins
# # print(dir(builtins))
# m = min([5, 1, 4, 2, 3])
# print(m)

# x = 'global x'
# def outer():
#     x = 'outer x'

#     def inner():
#         x = 'inner x'
#         print(x)
#     inner()
#     print(x)

# outer()

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# my_list = []
# for n in nums:
#     my_list.append(n)
# print(my_list)

# my_list = [n for n in nums]
# print(my_list)

# my_list = []
# for n in nums:
#     my_list.append(n*n)
# print(my_list)

# my_list = [n*n for n in nums]
# print(my_list)

# my_list = map(lambda n: n*n, nums)
# print(my_list)

# my_list = []
# for n in nums:
#     if n%2 == 0:
#         my_list.append(n)
# print(my_list)

# my_list = [n for n in nums if n%2 == 0]
# print(my_list)

# my_list = filter(lambda n: n%2 == 0, nums)
# print(my_list)

# my_list = []
# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((letter, num))
# print(my_list)

# my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
# print(my_list)

# names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
# heros = ['Batman', 'Superman', 'Spiderman', 'Walverine', 'Deadpool']
# print(zip(names, heros))
# my_dict = {}
# for name, hero in zip(names, heros):
#     my_dict[name] = hero
# print(my_dict)
# my_dict = {name: hero for name, hero in zip(names, heros)}
# print(my_dict)

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
# my_set = set()
# for n in nums:
#     my_set.add(n)
# print(my_set)

# my_set = {n for n in nums}
# print(my_set)


# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
# def gen_func(nums):
#     for n in nums:
#         yield n*n 

# my_gen = gen_func(nums)
# my_gen = (n*n for n in nums)

# for i in my_gen:
#     print(i)


# li = [9, 1, 8, 2, 7, 3, 6, 4, 5]
# s_li = sorted(li)

# print('Sorted Variable:\t', s_li)
# li.sort()
# print('Original Variable:\t', li)


# person = {'name': 'John', 'age': 23}
# sentence = 'My name is {} and I am {} years old.'.format(person['name'], person['age'])
# sentence = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)

# l = ['Yirga', 36]
# sentence = 'My name is {0[0]} and I am {0[1]} years old.'.format(l)

# tag = 'h1'
# text = 'This is a headline'
# sentence = '<{0}>{1} </{0}>'. format(tag, text)
# print(sentence) 


# import os 
# #os.chdir('/.../.../desktop') # to change diretcory 
# print(os.getcwd())

# import datetime
# tday = datetime.date.today()
# print(tday.isoweekday())
# tdelta = datetime.timedelta(hours=24)
# print(tday + tdelta)

# bday = datetime.date(2022, 8, 27)
# till_bday = bday - tday 
# print(till_bday.days)
# t = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
# print(t.microsecond)


#with open('test.txt', 'r') as f:
#f = open('test.txt', 'r')
# print(f.mode)
#print(f.read())

# with open('test.txt', 'r') as f:
#     f_contents = f.readlines()
#     print(f_contents, end='')



# import random

# greetings = ['Hello', 'Hi', 'Hey', 'Howdy', 'Hola']
# # value = random.random()
# # value = random.uniform(1, 10)
# # value = random.randint(1, 6)

# value = random.choice(greetings)
# print(value)

# import csv
# with open('name.csv', 'r')

# import re

# text_to_search = ''' juirgkle በላይ  98237509  ^$&^%(()& {}}  [[]  kklsdfngr @# '''

# pattern = re.compile(r'@')
# matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match)



# class Duck:
    
#     def quark(self):
#         print('Quark, quark')
    
#     def fly(self):
#         print('Flap, Flap!')


# class Person:
#     def quark(self):
#         print("I'm Quarking like a Duck!")
    
#     def fly(self):
#         print("I'm Flapping my Arms!")

# def quark_and_fly(thing):
#     thing.quark()
#     thing.fly()
#     print()

# d = Duck()
# quark_and_fly(d)


# class Employee:

#     def __init__(self, first, last, pay):
#         self.first = first 
#         self.last = last
#         self.pay = pay 
#         self.email = first + '.' + last + '@company.com'
#     def fullname(self):
#         print('{} {}'.format(self.first, self.last))

#     def apply_raise(self):
#         self.pay = int(self.pay * 1.04)

         

# emp_1 = Employee('Yirga', 'Belay', 60000)
# emp_2 = Employee('Hizkias', 'Yirga', 50000)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)
# # print(emp_1.email)
# # print(emp_2.email)
# # emp_1.fullname()
# # emp_2.fullname()

# import quandl as ql 
# import pandas as pd 
# import numpy as np 
# import keras 
# import tensorflow 




