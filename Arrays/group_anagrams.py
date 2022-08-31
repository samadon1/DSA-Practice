def groupAnagram(str):
    group = []
    res = []


    def compare(first, second):
        
        first_list = ''.join(sorted(first))
        second_list = ''.join(sorted(second))

        return first_list == second_list 

    for i in range(len(str)):
        group.append(str[i])
        for j in range(i+ 1, len(str)):
            print(str[i] + " --> " + str[j])
            # if compare(str[i], str[j]):
            #     group.append(str[j])
            #     print(group)
        
    # res.append(group)
    return res

str = ["tea", "car", "ate", "ice", "iec"]
print(groupAnagram(str))

# first = "tea"
# second = "ate"
# first_list = ''.join(sorted(first))
# second_list = ''.join(sorted(second))
# print(first_list == second_list)
# print(second_list)