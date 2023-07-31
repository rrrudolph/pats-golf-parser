import json
import csv

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
]

# Add the column names for each hole
for i in range(1,19):
    headers.append(f'Hole {i} Time')
    headers.append(f'Hole {i} Par')
    headers.append(f'Hole {i} Strokes')
    headers.append(f'Hole {i} Handicap Score')
    headers.append(f'Hole {i} Lat')
    headers.append(f'Hole {i} Lon')

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
