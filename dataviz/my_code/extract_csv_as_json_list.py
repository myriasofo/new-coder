
import csv

CSV_FILE_PATH = "data/sample_sfpd_incident_all.csv"

def run(file_path):
    json_list = []
    with open(file_path) as file_obj:
        csv_file = csv.reader(file_obj, delimiter=',')
        column_names = next(csv_file)
        for row in csv_file:
            column_row_tuples = zip(column_names, row)
            column_row_json = dict(column_row_tuples)
            json_list.append(column_row_json)
    return json_list

def main():
    parsed = run(CSV_FILE_PATH)
    print('data type of output:', type(parsed))
    print("data type of output's elements:", type(parsed[0]))
    print(parsed[0])
    print(len(parsed))

if __name__ == '__main__':
    main()
