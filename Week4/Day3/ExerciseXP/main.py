# 1#
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# print(dict(zip(keys, values)))

# 2#
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# values = family.values()
# ages = list(values)
# tic = 0
# list = []
# for age in ages:
#     if age < 3:
#         tic = "free"
#         list.append(tic)
#     elif age > 3 & age < 12:
#         tic = 10
#         list.append(tic)
#     elif age > 12:
#         tic = 15
#         list.append(tic)

# sum = sum(list)
# print("total family cost:", sum)

# 3#
# brand = {
#     "name":"zara",
#     "creation_date":1975,
#     "creator_name":"Amancio Ortega Gaona",
#     "type_of_clothes":"men, women, children, home",
#     "international_competitors":"Gap, H&M, Benetton",
#     "number_stores":7000,
#     "major_color":{ 
#             "france":"blue",
#             "spain":"red",
#             "us":"pink, green"
#          }
# }
# brand["number_stores"] = 2
# print(brand["number_stores"])

# print(brand)

# brand["country_creation"] = "spain"
# print(brand["country_creation"])

# del brand["creation_date"]

# print(brand["major_color"]["us"])

# print(len(brand))

# print(brand.keys())

# more_on_zara = {
#     "creation_date": "1975",
#     "number_stores": "10 000"
# }
# print(more_on_zara)

# brand.update(more_on_zara)

# print(brand["number_stores"])
# changed number_stores from 7000 to 10000

# 4#
# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

# users_dict = dict.fromkeys(users, "")
# print(users)
 
# for x in range(5):
#     for user in users:
#        users_dict[user]= x

# print(users_dict)

# r = sorted(users_dict.keys())
# print(r)
