if __name__ == '__main__':
    scores_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores_list.append([name, score])

def lowest_value(score_list):
    min = score_list[0][1]
    for item in score_list:
        if item[1] < min:
            min = item[1]

    return min

x = lowest_value(scores_list)

lowest_value_removed_list = []
for item in scores_list:
    if item[1] > x:
        lowest_value_removed_list.append(item)

second_low_value = lowest_value(lowest_value_removed_list)

second_lowest_value_list = []
for item in lowest_value_removed_list:
    if item[1] == second_low_value:
        second_lowest_value_list.append(item)

name_list = []
for item in second_lowest_value_list:
    name_list.append(item[0])
name_list.sort()

for item in name_list:
    print(item)