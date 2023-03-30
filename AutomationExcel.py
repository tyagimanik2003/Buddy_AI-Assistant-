import pandas as pd

filename = 'vegetable_names.csv'

# create a list of monument names
vegetable = ['Bean', 'Bitter_Gourd', 'Bottle_Gourd', 'Brinjal', 'Broccoli', 'Cabbage', 'Capsicum', 'Carrot', 'Cauliflower', 'Cucumber', 'Papaya', 'Potato', 'Pumpkin', 'Radish', 'Tomato']


# create a pandas dataframe with the monument names
df = pd.DataFrame(vegetable, columns=['Vegetable Name'])

# write the dataframe to a new CSV file
df.to_csv(filename, index=False)
