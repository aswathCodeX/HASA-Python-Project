# GUI using python for extrapolation of a hydrograph
##image
***
```
Background: Gumbel distribution is used to model the maximum or minimum of samples of various distribution.
Gumbel distribution predicts the chances of an extreme events like floods, earthquakes and other natural calamity.
The ability of the Gumbel distribution to represent the maxima can be used to predict future discharges in a river.
```
```
Goal: To predict 50, 100, 150, 200 and 1000 year flood discharge using Gumbel distribution and showcasing the results in a GUI
```
Link to clone the project repository
```

```
## Theory
### Gumbel Distribution
The Gumbel distribution is named after [Emil Julius Gumbel](https://en.wikipedia.org/wiki/Emil_Julius_Gumbel). Gumbel distribution is a special case of [generalized extreme value distribution](https://en.wikipedia.org/wiki/Generalized_extreme_value_distribution).

The gumbel distribution formula is 
     
Q = Qm.(1+K.Cv) 

where
* Q = Probable discharge with a return period of T years

* T = 50,100,150,200,1000 years

* Qm = Mean discharge

* K = Frequency factor 
    * K = (Yt - Yn) / Sd
    * Yt = -lnln (T/T-1) 
    * Yn = Expected Reduce mean of the gumbel distribution
    * Sd = Expected Reduce standard deviation of gumbel distribution

* Cv = Coefficient of variation

     * Cv = Sd / Qm

In order to determine the value of K, from the gumbel reduce table Yn and Sd needs to be extracted
##Data 
### Gumbel reduce table
In the gumbel reduce table possible values of Expected mean and Expected standard deviation is given with respect to the Number of data available.

Data is continuous from 10 number of data to 100.
After 100, 150 and 200 number of data is provided in the table. The reduce data is available in ```.csv``` format

| Number of data | Reduce mean | Reduce std |
|----------------|:------------|-----------:|
|         10       |    0.4952         |      0.9497       |
11|0.4996|0.9676
12|0.5035|0.9833
... |...|...
100|0.56|1.2065
150|0.5646|1.2253
200|0.5672|1.236
###Hydrological data

Hydrological data is extracted from River Necker using the [Website](https://udo.lubw.baden-wuerttemberg.de/public/q/3MD4H4f2pqsu7JaXsrmIRA)
Hydrological data is from Obendorf 409 station in Necker.

Data is available in ```.csv``` format

| YYYY-MM-DD | Q (m3/s) |
|------------|:------------|
|         01-11-1929      |   4.086        | 
| 02-11-1929     |6.326|
|...|...|
|31-12-2021| 11.79|

#Code
##Framework
Various functions and classes are created in accordance with the following flowchart
## flowchart

* ```main.py``` contains 4 functions- ```verify_gumbel()```,```get_reduce_mean()```,```get_reduce_std()```, ```gumbel_distribution()```
* ```Discharge_data.py```contains a class ```Discharge_data_handler```. the class contains 3 methods
* ```plot_discharge.py```contains a class ```plotting```. the class contains 2 methods and 3 magic methods
* ```gui.py```
* ```config.py```contains all the packages and modules and path that is required in the project
* ```fun.py```contains logging functions
* ```gumbel_reduce.py```contains ```gumbel_reduce()```

###Extracting hydrological and gumbel reduce data

```necker-data.csv``` contains discharge data from 1929 to 2021, separated by ```,```

In ```discharge_data.py``` disacharge_data_handler class and ```get_discharge_data``` and ```print_discharge_data``` method is present


``` 
class Discharge_data_handler:    
    def __init__(self):
        self.sep = ';'
        self.Discharge_data = pd.DataFrame

    def get_Discharge_data(self,csv):
        self.Discharge_data = pd.read_csv(csv, header=10,
                                          names=['Date', 'Discharge'],
                                          sep=self.sep,
                                          usecols=[0, 1], parse_dates=[0], index_col='Date')
        annual_max = self.Discharge_data.resample(rule='A', kind='period').max()
        annual_max["year"] = annual_max.index.year
        annual_max.reset_index(inplace=True, drop=True)
        return annual_max

```
get_discharge_data method takes an argument```csv```which is the path for the discharge data.
Data is sorted using pandas data frame and resampled to annual maxima using ```resample(rule='A', kind='period').max()```
Each year is indexed and the method returns pandas dataframe, which includes ```Discharge``` and ```year``` column with maximum annual discharge in the ```Discharge``` column. 
To print the sorted pandas dataframe print_Discharge_data method is used
```
    def print_Discharge_data(self):
        print(self.Discharge_data)
```
***
```gumbel.csv```contains gumbel reduce values separated by ```,``` for 10 to 200 number of datas.
It contains 3 columns ```Data number```, ```Reduce mean```,``` Reduce std```.
In ```gumbel_reduce.py``` ,``` gumbel_reduce()``` function is present.
```
def Gumbel_reduce(csv_file=''):
    Data = pd.read_csv(csv_file,header=0,
                       sep=',',
                       names = ['Number of Data', 'Reduce mean', 'Reduce std'],
                       usecols = [0, 1, 2],
                       index_col = 'Number of Data')
    return Data
```
```gumbel_reduce``` function takes an argument ```csv_file``` which is the path for the gumbel reduce data.
pandas dataframe is used to sort the data into 3 columns and assigned index column to the ```Number of Data```.
###Plotting
In plot_discharge.py one class ```plotting``` and 5 method is present.
Among the methods 3 are magic methods.

Application of plotting class is to plot the hydrograph for the Necker data and the exptrapolated discharges for 50, 100, 150,200,1000 years.

method ```plot_discharge``` and 3 magic methods are linked to plotting the hydrograph for the Necker data. 
```

class plotting:
        def __init__(self):
                self.t = pd.Series
                self.q = pd.Series
                self.T = np.array
                self.Q = np.array
                self.c = str
                self.s = 10
        def __mul__(self, multiplier):
                self.s *= multiplier
                return self.s

        def __gt__(self,value):
                 if self.s > value:
                         print('The Hydrograph scatter points are too big')

        def  __lt__(self,value):
                 if self.s < value:
                         print('The Hydrograph scatter points are too small')

        def plot_discharge(self, time_series=pd.Series(), q_series=pd.Series(), title="",color=""):
                self.t = time_series
                self.q = q_series
                self.c = color
                fig, axes = plt.subplots(figsize=(20,10))
                axes.scatter(x=self.t, y=self.q,marker='o', s=self.s, color=self.c)
                axes.set(xlabel="Year", ylabel="Discharge (CMS)", title=title)
                plt.xlim(self.t.min(),self.t.max())
                plt.grid()
                plt.show()
```
method ```plot_discharge() ```takes 4 arguments ```time series```,``` q_series```, ```title``` and ```color```.

```time series``` and ```q_series``` has to be pandas dataframe. ```color``` and ```title``` should be string.

```plot_discharge``` is generating a scatter plot for all the hydrological data. the flexibility on the size of the scatter points are controlled by ```__mul__()```,```__gt__()``` and ```__lt__()```. ```__mul_()```multiplies the scatter plot size by a factor of 10 while ```__lt__()``` warns the user if the scatter points are too small to discern by generating a print statement ```The Hydrograph scatter points are too small```  and ```__gt__()``` warns the user that scatter points are too large and might overlap and generates a print statement ```The Hydrograph scatter points are too big```.

```__mul__()``` method can be accessed by ```*```,```__gt__()``` can accessed by ```>```,```__lt__()``` can be accessed by ```<```. 
***
```gumbel_plotting()```method takes 4 arguments ```t_series```, ```q_series```, ```title``` and ```color```. The method generates a line graph for the extrapolated values.

```t_series```and ```q_series``` should be numpy array


```
def Gumbel_plotting(self, t_series, q_series, title='', save='',color=''):
                self.T = t_series
                self.Q = q_series
                fig, axes = plt.subplots(figsize=(20, 10))
                axes.plot(self.T, self.Q,linestyle="-",label='Extrapolation',marker="x",color=color)
                axes.legend()
                axes.set(xlabel= "Flood return period",ylabel="Discharge (CMS)", title=title)
                axes.set_xlim((0,1000))
                axes.set_ylim((0,400))
                plt.grid()
                plt.show()
   ```
###Main script
In the main script ```verify_gumbel()```, ```get_reduce_mean()```, ```get_reduce_std()``` and ```gumbel_distribution()``` functions are present.

```get_reduce_mean()```takes an argument and index the ```gumbel.csv``` file to extract the reduce mean.

The argument is the number of years of hydrological data available.
```
def get_reduce_mean(index):
    if index in range(100,150):
        index = 150
    elif index in range(150,200):
        index = 200
    value =Gumbel_reduce(csv_file=gumbel_reduce_path)
    return value['Reduce mean'][index]
```
```get_reduce_std()```takes an argument and index the ```gumbel.csv``` file to extract the reduce standard deviation.

The argument is the number of years of hydrological data available
```
def get_reduce_std(index):
    if index in range(100,150):
        index = 150
    elif index in range(150,200):
        index = 200
    value = Gumbel_reduce(csv_file=gumbel_reduce_path)
    return value['Reduce std'][index]
```
If the number of years of hydrological data that is available is greater than 100 years and less than 150 years, reduce mean and standard of 150 year will be considered. For greater than 150 years data, 200 year value will be taken into account.
***
```gumbel_distribution()``` calculates the extrapolated discharges for 50,100,150,200 and 1000 years using gumbel distribution and provide a list with discharge values.
```
 def Gumbel_distribution(Discharge_data):
    number_of_years= Discharge_data.shape[0]
    mean_discharge = Discharge_data['Discharge'].mean()
    std_dev = Discharge_data['Discharge'].std()
    reduce_mean = get_reduce_mean(number_of_years)
    reduce_std =  get_reduce_std(number_of_years)
    time_list = [50,100,150,200,500,1000]
    main_discharge = []
    for year in time_list:
        P = math.log(year / (year - 1))
        reduced_variate = -math.log(P)
        Frequency_factor = (reduced_variate - reduce_mean) / reduce_std
        Discharge_value = mean_discharge + Frequency_factor * std_dev
        main_discharge.append(Discharge_value)
    return main_discharge
```
In ```gumbel_distribution()```statistical pandas dataframe methods ```shape()```,```mean()```,```std()```. are used to get the discharge data size, mean and standard deviation.

```get_reduce_mean()``` and ```get_reduce_std()``` are called to determine the reduce mean and reduce standard deviation.

Inside the ```for``` loop all the anticipated parameters of the gumbel distribution is calculated and extrapolated discharge is append to an empty list.
***
```verify_gumbel()``` is a wrapper function which wrap the ```get_reduce_mean()``` and ```get_reduce_std()```function to make sure that the indexing value is within the limits of the gumbel reduce data provided in the file ```gumbel.csv```. Otherwise the function prints an error statement.
```
 def verify_Gumbel(func):
    def wrapper(args):
        try:
            result = func(args)
            print('No of years are within the gumbel reduce limit')
            return result
        except TypeError:
            print('ERROR: To extract reduce value numeric value is to be passed')
            return 0.0
        except ValueError:
            print('ERROR: To extract reduce value years should be in limit')
            return 0.0
    return wrapper
```
```discharge_data_handler``` class is instantiated and ```get_discharge_data()``` is called to retrieve and sort the discharge data.
```
Raw_Discharge_data = Discharge_data_handler()
data = Raw_Discharge_data.get_Discharge_data(csv=Discharge_data_path)
```
Discharge data is put as an argument in the```gumbel_distribution()```function and the output is list.
```
output_list=Gumbel_distribution(data)
```
```plotting``` class is instantiated, magic methods are exercised and hydrograph is plotted using ```plot_discharge()``` method.
```
plote=plotting()
plote * 15
plote > 150
plote < 5
plote.plot_discharge(data['year'],data['Discharge'],title='Hydrograph',color='grey')
```
Extrapolated discharges are plotted using ```gumbel_plotting()```method.

```
time_list = [50,100,150,200,500,1000]
x=np.array(time_list)
y=np.array(output_list)
plote.Gumbel_plotting(x,y,title='Gumbel Extrapolation',color='black')
```
A dictionary is generated containing the years and the extrapolated discharge values.
```
Main_dict = {}
for index,time in enumerate(time_list):
    Main_dict[time]=output_list[index]
print(Main_dict)
```
###GUI

###logging function

###config
In the ```config.py```script, all the libraries and packages are imported and paths of the reduce dataset and discharge data is defined.
```
try :
    import logging
    import os
    import numpy as np
    import pandas as pd
    import math
    import matplotlib.pyplot as plt
    import matplotlib.cm as cm
    from tkinter import *
    import tkinter as tk
    from tkinter.messagebox import showinfo
    from tkinter import ttk
    from tkinter.messagebox import showinfo, showerror
except ModuleNotFoundError as e:
    print('ModuleNotFoundError: Missing basic libraries and packages')
    print(e)

Discharge_data_path= os.path.abspath('')+ '\Discharge-data/Neckar-data.csv'
gumbel_reduce_path= os.path.abspath('')+'\gumbel_reduced/gumbel.csv'
```