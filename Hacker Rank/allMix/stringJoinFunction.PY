# https://www.hackerrank.com/challenges/python-mutations/problem


# Add an Element in the middle in the string
# First Apporach
string = "abracadabra"
l = list(string)
l[5] = 'k'
string = ''.join(l)
print(string)
# abrackdabra

# Second Approach
string = string[:5] + "k" + string[6:]
print(string)
# abrackdabra

# str.isalnum()
# This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
# any([char.isalnum() for char in s])
# To check any of the charecter in the string

# str.isalpha()
# This method checks if all the characters of a string are alphabetical (a-z and A-Z).
# any([char.isalpha() for char in s])
# To check any of the charecter in the string

# str.isdigit()
# This method checks if all the characters of a string are digits (0-9).
# any([char.isdigit() for char in s])
# To check any of the charecter in the string

# str.islower()
# This method checks if all the characters of a string are lowercase characters (a-z).
# any([char.islower() for char in s])
# To check any of the charecter in the string

# str.isupper()
# This method checks if all the characters of a string are uppercase characters (A-Z).
# any([char.isupper() for char in s])
# To check any of the charecter in the string

# In Python, a string of text can be aligned left, right and center.

# .ljust(width)

# This method returns a left aligned string of length width.

# >>> width = 20
# >>> print 'HackerRank'.ljust(width,'-')
# HackerRank----------  
# .center(width)

# This method returns a centered string of length width.

# >>> width = 20
# >>> print 'HackerRank'.center(width,'-')
# -----HackerRank-----
# .rjust(width)

# This method returns a right aligned string of length width.

# >>> width = 20
# >>> print 'HackerRank'.rjust(width,'-')
# ----------HackerRank

# The Irritiating Problem
#     H    
#    HHH   
#   HHHHH  
#  HHHHHHH 
# HHHHHHHHH
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHHHHHHHHHHHHHHHHHHHHHH   
#   HHHHHHHHHHHHHHHHHHHHHHHHH   
#   HHHHHHHHHHHHHHHHHHHHHHHHH   
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#                     HHHHHHHHH 
#                      HHHHHHH  
#                       HHHHH   
#                        HHH    
#                         H 
#Replace all ______ with rjust, ljust or center. 

# TheCode

# thickness = int(input()) #This must be an odd number
# c = 'H'

# #Top Cone
# for i in range(thickness):
#     print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

# #Top Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# #Middle Belt
# for i in range((thickness+1)//2):
#     print((c*thickness*5).center(thickness*6))    

# #Bottom Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

# #Bottom Cone
# for i in range(thickness):
#     print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

# uPTOhERE

# Wrap Function of Max_WIDTH

# Notes TextWrap
# Functions provided by the Textwrap module :
# 1.
# textwrap.wrap(text, width=70, **kwargs): This function wraps the input paragraph such that each line in the paragraph is at most width characters long. The wrap method returns a list of output lines. The returned list is empty if the wrapped output has no content. Default width is taken as 70.
# import textwrap
  
# value = """This function wraps the input paragraph such that each line
# in the paragraph is at most width characters long. The wrap method
# returns a list of output lines. The returned list
# is empty if the wrapped
# output has no content."""
  
# # Wrap this text.
# wrapper = textwrap.TextWrapper(width=50)
  
# word_list = wrapper.wrap(text=value)
  
# # Print each line.
# for element in word_list:
#     print(element)

# 2.textwrap.fill(text, width=70, **kwargs): The fill() convenience function works similar to textwrap.wrap except it returns the data joined into a single, newline-separated string. This function wraps the input single paragraph in text, and returns a single string containing the wrapped paragraph.

# import textwrap
  
# value = """This function returns the answer as STRING and not LIST."""
  
# # Wrap this text.
# wrapper = textwrap.TextWrapper(width=50)
  
# string = wrapper.fill(text=value)
  
# print (string)

# 3.
# textwrap.dedent(text): This function is used to remove any common leading whitespace from every line in the input text. This allows to use docstrings or embedded multi-line strings line up with the left edge of the display, while removing the formatting of the code itself.

# import textwrap
  
# wrapper = textwrap.TextWrapper(width=50)
  
# s = '''\
#     hello
#       world
#     '''
# print(repr(s)) # prints '    hello\n      world\n    '
  
# text = textwrap.dedent(s)
# print(repr(text)) # prints 'hello\n  world\n'

# 4.textwrap.shorten(text, width, **kwargs): This function truncates the input string so that the length of the string becomes equal to the given width. At first, all the whitespaces are collapsed in the string by removing the whitespaces with a single space. If the modified string fits in the given string, then it is returned otherwise, the characters from the end are dropped so that the remaining words plus the placeholder fit within width.

# import textwrap
  
# sample_text = """This function wraps the input paragraph such that each line
# n the paragraph is at most width characters long. The wrap method
# returns a list of output lines. The returned list
# is empty if the wrapped
# output has no content."""
  
# wrapper = textwrap.TextWrapper(width=50)
  
# dedented_text = textwrap.dedent(text=sample_text)
# original = wrapper.fill(text=dedented_text)
  
# print('Original:\n')
# print(original)
  
# shortened = textwrap.shorten(text=original, width=100)
# shortened_wrapped = wrapper.fill(text=shortened)
  
# print('\nShortened:\n')
# print(shortened_wrapped)


# 5.textwrap.indent(text, prefix, predicate=None): This function is used to add the given prefix to the beginning of the selected lines of the text. The predicate argument can be used to control which lines are indented.

# import textwrap
  
# s = 'hello\n\n \nworld'
# s1 = textwrap.indent(text=s, prefix=' ')
  
# print (s1)
# print ("\n")
  
# s2 = textwrap.indent(text=s, prefix='+ ', predicate=lambda line: True)
# print (s2)

# Hackerrank Code
# import textwrap

# def wrap(string, max_width):
    # FIRST TYPE with text wrap
#     return textwrap.fill(string,max_width)
    # SECOND TYPE with join
#     return "\n".join([string[i:i+max_width] for i in range(0,len(string),max_width)])

# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)

