
enter_string="Pinda1-Kaas2-3"

for i in  range(len(enter_string)):
    if enter_string.isalpha():
        enter_string = enter_string.replace(enter_string, " ")
        print("(k)",enter_string,end="")



#eigen variant
word1 = "pinda1kaas23"
word2 = ""
for j in word1:
    if j.isalpha():
        word2 += " "
    else:
        word2 = word2 + j
print("x", word2, "x")


word3 = "Pinda1-Kaas2-3"
for i in word3:
    if i.isalpha():
        word3.replace(i," " )
print( 'x',word3,'x')
