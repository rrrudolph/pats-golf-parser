import json
import csv

# get all the column names for each hole
# for i in range(1,19):
#     print(f"'Hole {i} - Time',")
#     print(f"'Hole {i} - Par',")
#     print(f"'Hole {i} - Strokes',")
#     print(f"'Hole {i} - Handicap Score',")
#     print(f"'Hole {i} - Lat',")
#     print(f"'Hole {i} - Lon',")
# quit()

with open('golfdata.json') as json_file:
    data = json.load(json_file)
 
write_file = open('golf-data.csv', 'w+')
csv_writer = csv.writer(write_file)

headers = [
    "Course",
    "Start Time (UTC)",
    "Start Time",
    "Scorecard URL",
    "Score",
    "Handicap",
    "Strokes",
    "Handicapped Strokes",
    'Hole 1 - Time',
    'Hole 1 - Par',
    'Hole 1 - Strokes',
    'Hole 1 - Handicap Score',
    'Hole 1 - Lat',
    'Hole 1 - Lon',
    'Hole 2 - Time',
    'Hole 2 - Par',
    'Hole 2 - Strokes',
    'Hole 2 - Handicap Score',
    'Hole 2 - Lat',
    'Hole 2 - Lon',
    'Hole 3 - Time',
    'Hole 3 - Par',
    'Hole 3 - Strokes',
    'Hole 3 - Handicap Score',
    'Hole 3 - Lat',
    'Hole 3 - Lon',
    'Hole 4 - Time',
    'Hole 4 - Par',
    'Hole 4 - Strokes',
    'Hole 4 - Handicap Score',
    'Hole 4 - Lat',
    'Hole 4 - Lon',
    'Hole 5 - Time',
    'Hole 5 - Par',
    'Hole 5 - Strokes',
    'Hole 5 - Handicap Score',
    'Hole 5 - Lat',
    'Hole 5 - Lon',
    'Hole 6 - Time',
    'Hole 6 - Par',
    'Hole 6 - Strokes',
    'Hole 6 - Handicap Score',
    'Hole 6 - Lat',
    'Hole 6 - Lon',
    'Hole 7 - Time',
    'Hole 7 - Par',
    'Hole 7 - Strokes',
    'Hole 7 - Handicap Score',
    'Hole 7 - Lat',
    'Hole 7 - Lon',
    'Hole 8 - Time',
    'Hole 8 - Par',
    'Hole 8 - Strokes',
    'Hole 8 - Handicap Score',
    'Hole 8 - Lat',
    'Hole 8 - Lon',
    'Hole 9 - Time',
    'Hole 9 - Par',
    'Hole 9 - Strokes',
    'Hole 9 - Handicap Score',
    'Hole 9 - Lat',
    'Hole 9 - Lon',
    'Hole 10 - Time',
    'Hole 10 - Par',
    'Hole 10 - Strokes',
    'Hole 10 - Handicap Score',
    'Hole 10 - Lat',
    'Hole 10 - Lon',
    'Hole 11 - Time',
    'Hole 11 - Par',
    'Hole 11 - Strokes',
    'Hole 11 - Handicap Score',
    'Hole 11 - Lat',
    'Hole 11 - Lon',
    'Hole 12 - Time',
    'Hole 12 - Par',
    'Hole 12 - Strokes',
    'Hole 12 - Handicap Score',
    'Hole 12 - Lat',
    'Hole 12 - Lon',
    'Hole 13 - Time',
    'Hole 13 - Par',
    'Hole 13 - Strokes',
    'Hole 13 - Handicap Score',
    'Hole 13 - Lat',
    'Hole 13 - Lon',
    'Hole 14 - Time',
    'Hole 14 - Par',
    'Hole 14 - Strokes',
    'Hole 14 - Handicap Score',
    'Hole 14 - Lat',
    'Hole 14 - Lon',
    'Hole 15 - Time',
    'Hole 15 - Par',
    'Hole 15 - Strokes',
    'Hole 15 - Handicap Score',
    'Hole 15 - Lat',
    'Hole 15 - Lon',
    'Hole 16 - Time',
    'Hole 16 - Par',
    'Hole 16 - Strokes',
    'Hole 16 - Handicap Score',
    'Hole 16 - Lat',
    'Hole 16 - Lon',
    'Hole 17 - Time',
    'Hole 17 - Par',
    'Hole 17 - Strokes',
    'Hole 17 - Handicap Score',
    'Hole 17 - Lat',
    'Hole 17 - Lon',
    'Hole 18 - Time',
    'Hole 18 - Par',
    'Hole 18 - Strokes',
    'Hole 18 - Handicap Score',
    'Hole 18 - Lat',
    'Hole 18 - Lon'
]

for i, item in enumerate(data['details']):
    if i == 0:
        csv_writer.writerow(headers)
 
    h = item['scorecardDetails'][0]['scorecard']['holes']
    holes = []
    for num, hole in enumerate(h):
        holes.append(hole.get('lastModifiedDt', ''))
        holes.append(item['courseSnapshots'][0]['holePars'][num])
        holes.append(hole.get('strokes', ''))
        holes.append(hole.get('handicapScore', ''))
        holes.append(hole.get('pinPositionLat', ''))
        holes.append(hole.get('pinPositionLon', ''))

    csv_writer.writerow(
        item['courseSnapshots'][0]['name'],
        item['scorecardDetails'][0]['scorecard']['formattedStartTime'],
        item['scorecardDetails'][0]['scorecard']['startTime'],
        item['scorecardURL'],
        item['scorecardDetails'][0]['scorecard'].get('score', ''),
        item['scorecardDetails'][0]['scorecard'].get('playerHandicap', ''),
        item['scorecardDetails'][0]['scorecard']['strokes'],
        item['scorecardDetails'][0]['scorecard'].get('handicappedStrokes', ''),
        *holes
    )
 
write_file.close()
