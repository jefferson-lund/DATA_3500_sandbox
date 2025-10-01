# """
# given a list, return another list with the products of each number in the first list

# probably loop through the list once for each int in the list, and multiply by each other number (noninclusive)
# either secondlist[x] = [number * i]
# or secondlist[i] = list[i] * x

# """

# input_list = [1,2,3]
# output_list = []

# for i in input_list:
#     product = 1
#     for j in input_list:
#         if i == j:
#             continue
#         product *= j

#     output_list.append(product)

# print(output_list)



ages = [22, 34, 98, 67]
ages.append(21)
print("ages: :", ages)
ages.pop(2)
print("ages:", ages)
ages.insert(2, 101)
print("ages:", ages)

 