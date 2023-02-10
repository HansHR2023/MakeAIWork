

# word3 = "Pinda1-Kaas2-3"
# for i in word3:
#     if i.isalpha():
#         word3.replace(i," " )
# print( 'x',word3,'x')


import re
word5 =  "Pinda1-Kaas2-3"
nwword = re.sub(r"[^0-9],' ', word5")
print(nwword)


[16:26] Ji Yoon Kim (1069519)
string = "happy 2023"new_str = re.sub(r"[^0-9]", " ", string)print(new_str)

