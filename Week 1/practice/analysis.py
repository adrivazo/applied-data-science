import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas_profiling
#read the file and create data frame

if __name__ == '__main__':
    print("hello!")
    data = pd.read_csv("master.csv")

    print(data.head())

    # Is the suicide number more prominent in some age categories than others?
    print(data.groupby("generation")["suicides_no"].sum().to_frame().reset_index().sort_values(by="suicides_no"))
    #yes boomers

    ##country,year,sex,age,suicides_no,population,suicides/100k pop,
    # country-year,HDI for year, gdp_for_year ($) ,gdp_per_capita ($),generation

    #Which countries have the highest and the least number of suicides?
    print(data.groupby("country")["suicides_no"].sum().to_frame().reset_index().sort_values(by="suicides_no"))
    print(data.groupby("country")["suicides/100k pop"].sum().to_frame().reset_index().sort_values(by="suicides/100k pop"))

    #What is the effect of population on suicide numbers?
    # data
    X = data['population']
    Y = data['suicides_no']

    # plot the scatter plot
    sns.scatterplot(x=X,y=Y,data=data,size='suicides_no')


    # add the axes labels to the plot
    plt.xlabel('population')
    plt.ylabel('suicides_no')

    # display the plot
    plt.savefig("scatter pop suicides new.png")

    # compute correlation
    corr_matrix = data.corr()

    # plot heatmap
    # 'annot=True' returns the correlation values
    sns.heatmap(corr_matrix, annot=True)

    # display the plot
    plt.savefig("corr.png")

