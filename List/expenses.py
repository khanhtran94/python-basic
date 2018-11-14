import csv
def wirte_csv(a):
  with open('test.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(a)
travel_expenses = [
  [1, 2, 3, 4],
  [1, 3, 4, 2, 3],
  [0, 2, 3, 4, 3],
]
file_name = "test.csv"
print("Travel ")
week_number = 1
for week in travel_expenses:
  a = "* Week #{}: ${}".format(week_number, sum(week))
  week_number += 1
  wirte_csv(a)
  print(a)
