# programming_dictionaries = {
#     "Key": "this is the value of frist key",
#     "key2": "this is the 2nd key value",
#     "key3": "this is the 3rd key value,"}
#
# # print(programming_dictionaries)
# # programming_dictionaries["key4"] = "this is change value of key4.."
#
# # programming_dictionaries = {}
# programming_dictionaries["key4"] = "new value"
# programming_dictionaries["key5"] = "key5 value"
# # print(programming_dictionaries)
#
# for key in programming_dictionaries:
#     print(key)
#     print(programming_dictionaries[key])


# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }
#
# student_grades = {}
# for student in student_scores:
#     score = student_scores[student]
#     if score >= 91:
#         student_grades[student] = "Exceeds Expectations"
#     elif score >= 81:
#         student_grades[student] = "outstanding"
#     elif score >= 71:
#         student_grades[student] = "Acceptable"
#     elif score <= 61:
#         student_grades[student] = "fail"
# print(student_grades)

# trave_log = {
#     "france": ["paris", "lille", "dijon"]
# }
# print(trave_log["france"][1])

#nasted list
# nasted_list = ["A", "B", ["C","D"], ["E", "F","G"]]
# print(nasted_list[3][2])
#
# nasted_list = ["A", "B", ["C", "D", ["H", "I", "J"]], ["E", "F", "G"]]
# print(nasted_list[2][2][1])


#Nasted dic
# travel_log = {
#     "france": {
#         "visited_cities": ["paris", "lille", "dijon"],
#         "number_of_times_visited": 3,
#     },
#     "germaney": {
#         "cities": ["barline", "tokyo"]
#     },
#
# }
# print(travel_log["france"]["visited_cities"])
# print(travel_log["france"]["visited_cities"][1])
# print(travel_log["france"]["number_of_times_visited"])
# print(travel_log["germaney"]["cities"][1])

# for travels in travel_log:
#     print(travel_log[travels][1])
    # print(travel_log[travels]["visited_cities"][1])
    # print(travel_log[travels]["number_of_times_visited"])


# starting_dictionary = {
#     "a": 9,
#     "b": 8,
# }
# final_dictionary = {
#     "a": 9,
#     "b": 8,
#     "c": 7,
# }
# final_dictionary["c"] = 7
# starting_dictionary = final_dictionary
# print(starting_dictionary)

dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}
# dict["c"] = 1, 2, 3
# for key in dict:
#     dict[key] += 1
# dict[1] = 4
# print(dict[1])
# dict["c"] =[1,2,3]

print(dict[1])