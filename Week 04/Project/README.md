# Week 04 - Project
## Purpose

Implement search criteria defined in the JSON format for searching for capital projects in PGH dataset, outputting resulting projects into a file in JSON format

## Unified JSON-encoded search criteria:

{"fiscal_year": [-1], "start_date": [""], "area": [""], "asset_type": [""], "planning_status": [""]}

### Search Notes:

-   For dates: We will throw out malformed dates that are not YYYY-MM-DD(This requirement was removed due to lack of connecetion to the primary data set)
-   A blank value in any specified query for a column/field will disqualify that record from inclusion in the results
-   Empty string: do not limit results by this criteria at all
-   Note: the "planning_status" key in the search JSON corresponds to the field named "status" in the csv
---
## program requirement 1: searching

Write code that can read in a search criterion JSON file of your specification. You'll need to be prepared to share this specification with others in the class

Allow the user to specify search criteria for project fiscal year, start date, area, asset_type, and planning status

## program requirement 2: management costs

Write a method that will calculate total project management costs for all the capital projects in Pittsburgh given a management cost scheme, encoded in JSON as specified by the class. Example: For all projects up to $10k, management costs are 8% of the total project budget. For projects between $10k and $100k, management costs drop to 5%, and over $100k, costs increase to 11%.


---
source: [https://technologyrediscovery.net/python/obact.py.dict.html](https://technologyrediscovery.net/python/obact.py.dict.html)