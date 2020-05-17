tuple1 = (1,2,3,4,5)
tuple2 = (6,7,8,9,10)

result = list(tuple1 [::2] + tuple2[1::2])
print (result)
result = set(result)
print(result)