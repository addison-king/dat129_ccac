# **Homework - Week 03**

## Overview
1.  Complete our icon project with as many transformations as possible
2.  Make sure to have it pushed to your git repo and have emailed Eric the link and Be sure to have reviewed a peer's project
3.  Explore the city of  [Pittsburg's capital projects on the WPRDC](https://data.wprdc.org/dataset/capital-projects)  and answer a question by processing the dataset as a CSV
4. Dictionaries & files module

## Module: Dictionaries & files 
### resources

The python foundation maintains the most comprehensive and authoritative documentation on all built-in aspects of the python language. Start here:

[_vpn_key_](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)

[Map-based data structures (official documentation)](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)

[_text_fields_](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)

[The String built-in type (official documentation)](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)

### Warm-up 1: Looping to a file

Study the following file contents. Generate a program in Python to reproduce this structure. NOTE: You'll need to use two for() loops, nested. You can try seeing if you can print the pattern out first to the console, then replace the calls to print() with calles to yourfile.write().

![file example](http://www.technologyrediscovery.net/python/img/filesEx1_file.png)

### Warm-up 2: String formatting program specification

1.  Download the following text file of names:  [file link](http://www.technologyrediscovery.net/python/week8_strings/names.txt)
2.  Your desired program output is a formal greeting for individuals whose names exist in a text file in the order: first last. The output should look like this:
![output](http://www.technologyrediscovery.net/python/week8_strings/parsingOutput.png)4.  The process of generating these greetings should take place in two methods: one should read in a file given a file name (assumed to be in the working directory) and extract the name in a single line. The second method should receive a line of text (i.e. a name in the form first last) and generate the greeting. Remember, you'll need to invert the string since we're using string formatting, not string concatenation.

### Group code along with CSV files

What can we infer about the state of criminal justice in Allegheny County from their publicly released jail census?

1.  Download  [this CSV of jail census data](https://technologyrediscovery.net/python/jail.csv)  by right-clicking the link and selecting something like "save link as..."
2.  Visit the WPRDC dataset page

Jail population statistics calculation example: recreate this program without using the CSV module at all! You'll need to use the split() function to break down lines of text from the file, and you'll want to use zip() to combine each row after the header with the values in the header row.

----------

## JSON encoding

### _live_help_Guiding questions

-   What are the most widely used protocols for exchanging data between systems?

### _check_circle_Learning Objectives

-   Parse JSON files into Python objects and manipulate those objects
-   Create JSON files from Python objects and transfer that data to other python systems

_expand_more_toggle full session guide

### _book_Resources

-   [JSON Documentation](https://json.org/)
-   [json python library](https://docs.python.org/3.6/library/json.html#json-to-py-table)
-   [Capital projects in PGH](https://data.wprdc.org/dataset/capital-projects)
-   [geojson specs for kicks](http://geojson.org/geojson-spec.html)

### _list_Lesson sequence

1.  Course oranization system: gitHub and upload index, folders, attendance
2.  Review work from last week: programming CSV parsers without CSV module
3.  JSON, XML, and serial binary format notes
4.  JSON parsing simple examples: opening and printing the  [Capital projects in PGH](https://data.wprdc.org/dataset/capital-projects)
5.  Mini task 1:  Use a for loop to list all project info in a neatly formed set, like shown in the screen shot below:
6.  Mini task 2:  Write a method called  logMalformedProject  that is called each time a project is visited by the main loop that does not contain a value for the key 'area'. This method should write the project id to a single line in a log file with an appropriate name.
7.  Mini task 3:  Create a method that assembles a list of unique values for the project area. If you are feeling ambitious, do the same for 'status' and 'asset type' since this will come in handy during the search specification.

#### Screen shot of capital project print formatting

![capital project analysis output](https://technologyrediscovery.net/term/fa18/cit129/img/capitalProjectOutput.png)

----------

Write python code that conforms to the following specs:

### purpose

Implement search criteria defined in the JSON format for searching for capital projects in PGH dataset, outputting resulting projects into a file in JSON format

### Unified JSON-encoded search criteria:

{"fiscal_year": [-1], "start_date": [""], "area": [""], "asset_type": [""], "planning_status": [""]}

#### Search Notes:

-   For dates: We will throw out malformed dates that are not YYYY-MM-DD(This requirement was removed due to lack of connecetion to the primary data set)
-   A blank value in any specified query for a column/field will disqualify that record from inclusion in the results
-   Empty string: do not limit results by this criteria at all
-   Note: the "planning_status" key in the search JSON corresponds to the field named "status" in the csv

### program requirement 1: searching

Write code that can read in a search criterion JSON file of your specification. You'll need to be prepared to share this specification with others in the class

Allow the user to specify search criteria for project fiscal year, start date, area, asset_type, and planning status

### program requirement 2: management costs

Write a method that will calculate total project management costs for all the capital projects in Pittsburgh given a management cost scheme, encoded in JSON as specified by the class. Example: For all projects up to $10k, management costs are 8% of the total project budget. For projects between $10k and $100k, management costs drop to 5%, and over $100k, costs increase to 11%.

### _send_Products

1.  Working code from mini-tasks 1,2, and 3
2.  A solid attempt at the full project specs in the green box
3.  A possible API source for the week after next

### _cake_Extension exercises

We can turn python objects into JSON files easily that can be digested by servers all over the world. We can also turn python objects into files that can only be eaten by other python interpreters. The library for this is called pickle. Try serializing (turning a python object into data inside a file, instead of in RAM) your project objects and resurrecting them using the  [pickle library.](https://docs.python.org/2/library/pickle.html#module-pickle)

#### 311 Data Parsing challenge:

1.  Visit the  [WPRDC 311 data home](https://data.wprdc.org/dataset/311-data)  page at the WPRDC. Study the data dictionary. Learn about the 311 program if you don't about their system.
2.  Extract a research question about the data that can be answered by processing the 300,000+ entries in their central data. Examples include:

-   Budgets cuts are coming! Which public works district seems to have the lightest load of 311 requests? The Heaviest? How would you redirect resources between districts?
-   Which submission mechanism is used most for which types of complaints?
-   Which neighborhood receives the most requests? Can we make any inferences between number of requests and the quality of life in that neighborhood?

4.  Write a program in python to answer these questions by ingesting the entire set of 311 data posted to the WPRDC. HINT: Start with a small subset of the data, like  [this random extraction of a few dozen](https://technologyrediscovery.net/python/pgh311Abbrev.csv)  rows.
5.  Come prepared to share your results!