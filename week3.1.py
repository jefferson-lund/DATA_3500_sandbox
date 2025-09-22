
# print("Hello everyone, we love mondays")
# age = 25
# print(age // 2)
# age = 25
# print(age/2)
# print("\n")
# welcome_message = """

# whatsawhasawhasawhasaaaap bitconeeeeeeeectttt

# """
# print(welcome_message)


# # examples

# """
# Professor Harding is running a half marathon - she ran 10 miles in 1 hr 18 minu with a pace of 7:42
# FOr the hald (13.2), what is my projected finish time? Print out like this hr:min:sec
# """
finish_time = 0
pace = ((7*60)+42)
print("Pace:", pace)

half_distance = 13.2
sec_finish = half_distance * pace
print("Seconds to finish:", sec_finish)

projected_hours = sec_finish // 3600
print("Projected Finish Time: ", finish_time)

projected_hours = int(sec_finish // 3600)
projected_min = int((sec_finish % 3600) / 60)
projected_sec = int(sec_finish % 60)

print("Projected Finish Time: " + str(projected_hours) + ":" + str(projected_min) + ":" + str(projected_sec))

stick_man = """

    O 
   /|\
  / | \
    /\
   /  \
   
"""
print(stick_man)