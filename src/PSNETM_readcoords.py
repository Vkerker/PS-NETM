import os
import pandas as pd
from PSNETM_XYZ_to_NEU import xyz_to_neu
from datetime import datetime, timedelta


def prideppp_read(dir):

    columns = ["x", "y", "z", "date"]
    coordinates = pd.DataFrame(columns=columns)
    for file in os.listdir(dir):
        f = os.path.join(dir ,file)
        with open(f, 'r') as file:
            lines = file.readlines()
            if lines[22].startswith("NO"):
                continue
            else:
                coords = lines[45].split()
                add_coords = pd.DataFrame([[float(coords[2]), float(coords[3]), float(coords[4]), str(lines[3][0:10])]], columns=columns)

                coordinates = pd.concat([coordinates, add_coords], ignore_index=True)
                coordinates["date"] = pd.to_datetime(coordinates["date"])
                coordinates.index = coordinates["date"]
        stname = lines[0][0:4].upper()    
    del coordinates["date"]
    topo_coords = xyz_to_neu(coordinates)
    
    return topo_coords, stname

def NEU_read(file):

    columns = ["N", "E", "U"]
    coordinates = pd.DataFrame(columns=columns)
    dates = pd.DataFrame(columns=["decYr"])
    with open (file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith("#"): continue
            line_data = line.split()
            add_coordinate = pd.DataFrame([[ float(line_data[3]), float(line_data[4]), float(line_data[5]) ]], columns=columns)
            add_date = pd.DataFrame([float(line_data[0])], columns=dates.columns)

            coordinates = pd.concat([coordinates, add_coordinate], ignore_index=True)
            dates = pd.concat([dates, add_date], ignore_index=True)
        dates = decimal_year_to_datetime(dates)
        coordinates.index = pd.to_datetime(dates["Datetime"])
        return coordinates
    
def series_read(file):

    columns = ["N", "E", "U"]
    dates = pd.DataFrame(columns=["decYr"])
    coordinates = pd.DataFrame(columns=columns)
    with open (file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith("#"): continue
            line_data = line.split()
            add_coordinate = pd.DataFrame([[ float(line_data[1]), float(line_data[2]), float(line_data[3]) ]], columns=columns)
            add_date = pd.DataFrame([float(line_data[0])], columns=dates.columns)

            coordinates = pd.concat([coordinates, add_coordinate], ignore_index=True)
            dates = pd.concat([dates, add_date], ignore_index=True)

        dates = decimal_year_to_datetime(dates)
        coordinates.index = pd.to_datetime(dates["Datetime"])
        return coordinates

def XYZ_read(dir):

    columns = ["x", "y", "z"]
    coordinates = pd.DataFrame(columns=columns)
    dates = pd.DataFrame(columns=["decYr"])

    with open (dir, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith("#"): continue
            line_data = line.split()
            add_coordinate = pd.DataFrame([[ float(line_data[3]), float(line_data[4]), float(line_data[5]) ]], columns=columns)
            add_date = pd.DataFrame([float(line_data[0])], columns=dates.columns)
            
            coordinates = pd.concat([coordinates, add_coordinate], ignore_index=True)
            dates = pd.concat([dates, add_date], ignore_index=True)
        dates = decimal_year_to_datetime(dates)
        coordinates.index = pd.to_datetime(dates["Datetime"])
        neu_coords = xyz_to_neu(coordinates)
    return neu_coords

def resample_coords(data):
    data = data[~data.index.duplicated()]
    data = data.resample("D").asfreq()
    if data.isnull().values.any():
        data.interpolate(method="linear", inplace=True)
    return data


def decimal_year_to_datetime(dataframe):
    dataframe['Datetime'] = pd.to_datetime(dataframe['decYr'].apply(lambda x: datetime(int(x), 1, 1) + timedelta(days=(x - int(x)) * 365.25))).dt.round('h').dt.date
    return dataframe