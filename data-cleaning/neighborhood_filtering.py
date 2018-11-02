import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from geopy.geocoders import Nominatim

evictions = pd.read_csv("Evictions_cleaned.csv")
neighborhoods = evictions["Neighborhoods - Analysis Boundaries"].unique()
nbd_dict = {}

def nbhd_filter(df, neighborhood = None, eviction_type = 'all'):
    nbds = df[df["Neighborhoods - Analysis Boundaries"] == neighborhood]
    if eviction_type == 'all':
        return len(nbds.index)
    else:
        return len(nbds[nbds[eviction_type] == True].index)

for nbd in neighborhoods:
    nbd_dict[nbd] = nbhd_filter(evictions, nbd)

sorted_evictions = pd.DataFrame.from_dict(nbd_dict, orient="index", columns = ["Total Evictions"])

eviction_types = evictions.columns[6:24]

for x in eviction_types:
    for n in neighborhoods:
        sorted_evictions[x] = nbhd_filter(evictions, n, x)

