#!/usr/bin/env python
# coding: utf-8

# In[18]:


#Import libraries
import sqlalchemy
import pymysql
from sqlalchemy import create_engine
import pandas as pd


# In[33]:


# creating and initializing a nested list
students = [['jackma', 'Mon', 'Sydeny', 'Australia', 5],
            ['Ritika', 'Tue', 'Delhi', 'India_2', 56],
            ['Vansh', 'Wed', 'Delhi', 'India_3', 87],
            ['Nany', 'Thu', 'Tokyo', 'Japan_2', 87],
            ['May', 'Fri', 'New York', 'US', 76],
            ['Michael', 'Sat', 'las vegas', 'US', 98]]
 
# Create a DataFrame object
df = pd.DataFrame(students,
                  columns=['Name', 'Day', 'City', 'Country', 'Income'],
                  index=['1', '2', '3', '4', '5', '6'])


# In[24]:


#see data frame
df.head(2)


# In[34]:


#connect sql alchemy engine
my_conn = create_engine('mysql+pymysql://root:password@localhost/sales')
print(df.shape)

#load to database EMPDOC is table

    
    
df.to_sql(name='days', con=my_conn, if_exists='append', index=False, dtype=sqlalchemy.types.String(length=255))

#Disable safe object mode for erroe code 1175,  
#Query = SET SQL_SAFE_UPDATES=0;

sql = """
 delete  from days where id not in( select * from(
select max(id) as id from days 
group by `Day`, `Name` having count(`Day`)>1)as t);  
"""

with my_conn.begin() as connection:     
    connection.execute(sql)


