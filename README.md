# Python-Work

## Why Python? 
Versatile, strong community, easy to learn?

## Primitive Data Types
Python assumes the type of a variable based on the assigned value.

*Example*:
For instance if you have a variable called 'amount' and assign amount = 10 Python infers that the variable amount is an int since it's assigned to a whole number. If you assign amount to a value such as 10.50 Python will infer that amount is a float since it's assigned a decimal value.

### Strings: 
A String stores text, create a String in Python with single quotes or double quotes.

*Example*:

name = 'Mikayla'
print(name) = Mikayla

However if a single quote is apart of the string you will want to use double quotes instead.

*Example*:

store_name = "Mikayla's store" not store_name='Mikayla's Store' this will cause an error because we are using single quotes within the string itself.

You can also concatenate strings by using the '+' operator for instance:
hello = "Hello"
name = "Mikayla"
greeting = hello + name 
print(greeting) = HelloMikayla.

## input() Function