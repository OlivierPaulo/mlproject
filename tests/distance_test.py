# -*- coding: UTF-8 -*-

# Import from standard library
import os
import mlproject
import pandas as pd

# Import distance module with haversine function
from mlproject.distance import haversine
import pytest


def test_haversine():

    lat1, lon1 = 48.865070, 2.380009
    #Insert your coordinates from google maps here
    lat2, lon2 = 38.726291, -9.135888

    assert haversine(lon1, lat1, lon2, lat2) == 1454.4836015886594
