
import collections
import matplotlib.pyplot as plt
import numpy as np

import extract_csv_as_json_list

CSV_FILE_PATH = "data/sample_sfpd_incident_all.csv"

def extract_day_data(source_data):
    day_list = [item["DayOfWeek"] for item in source_data]
    day_dict = collections.Counter(day_list)
    return [
        day_dict["Monday"],
        day_dict["Tuesday"],
        day_dict["Wednesday"],
        day_dict["Thursday"],
        day_dict["Friday"],
        day_dict["Saturday"],
        day_dict["Sunday"]
    ]

def visualize_day_data(source_data):
    day_data = extract_day_data(source_data)
    day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])

    plt.plot(day_data)
    plt.xticks(range(len(day_tuple)), day_tuple)
    plt.savefig("Days.png")
    plt.clf()

def visualize_category_data(source_data):
    category_list = [item["Category"] for item in source_data]
    category_dict = collections.Counter(category_list)

    labels = tuple(category_dict.keys())
    xlocations = np.arange(len(labels)) + 0.5
    width = 0.5

    plt.bar(xlocations, category_dict.values(), width=width)
    plt.xticks(xlocations + width / 2, labels, rotation=90)
    plt.subplots_adjust(bottom=0.4)
    plt.rcParams['figure.figsize'] = 12, 8
    plt.savefig("Categories.png")
    plt.clf()

def main():
    json_list = extract_csv_as_json_list.run(CSV_FILE_PATH)
    #visualize_day_data(json_list)
    visualize_category_data(json_list)

if __name__ == '__main__':
    main()
