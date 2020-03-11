# Database with Python

## Basic Commands (Python):
- Create a connection to a database
	- connection = sqlite3.connect('your_database.db')
- Create a cursor
	- cursor = connection.cursor()
- Create table with headers
	- cursor.execute("CREATE TABLE table_name(header_1, header_2, header_3)")
- Delete table
	- cursor.execute("DROP TABLE IF EXISTS table_name")


### More Info / Sources:

- https://www.sqlitetutorial.net/
    - sqlite tutorial
- https://likegeeks.com/python-sqlite3-tutorial/
    - python sqlite3 tutorial
- https://docs.python.org/3.9/library/sqlite3.html
    - python documentation for sqlite3
- https://stackoverflow.com/questions/41900593/csv-into-sqlite-table-python/41900956#41900956
    - .csv >> pandas >> sqlite3
- https://data.wprdc.org/datastore/dump/1e9b0886-5756-413a-b35f-89746cf56fd9
    - jail.csv (ACJ Daily Census Data - 06/2019)