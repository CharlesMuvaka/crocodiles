import pandas as pd
import numpy as np
import sys


# sorting the data in descending order
def sort_data(data_frame, data_frame_column):
    return data_frame.sort_values(data_frame_column, ascending=False)


def add_sighting(data_frame, location, water, update):
    if not update:
        data_frame.loc[len(data_frame)] = [len(data_frame), location.newX, location.newY, water, 1]
    else:
        data_frame.loc[
            (data_frame['y'] == location[1]) & (data_frame['x'] == location[0]), ['number_of_sightings']] += 1
    return data_frame
