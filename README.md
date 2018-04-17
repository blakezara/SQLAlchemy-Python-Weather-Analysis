# Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii! To help with your trip planning, you decided to do some climate analysis on the area. Because you are such an awesome person, you have decided to share your ninja analytical skills with the community by providing a climate analysis api. The following outlines what you need to do.


Step 1 - Data Engineering

The climate data for Hawaii is provided through two CSV files. Start by using Python and Pandas to inspect the content of these files and clean the data.


Create a Jupyter Notebook file called data_engineering.ipynb and use this to complete all of your Data Engineering tasks.
Use Pandas to read in the measurement and station CSV files as DataFrames.
Inspect the data for NaNs and missing values. You must decide what to do with this data.
Save your cleaned CSV files with the prefix clean_.

Step 2 - Database Engineering

Use SQLAlchemy to model your table schemas and create a sqlite database for your tables. You will need one table for measurements and one for stations.


Create a Jupyter Notebook called database_engineering.ipynb and use this to complete all of your Database Engineering work.
Use Pandas to read your cleaned measurements and stations CSV data.
Use the engine and connection string to create a database called hawaii.sqlite.

Use declarative_base and create ORM classes for each table.


You will need a class for Measurement and for Station.
Make sure to define your primary keys.


Once you have your ORM classes defined, create the tables in the database using create_all.

Step 3 - Climate Analysis and Exploration

You are now ready to use Python and SQLAlchemy to do basic climate analysis and data exploration on your new weather station tables. All of the following analysis should be completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.


Create a Jupyter Notebook file called climate_analysis.ipynb and use it to complete your climate analysis and data exporation.
Choose a start date and end date for your trip. Make sure that your vacation range is approximately 3-15 days total.
Use SQLAlchemy create_engine to connect to your sqlite database.
Use SQLAlchemy automap_base() to reflect your tables into classes and save a reference to those classes called Station and Measurement.

Step 4 - Climate App

Now that you have completed your initial analysis, design a Flask api based on the queries that you have just developed.


Use FLASK to create your routes.
