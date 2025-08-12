result = 0
for i in range (1,101):
    result_old = result
    result = result + i
    # print(str(i) + ":" + str(result_old) + " + " + str(i) + " =" + str(result))
    print(f" {i:3} | {result_old:5} + {i:3} = {result:6} ")
print(result)

# 2 datatypes: integers: result, i
#              strings: str(i)
# concatenate strings: "abc" + "def" = "abcdef"