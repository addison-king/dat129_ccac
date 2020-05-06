# Final Project - Spring 2020 - API - Database - Pandas - Matplotlib

## Proposed requirements:
### objective

Create a culminating project in the Python language that demonstrates solid scripting design and thoughtful program design utilizing methods for modularity and basic data processing with files, APIs, databases, and Pandas

### design requirements

1.  Thoughtfully use exception handling to cope with unexpected or failure outcomes, such as files not existing, the system not connecting to the Internet for GET requests, etc. When possible write useful information about the source of the errors to a log file for later review and adjustment or re-running of code.
2.  When possible, consider ways your code can be modularized to be useful for related--but not identical--projects like yours. How can you decouple specific names of pages or HTML elements, for example, from the python code itself? Perhaps custom values can live in text files and be read in dynamically by your python code.
3.  Create meaningful output messages that your script can give to the user to monitor the progress and activities of your script.
---
## Workflow
### Overall goals:
1. New TV Series per year
2. New TV Series per decade
3. Number of shows per season count
4. Average runtime

***TL;DR: Queries TheTVDB.com API for a season ID. Stores the information about that ID into a sqlite db. Using Python, extracts data from the db to analyze using pandas (dataframes) and matplotlib (graphs).***

## Step 1 - Data Collection:
- The first step is to get data from TheTVDB API. In order to do so, you need a API authentication token. To get a token you have to have an account on the site and then query the API using your account name, account key, and API key. All unique to you.
- With the API token, you can now ask the API for information. To prevent duplicate ID entries, the program will retrieve the max ID value from the database. This value is then used as the starting point to continue asking the website for more info.
- The API will return several pieces of information about a TV Show (such as, title, number of seasons, runtime, network, first aired date, and genre). The data is parsed into a dictionary (basically json format).
## Step 2 - SQLite:
- The database is comprised of 500,000 entries. Each entry is a different "Series ID" beginning with Series ID = 1 to Series ID = 500,000. Overall, there is 80,189 different named TV Shows in the database. 
- Several different SQLite commands were used to extract only pertinent data for the task at hand (for example, selecting only runtime values, if seriesName and runTime are not null values).
- Once the data was extracted (initially in tuple format) it is converted into a long list. 
## Step 3 - Analysis & Graphing:
- Taking the list of selected data, it was turned into a dataframe. Once in dataframe format, the data can be ordered and analyzed further.
- 3 graphs (New TV Series per decade, New TV Series per year, Number of Seasons per show) and 1 stat (average runtime) were created.

![New Television Series Divided by Decades](https://raw.githubusercontent.com/brandyn-gilbert/dat129_ccac/master/Final%20Project/Figure%20-%20New%20TV%20Series%20Per%20Decade.png)
![New Television Series Divided by Year](https://raw.githubusercontent.com/brandyn-gilbert/dat129_ccac/master/Final%20Project/Figure%20-%20New%20TV%20Series%20Per%20Year.png)
![Television Series Divided by Number of Seasons per Show](https://raw.githubusercontent.com/brandyn-gilbert/dat129_ccac/master/Final%20Project/Figure%20-%20Seasons%20Per%20TV%20Show.png)
![Typical console output](https://raw.githubusercontent.com/brandyn-gilbert/dat129_ccac/master/Final%20Project/Console%20Output%20-%20runtime.PNG)