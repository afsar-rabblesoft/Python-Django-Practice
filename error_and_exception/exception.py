# """Error can't be Handled
# eg of errors
# Syntax Error
# Out of Memory Error
# Recursion Error
# """
# # Even if the syntax of a statement or expression is correct, it may still cause an error when executed.
# # The programs usually do not handle exceptions, and result in error messages
# """Type Error str+int
# Zero Division Error 100/0
# Import Error
# """
# # Example of Zero Division Error 100/0
# try:
#     a = 100 / 0
#     print(a)
# except ZeroDivisionError:
#     print("Zero Division Exception Raised.")
# else:
#     print("Success, no error!")

# # Index Error
# try:
#     a = ["a", "b", "c"]
#     print(a[4])
# except LookupError:
#     print("Index Error Exception Raised, list index out of range")
# else:
#     print("Success, no error!")

# # Type error
# try:
#     a = 2
#     b = "Data"
#     c = a + b
# except TypeError:
#     print("Type error Occured Please enter int value")
# else:
#     print("No Type error found")


# Create a class inherit Exceptions class implement your own function
# class TestE:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#         self.c = 0

#     def add(self):
#         try:
#             self.c = self.a + self.b
#         except TypeError:
#             print("Type error Occured Please enter int value")
#         else:
#             print("No Type error found")

#     def divide(self):
#         try:
#             self.c = self.a / self.b
#         except:
#             print("Type Division error")
#         else:
#             print("No Division error")


# a = TestE(5, 0)
# a.divide()


try:
    a = input()
    b = input()
    c = int(a) + int(b)
    d = int(a) / int(b)
except ValueError:
    print("Both Value should be type int")
# except TypeError:
#     print("Type Error")
except ZeroDivisionError:
    print("Zero Division")
finally:
    print("No Error")
