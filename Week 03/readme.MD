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
