#String methods

txt= "ganesh"
print(txt.capitalize())

txt = "GANESH"
print(txt.casefold())
txt = "GANESH"

print(txt.center(10))

txt = "banana"

x = txt.center(20, "-")

print(x)

x = "abcd"

print(x.encode())

txt = "My name is Ståle"

x = txt.encode()

print(x)
txt = "My name is Ståle"
print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))