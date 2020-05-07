## Project name: UCU-Semester-Homework: Martian_Weather_Project
Welcome to the Martian Weather Project.

## Description: 
The Martian_Weather_Project consists of an web app, 
which uses NASA's InSight: Mars Weather Service API to provide users with such information as:

* weather for one Sol (Martian day): 
  * average temperature
  * average pressure
  * average wind speed  
* a wind rose for each Sol
* line graphs with such information:
  * minimum week temperature
  * maximum week temperature
  * average week temperature
  * minimum week pressure
  * maximum week pressure
  * average week pressure
  * minimum week wind speed
  * maximum week wind speed 
  * average week wind speed
  
Information is provided visually, using graphs, tables, etc.

Web app is implemented using Python, OOP, abstract data types and structures,Python libraries and modules, etc.

All the information about the process of developing that project and research is available on the project's wiki.
## Table of Contents:
### Main modules:
[main.py](https://github.com/dariaomelkina/UCU-Semester-Homework/blob/master/modules/main.py) –– main module with the actual program.

[adt_weather_data.py](https://github.com/dariaomelkina/UCU-Semester-Homework/blob/master/modules/adt_weather_data.py) –– module with ADT Weather Data Container.

[list.py](https://github.com/dariaomelkina/UCU-Semester-Homework/blob/master/modules/list.py) –– module with list data structure.

[linked_list.py](https://github.com/dariaomelkina/UCU-Semester-Homework/blob/master/modules/linked_list.py) –– module with linked list data structure.

[multi_linked_list.py](https://github.com/dariaomelkina/UCU-Semester-Homework/blob/master/modules/multi_linked_list.py) –– module with multi-linked list data structures.
### Wiki: 
[0. Домашнє завдання №0](https://github.com/dariaomelkina/UCU-Semester-Homework/wiki/0.-%D0%94%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%94-%D0%B7%D0%B0%D0%B2%D0%B4%D0%B0%D0%BD%D0%BD%D1%8F-%E2%84%960)

[1. Домашнє завдання №1](https://github.com/dariaomelkina/UCU-Semester-Homework/wiki/1.-%D0%94%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%94-%D0%B7%D0%B0%D0%B2%D0%B4%D0%B0%D0%BD%D0%BD%D1%8F-%E2%84%961)

[2. Домашнє завдання №2](https://github.com/dariaomelkina/UCU-Semester-Homework/wiki/2.-%D0%94%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%94-%D0%B7%D0%B0%D0%B2%D0%B4%D0%B0%D0%BD%D0%BD%D1%8F-%E2%84%962)

[3. Домашнє завдання №3](https://github.com/dariaomelkina/UCU-Semester-Homework/wiki/3.-%D0%94%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%94-%D0%B7%D0%B0%D0%B2%D0%B4%D0%B0%D0%BD%D0%BD%D1%8F-%E2%84%963)

[4. Домашнє завдання №4](https://github.com/dariaomelkina/UCU-Semester-Homework/wiki/4.-%D0%94%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%94-%D0%B7%D0%B0%D0%B2%D0%B4%D0%B0%D0%BD%D0%BD%D1%8F-%E2%84%964)

[5. Домашнє завдання №5](https://github.com/dariaomelkina/UCU-Semester-Homework/wiki/5.-%D0%94%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%94-%D0%B7%D0%B0%D0%B2%D0%B4%D0%B0%D0%BD%D0%BD%D1%8F-%E2%84%965)
### Example modules:
[libs_and_modules_usage_example.py](https://github.com/dariaomelkina/UCU-Semester-Homework/blob/master/examples/libs_and_modules_usage_example.py) –– module with examples of needed libraries and modules usage.

[api_usage_example.py](https://github.com/dariaomelkina/UCU-Semester-Homework/blob/master/examples/api_usage_example.py) –– module with NASA’s InSight: Mars Weather Service API usage example.

[adt_usage_example.py](https://github.com/dariaomelkina/UCU-Semester-Homework/blob/master/examples/adt_usage_example.py) –– module with ADT Weather Data Container usage example.

## Purpose and usage: 
Project's purpose is to make it easier to access latest information about Martian weather, 
by obtaining it with API and representing visually for the user. Graphs with week data also 
make it much easier to research tendencies, congruences and changes of the weather.

In order to use it such modules and libraries should be installed (apart from project's main modules):
Dash, Plotly, others are inbuilt. (Pandas is installed only for testing and is not used in the actual program)

Web app is launched from the main.py module. It runs locally.

Each time app is launched, information is requested from Nasa, using demo key. 
For higher rate limits it should be replaced by NASA's developer key.

After web app is launched, user can see a table with information about one sol, and, 
on the right, there is a wind rose for that day. In order to switch between other sols, 
there are tabs with numbers of sols, by clicking on which, user can switch to a desired
day. It will automatically change both the table and the wind rose.

All the graphs with whole week's information are located below on the page of the web app.
 
## Example:
![](https://github.com/dariaomelkina/UCU-Semester-Homework/blob/master/docs/app1.png)
![](https://github.com/dariaomelkina/UCU-Semester-Homework/blob/master/docs/app2.jpg)
![](https://github.com/dariaomelkina/UCU-Semester-Homework/blob/master/docs/app3.png)
![](https://github.com/dariaomelkina/UCU-Semester-Homework/blob/master/docs/app4.png)
![](https://github.com/dariaomelkina/UCU-Semester-Homework/blob/master/docs/app5.jpg)
![](https://github.com/dariaomelkina/UCU-Semester-Homework/blob/master/docs/app6.png)

## Input/Output data:
All the data is loaded automatically, using NASA's API, with no need in input from the user. 

Output data is represented visually by tables, charts and line graphics, which are located on the
web apps page.

## Program structure:
Main module consists of functions, used to obtain information with API, to create plotly figures, 
to render information for the web app and of the actual Dash app and its layout. Launching that 
module automatically locally launches the web app.

Assets folder contains background image for the app and a reset ccs for better visual performance.

Module with ADT Weather Data Container contains WeatherData class, which is a key figure in the main module.
Class consists of some standard methods for containers or any other types of data structures, method for extracting data
from a json-string and methods, which return information for main module functions. All the important weather data
is stored in that container.

Modules with list, linked list and multi-linked (double/triple) lists data structures consist of corresponding classes (and
their node classes).

In order to get more information about functions, classes and their methods, have a look at the documentation in the modules.

## Prerequisites: 
Install Dash, Plotly (and Pandas for testing):

``` pip install pandas ```

``` pip install dash ```

``` pip install plotly ```

Obtaining NASA's developer key is arbitrary. It can be done here: https://api.nasa.gov.

## Testing:
There are three modules, provided for testing libraries and modules, used in the project (they should be installed 
on the computer, the module will show, how the data is extracted and represented visually), 
abstract data type Weather Data container (the module demonstrates capabilities of the adt and its functionality, by 
loading data into the adt and showing some visual representations, using adt methods and Dash) and API (the module 
demonstrates, which data can be get with that exact NASA's API, and uses Pandas, to show it). 

They are located in the 'examples' folder. 

## Credits: 
* Daria Omelkina, Ukrainian Catholic University, 2020
