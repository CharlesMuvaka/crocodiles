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


def next_site(data_frame, previous_num=sys.maxsize, previous_site=None):
    minimum_distance = sys.maxsize
    closest_x = None
    closest_y = None

    if previous_site is not None:
        last_coordinate = np.array(data_frame.loc[previous_site]['x'], data_frame.loc[previous_site]['y'])
        # Removing the already visited sight from the frame
        new_frame = data_frame.drop(previous_site, axis=0)
        print(len(new_frame))
        temporary_frame = new_frame.loc[new_frame['number_of_sightings'] < previous_num]

        for row in temporary_frame.itertuples():
            current_coordinate = np.array((row.x, row.y))

            # calculating distance to find out the nearest vertex
            distance = np.linalg.norm(last_coordinate - current_coordinate)
            # print(current_coordinate)

            if distance < minimum_distance:
                minimum_distance = distance
                closest_x = row.x
                closest_y = row.y
                # print(closest_x)
                # print(closest_y)
                closest_node = row.Node
                closest_sighting = row.number_of_sightings

    else:
        updated_frame = data_frame
        temporary_frame = updated_frame.loc[updated_frame['number_of_sightings'] < previous_num]

        # sorting data in the data frame
        sorted_frame = sort_data(temporary_frame, 'number_of_sightings')
        # getting the closest node and the closest co-ordinates of the first sight
        closest_node = sorted_frame.iloc[1].name
        closest_x = sorted_frame.iloc[1]['x']
        closest_y = sorted_frame.iloc[1]['y']
        # print(closest_x)
        # print(closest_y)
        closest_sighting = sorted_frame.iloc[1]['number_of_sightings']

    return int(closest_sighting), closest_node, closest_x, closest_y


