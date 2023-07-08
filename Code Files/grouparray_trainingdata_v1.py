# -*- coding: utf-8 -*-
"""
Created on Mon May  1 23:58:10 2023

@author: yuzhe
"""

import pandas as pd
import pickle

# Read the CSV file
csv_file = '4-30_testingdata_v2.csv'
df = pd.read_csv(csv_file)


# Group the data by Company Name and Year and merge the text
grouped = df.groupby(['Company Name', 'Year'])['Text'].apply(' '.join)

# Convert the grouped data into a list of texts
training_data = grouped.tolist()

# Save the training data as a pickle file
pickle_file = '5-2_testingdata_v1.pickle'
with open(pickle_file, 'wb') as f:
    pickle.dump(training_data, f)

