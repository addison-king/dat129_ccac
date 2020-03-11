# Database with Python

## Basic Commands (Python):
- Create a connection to a database
	- connection = sqlite3.connect('your_database.db')
- Create a cursor
	- cursor = connection.cursor()
- Create table with headers
	- cursor.execute("CREATE TABLE table_name(header_1 type, header_2 type, header_3 type)")
		- 'type' means: NULL, INTEGER, REAL, TEXT, BLOB
- Delete table
	- cursor.execute("DROP TABLE IF EXISTS table_name")
- Insert values into table - Simple, UNSAFE
	- cursor.execute("INSERT INTO table_name(value_1, value_2, value_3)")
		- this will insert 1 row of data
- Insert values into table - More Secure
	- data_values = (value_1, value_2, value_3)
	- cursor.execute("INSERT INTO table_name(header_1, header_2, header_3) VALUES(?, ?, ?)", data_values)
- Insert multiple values into table
	- data_values = [(value_11, value_12, value_13), (value_21, value_22, value_23), (value_31, value_32, value_33)]
	- cursor.executemany("INSERT INTO table_name VALUES(?, ?, ?)", data_values)
- Select data inside the table
	- cursor.execute("SELECT * FROM table_name")
	- cursor.execute("SELECT header_1, header_2 FROM table_name")
- Select modifiers
	WHERE
		- cursor.execute("SELECT * FROM table_name WHERE clause_here")
	GROUP BY
		- cursor.execute("SELECT * FROM table_name GROUP BY clause_here")
	ORDER BY
		- cursor.execute("SELECT * FROM table_name ORDER BY clause_here")
	COUNT()
		- cursor.execute("SELECT header_1, COUNT(header_2) FROM table_name")

## More Info / Sources:

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