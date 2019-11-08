import csv


def get_top_performers(file_path, number_of_top_students=1):
    with open(file_path, "r") as csv_f:
        rows = list(csv.reader(csv_f))[1:]
    rows.sort(key=lambda r: r[2])
    rows.reverse()
    return [row[0] for row in rows[:number_of_top_students]]


def sort_by_age(input_file_path, output_file_path="data/sorted_by_age_students.csv"):
    with open(input_file_path, "r") as csv_f:
        rows = list(csv.reader(csv_f))
    rows.sort(key=lambda r: r[1])
    rows.reverse()
    with open(output_file_path, "w") as csv_f:
        csv_writer = csv.writer(csv_f)
        csv_writer.writerows(rows)


if __name__ == "__main__":
    print(get_top_performers("data/students.csv", 5))
    sort_by_age("data/students.csv")
