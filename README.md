# tableQA
Tool for querying natural language on tabular data like csvs,excel sheet,etc.   

#### Features    
* Supports detection from multiple csvs 
* Support FuzzyString implementation. i.e, incomplete csv values in query can be automatically detected and filled.
* Open-Domain, No training required.
* Add manual schema for customized experience
* Auto-generate schemas in case schema not provided


### Configuration:
```git clone https://github.com/abhijithneilabraham/tableQA ```  

```cd tableqa```

```pip install -r requirements.txt```

      
## Quickstart


#### Getting an SQL query from csv 

```
from agent import Agent
agent=Agent(data_dir) #specify the data directory.
print(agent.get_response("Your question here")) #returns an sql query
```

#### Do Sample query on sqlite database
```
from database import Database
database=Database(data_dir)
response=database.Query_Sqlite("Your question here")
print("Response ={}".format(response)) #returns the result of the sql query after feeding the csv to the database
```


#### Adding Manual schema

include the directory containing the schemas of the respective csvs, with the same filename. Refer "/cleaned_data"  and "/schema" for examples.

Example:

##### SQL query 
```
from agent import Agent
agent=Agent("cleaned_data","schema") #specify the data and schema directories.
print(agent.get_response("How many people died of stomach cancer in 2011")) 
#sql query: SELECT SUM(Death_Count) FROM cancer_death WHERE Cancer_site = "Stomach" AND Year = "2011" 
```


##### Database query

```
from database import Database
database=Database("cleaned_data","schema")
response=database.Query_Sqlite("how many people died of stomach cancer in 2011")
print("Response ={}".format(response)) #returns the result of the sql query after feeding the csv to the database
#Response =[(22,)]
```

