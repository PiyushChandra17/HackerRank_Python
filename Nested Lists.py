mark_sheet = []
score_list = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    mark_sheet.append([name,score])
    score_list.append(score)

second_lowest_score = sorted(list(dict.fromkeys(score_list)))[1]

for name,score in sorted(mark_sheet):
    if score == second_lowest_score:
        print(name)