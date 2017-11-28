
import geojson

import extract_csv_as_json_list

CSV_FILE_PATH = 'data/sample_sfpd_incident_all.csv'
OUTPUT_FILE_NAME = 'temp.geojson'

def get_feature_json(index, line):
    data = {}
    data['type'] = 'Feature'
    data['id'] = index
    data['properties'] = {
        'title': line['Category'],
        'description': line['Descript'],
        'date': line['Date']
    }
    data['geometry'] = {
        'type': 'Point',
        'coordinates': (line['X'], line['Y'])
    }
    return data

def map_data(source_data):
    geo_json = {
        "type": "FeatureCollection",
        "features": []
    }

    for index, line in enumerate(source_data):
        if line['X'] == "0" or line['Y'] == "0":
            continue

        data = get_feature_json(index, line)
        geo_json['features'].append(data)

    with open(OUTPUT_FILE_NAME, 'w') as file_obj:
        file_obj.write(geojson.dumps(geo_json))

def main():
    police_data = extract_csv_as_json_list.run(CSV_FILE_PATH)
    map_data(police_data)

if __name__ == '__main__':
    main()
