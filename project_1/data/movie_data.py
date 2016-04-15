import os
import json
import pandas as pd
import numpy as np
import sys

from pprint import pprint

import logging
# Initializing a logger
logger = logging.getLogger(__name__)

# read in the dataset
def get_movies(aDir):
    import os, json
    file_contents = os.listdir(aDir)

    movie_list = []

    for filename in file_contents:
        filepath = os.path.join(aDir, filename)

        if not filename.endswith(".json"):
            continue

        with open(filepath, 'r') as movie_file:
            movie_data = json.load(movie_file)
        if hasattr(movie_data, "keys"): # type(movie_data) == dict:
            movie_list.append(movie_data)
    return movie_list
