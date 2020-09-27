from datetime import timedelta, date


# I have used this for the part with a date generation:
# https://www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-50.php
# this is not the optimal solution but I am using it as it is working fine
# a better solution would have been to run each line through the dt_list, and store the result in a final dict,
# which we can export to the out_put.txt at the end of the script
# this works only with utf-8 encoded files. if the file has other encoding, I am running it through file -> save as
# than file -> save with encoding -> utf-8 with sublime_text
# the input file should be in the working directory


def daterange(date1, date2):
    for n in range(int((date2 - date1).days) + 1):
        yield date1 + timedelta(n)


start_date = date(2019, 7, 11)
end_date = date(2020, 3, 10)
dt_list = []

for dt in daterange(start_date, end_date):
    dt_list.append(dt.strftime('%Y.%m.%d,'))

final_dict = {}

for el in dt_list:
    temp_dict = {}
    with open('data_input.txt', 'r') as f:
        for line in f:
            temp_list = line.split()
            if el in temp_list:
                if temp_list[2] not in temp_dict:
                    try:
                        temp_dict[temp_list[2]] = [(temp_list[3], float(temp_list[4]))]
                    except:
                        pass
                else:
                    try:
                        temp_dict[temp_list[2]].append((temp_list[3], float(temp_list[4])))
                    except:
                        pass

                try:
                    temp_dict[temp_list[2]].sort(key=lambda tup: tup[1])
                    dt_final = temp_list[2]
                    max_tup = temp_dict[temp_list[2]][-1]
                    min_tup = temp_dict[temp_list[2]][0]
                except:
                    pass
    with open('data_output.txt', 'a') as f_output:
        f_output.write(f'On {dt_final} T max = {max_tup[1]} at {max_tup[0]}, T min = {min_tup[1]} at {min_tup[0]} \n')

print('Done')
