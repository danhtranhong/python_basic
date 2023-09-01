from math import pi
import datetime
x = 1234567890
y = pi
z = .723
today = datetime.datetime.now()

### Question 1 

s = "String Formatting"
left_aligned = "25 width left-aligned string output s"
right_aligned = "25 width right-aligned string output s"
question_mark = "?"


ruler = '-'*(len(s)+4)
print(f'\t\t{ruler}')
print(f'\t\t| {s} |')
print(f'\t\t{ruler}')
print(f'| {left_aligned} = {s}')
print(f'| {left_aligned} padded with ? s = {s}{question_mark*8}.')
print(f'| {right_aligned} = \t{s}')
print(f'| {right_aligned} padded with ? s = {question_mark*8}{s}.')

### Question 2

numb = "Number Formatting"
binary_numb = format(x,'b')
decimal_numb = "{:.10f}".format(y)
sc_format = "{:.5E}".format(y)
percetage = "{:.2%}".format(z)

ruler_2 = '-'*(len(numb)+4)
print(f'\t\t{ruler_2}')
print(f'\t\t| {numb} |')
print(f'\t\t{ruler_2}')
print(f'| Integer x with thousand separator x  =  {int(x):,}')
print(f'| Integer x in binanry  =  {binary_numb}')
print(f'| Floating-point with 10-decimal y  =  {decimal_numb}')
print(f'| Floating-point in scientific format y  =  {sc_format}')
print(f'| Floating-point as percentage z  =  {percetage} ')


## Question 3 
date_time = "Date & Time Formatting"
time_format = "HH-MM-SS"

a = today.strftime('%y-%m-%d')
b = today.strftime('%Y-%m-%d')
c = today.strftime('%a %d, %b %Y')
d = today.strftime('%H:%M:%S')
e = today.strftime('%Y-%m-%d %H:%M:%S')

ruler_3 = '-'*(len(date_time)+4)
print(f'\t\t{ruler_3}')
print(f'\t\t| {date_time} |')
print(f'\t\t{ruler_3}')
print(f'| Date in the format YY-MM-DD {a}')
print(f'| Date in the format YYYY-MM-DD {b}')
print(f'| Date in with the day & month name {c}')
print(f'| Time in the format {time_format} {d}')
print(f'| Date in the format YYYY-MM-DD {time_format} {e}')

