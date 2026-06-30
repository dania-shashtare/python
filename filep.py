# ===================read file===================
# f = open("dodo.txt")
# print(f.read())
# f.close() #i must use close() if wase not used with
# with open("dodo.txt") as f:
# print(f.read()) # print all file
# print(f.read(5))  # print dania
# print(f.readline()) # print firs line
# print(f.readline()) # print second line
# for x in f:
# print(x)
"""
dania shashtare 

computer engineer

NNU 
"""

# ===================write file===================
# with open("dodo.txt", "a") as f:#بكتب على نهاية الملف
#   f.write("grad year 2026")
# with open("dodo.txt") as f:
# print(f.read())
"""
print:
dania shashtare 
computer engineer
NNU 
grad year 2026
"""

# with open("dodo.txt", "w") as f:  # بكتب بدال يلي موجود بالملف
#   f.write("grad year 2026")
# with open("dodo.txt") as f:
#   print(f.read())
"""
print
grad year 2026
"""
# ===================creat new file===================
# f = open("dania.txt", "x")

# ===================remove file===================
# os.remove("dania.txt")
# Check if File exist
# import os
# if os.path.exists("dania.txt"):
# os.remove("dania.txt")
# else:
# print("The file does not exist")

# os.rmdir("myfolder") using delete folder
