import pandas as pd
import numpy as np


df = pd.read_csv('Countries with GDP.txt', sep="\t", header=None)


df


gdp = pd.DataFrame(list([df.iloc[1],
    df.iloc[3]]))


#gdp["Item"].apply(lambda x: pd.Series(x.split(","))).index = ["Country","GDP"]


gdp_new = gdp["Item"].apply(lambda x: pd.Series(x.split(",")))


gdp_new.index = ["Country","GDP"]


gdp_final = gdp_new.transpose()


gdp_final["GDP"] = pd.to_numeric(gdp_final["GDP"])


type(gdp_final["Country"][1])


gdp_final["GDP"].argmax()


print(gdp_final.loc[gdp_final["GDP"].argmax()]["Country"])


print(gdp_final.loc[gdp_final["GDP"].argmin()]["Country"])


for i in gdp_final.index:
    #print(i)
    print(gdp_final["Country"][i] + " - " + str(gdp_final["GDP"][i]))


print("Highest GDP value is: " +str(gdp_final.loc[gdp_final["GDP"].argmax()]["GDP"]))


print("Lowest GDP value is: " +str(gdp_final.loc[gdp_final["GDP"].argmin()]["GDP"]))


print("Mean GDP value is: " +str(gdp_final["GDP"].mean()))


print("Standard deviation of GDP values is: " +str(gdp_final["GDP"].std()))


print("Sum of all GDP values is: " +str(sum(gdp_final["GDP"])))
