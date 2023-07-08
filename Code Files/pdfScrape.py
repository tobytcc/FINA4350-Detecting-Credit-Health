# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 03:31:42 2023

@author: yuzhe
"""

import os
import pandas as pd
from PyPDF2 import PdfReader
import re

# The folder where the PDFs are saved
pdf_folder = r'C:\Users\yuzhe\OneDrive\1. Academics\FINA4350\4350 Project\Testing Data\Process\Resources'



# Initialize an empty dataframe
df = pd.DataFrame(columns=['Company Name', 'Document Type', 'Year', 'Page_Number', 'Text'])

# Iterate over each file in the folder
for filename in os.listdir(pdf_folder):
    if filename.endswith('.pdf'):
        # Open each PDF file
        with open(os.path.join(pdf_folder, filename), 'rb') as file:
            # Initialize a PDF file reader object
            pdf_reader = PdfReader(file)
            
            # Split the filename
            company_name, document_type, year = filename.rsplit('.', 1)[0].split('_')
            
            # Iterate over each page in the PDF
            for page_num in range(len(pdf_reader.pages)):
                # Skip pages with a page number less than 10 as most likely its content page and management discussion usually starts at 20+ pages
                if page_num < 9:  # Page numbering starts at 0, so page 10 would be index 9
                    continue
                
                # Extract the text from the page
                text = pdf_reader.pages[page_num].extract_text()

                # Remove Chinese characters
                text = re.sub(r'[\u4e00-\u9fff]+', '', text)

                # Remove numbers
                text = re.sub(r'\d+', '', text)

                # Remove special characters
                text = re.sub(r'[^a-zA-Z\s]', '', text)
                
                #Remove extra white spaces
                text = re.sub(r'\s+',' ',text)
                
                # Normalize the text
                normalized_text = text.lower()
                
                # Remove single characters
                normalized_text = re.sub(r'\s+\w\s+', ' ', normalized_text)

                # Get the first 200 words
                first_100_words = ' '.join(normalized_text.split()[:100])

                # Check if the first 100 words contain "management discussion and analysis"
                if "management discussion and analysis" in first_100_words:
                    # Append the data to the dataframe
                    data_dict = {'Company Name': company_name, 'Document Type': document_type, 
                                    'Year': year, 'Page_Number': page_num+1, 'Text': text}
                    df = pd.concat([df, pd.DataFrame([data_dict])], ignore_index=True)

# Save the dataframe to a CSV file
df.to_csv('4-30_testingdata_v1.csv', index=False)


# Read the CSV file
csv_file = '4-30_testingdata_v1.csv'
df = pd.read_csv(csv_file)

# Remove leading and trailing spaces
df['Text'] = df['Text'].str.strip()

# Remove single character words
df['Text'] = df['Text'].apply(lambda x: re.sub(r'\b\w\b', '', x))

# Save the cleaned dataframe back to the CSV file
df.to_csv(csv_file, index=False)

