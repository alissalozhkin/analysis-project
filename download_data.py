"""
Module to download data from the requisite datasets for our final project.
"""
from typing import Dict


def get_temperature_data(file_name: str) -> Dict[int, float]:
    """Return a dictionary mapping year to annual mean, from the Bloomberg dataset about
    annual average mean for temperature. Retrieved data goes from 1880 to 2014.
    Preconditions:
        - file is csv
        - file is not empty
        - file is the same format as https://www.bloomberg.com/graphics/2015-whats-warming-the-world/data/observed.csv

    """
    with open(file_name, encoding='utf-8') as f:
        f.readline()  # reading in the header row

        temperature_data = {}

        for line in f:
            split_line = str.split(line, ',')
            year = int(split_line[0])
            mean = float(split_line[1])

            temperature_data[year] = mean

    return temperature_data


def get_sea_data(file_name: str) -> Dict[int, float]:
    """Return a dictionary mapping year to annual average increase in sea level,
    where the 'base' sea level occurs in 1880. Retrieved data goes up to 2013.
     Preconditions:
        - file is csv
        - file is not empty
        - file is the same format as https://www.epa.gov/sites/production/files/2016-08/sea-level_fig-1.csv
    """
    with open(file_name, encoding='utf-8') as f:
        for _ in range(7):
            f.readline()  # reading in the header, which is 7 lines long

        sea_data = {}

        for line in f:
            split_line = str.split(line, ',')
            year = int(split_line[0])

            if year != 2014 and year != 2015:
                sea_change = float(split_line[1])

                sea_data[year] = sea_change

    return sea_data


def get_glacier_data(file_name: str) -> Dict[int, float]:
    """Return a dictionary mapping year to change in glacier mass balance.
     Retrieved data goes from 1945 to 2014.
    Preconditions:
        - file is csv
        - file is not empty
        - file is the same format as https://datahub.io/core/glacier-mass-balance#data
        - glacier mass balance over time
    note: there's a lot of repeated code here compared to get_temperature_data,
    consider somehow merging some functions?
    """
    with open(file_name, encoding='utf-8') as f:
        f.readline()  # reading in the header line

        glacier_data = {}

        for line in f:
            split_line = str.split(line, ',')
            year = int(split_line[0])
            mass_change = float(split_line[1])

            glacier_data[year] = mass_change

    return glacier_data


def get_gas_data(file_name: str) -> Dict[int, float]:
    """Return a dictionary mapping year to average annual CO2 levels.
     Retrieved data goes from _ to _.
    Preconditions:
        - file is csv
        - file is not empty
        - file is the same format as https://www.co2.earth/monthly-co2
        - average of CO2 is measured by Ppm (parts per million)
        FIXME: THE FUNCTION IS NOT COMPLETE.
    """
    with open(file_name, encoding='utf-8') as f:
        f.readline()  # reading in the header line

        gas_data = {}

        for line in f:
            split_line = str.split(line, ',')
            year = int(split_line[0])
            average_level = float(split_line[1])

            gas_data[year] = average_level

    return gas_data
