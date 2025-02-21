
# Set and Def - Unordered and unindexed and is mutable
myset = {"a","b","c"}
print(myset)
# Remove an item from the set
myset.remove("b")
print(myset)
# Clear the set
myset.clear()
print(myset)
# Add an item to the set
myset.add("a")
print(myset)
#Update multplie items to the set using Update
myset.update("b","D")
print(myset)
# Union to join the sets
s1 = {"a"}
s2 = {"b"}
s3 = {}
s3= s1.union(s2)
print(s3)
# Join two sets using update method/function
s1.update(s2)
print(s1)
#Access the items from the set
for x in s1:
    print(x)

