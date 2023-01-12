import pandas as pd
import numpy as np
import sys


# sorting the data in descending order
def sort_data(data_frame, data_frame_column):
    return data_frame.sort_values(data_frame_column, ascending=False)
