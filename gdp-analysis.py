import pandas as pd
import numpy as np

# Import the dataset with pandas
df = pd.read_csv('Countries with GDP.txt', sep="\t", header=None)

# The loaded dataframe is in a weird format. We have to do some reformatting to convert the dataframe into a usable format.
df

# The second and fourth rows of the dataframe is where all the info we need are at. We create a new dataframe gdp using those two rows.
gdp = pd.DataFrame(list([df.iloc[1],
    df.iloc[3]]))

gdp.columns = ["Item"]


# The gdp dataframe has only one column containing all the info. We need to split the value in the Item column separated by commas. Iterating over the column...
gdp_new = gdp["Item"].apply(lambda x: pd.Series(x.split(",")))


# Renaming the indexes of the new dataframe created...
gdp_new.index = ["Country","GDP"]


# We transpose the created dataframe and store it to a new variable that gives us the final, usable dataframe for our calculations...
gdp_final = gdp_new.transpose()


# Transforming the GDP column of the gdp_final dataframe to numeric datatype (object by default).
gdp_final["GDP"] = pd.to_numeric(gdp_final["GDP"])


type(gdp_final["Country"][1])


gdp_final["GDP"].argmax()


# Country with highest GDP
print("Country with highest GDP: " +gdp_final.loc[gdp_final["GDP"].argmax()]["Country"])


# Country with lowest GDP
print("Country with lowest GDP: " +gdp_final.loc[gdp_final["GDP"].argmin()]["Country"])


# Entire list of countries with their GDPs
for i in gdp_final.index:
    #print(i)
    print(gdp_final["Country"][i] + ", GDP = " + str(gdp_final["GDP"][i]))

    
# Highest GDP value
print("Highest GDP value is: " +str(gdp_final.loc[gdp_final["GDP"].argmax()]["GDP"]))

# Lowest GDP value
print("Lowest GDP value is: " +str(gdp_final.loc[gdp_final["GDP"].argmin()]["GDP"]))

# Mean GDP value
print("Mean GDP value is: " +str(gdp_final["GDP"].mean()))

# Standard deviation of GDP value
print("Standard deviation of GDP values is: " +str(gdp_final["GDP"].std()))

# Sum of all GDP values
print("Sum of all GDP values is: " +str(sum(gdp_final["GDP"])))
