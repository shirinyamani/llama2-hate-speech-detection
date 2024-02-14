import pandas as pd
import numpy as np

# importing data
binary_data = pd.read_csv('../data/Ethos_Binary.csv', delimiter=';')
multilabel_data  = pd.read_csv('../data/Ethos_Multi_Label.csv', delimiter=';')

#building dataset for the tast
sexist = pd.DataFrame(multilabel_data[multilabel_data['gender']>=.5]['comment'])
racist = pd.DataFrame(multilabel_data[multilabel_data['race']>= .5]['comment'])
not_hate = binary_data[binary_data['isHate']==0]

#add column of category
sexist["category"] = "sexist"       # Add "category" column to comments
racist["category"] = "racist"       # ""
not_hate["category"] = "not hate" 

#all in one single dataframe
comments = pd.concat([sexist, racist])
comments.reset_index(drop=True)