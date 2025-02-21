

sa = 'rud'
a= ''

for i in range(len(sa),0,-1):
    a = a + sa[i-1]
print(a)


c = 12345
d = str(c)
print(len(d))
b= c % 10

c = c //10

#

i= 1

while i<=10:
    print(i)
    i = i+1


print("AAA"*3)



strm = "Welcome"
print(strm[1:3])
print(strm[:6])
print(strm[2:])

print(strm[1:-1])
print(strm[:-2])

print(ord('A'))
print(chr(65))



s=  "welcome"

if "come11" in s :
    print("Yes")
else:
    print("No")


if "come11" not in s :
    print("Yes")
else:
    print("No")
rev = ""
for j in s:
    rev = j + rev
print(rev)