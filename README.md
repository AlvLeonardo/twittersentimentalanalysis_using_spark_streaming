# Twitter sentiment analysis using PySpark

This project comes from the evaluation process of Compass UOL's scholarship program, carried out from October to December 2021

# Project's goal

The project intends to carry out an analysis of sentiments from Tweets obtained from the Twitter platform, with the main focus on the sentiment related to the current president of Brazil, generating a comparison between historical data for the year 2018 and current data for 2021.

# Form of Analysis

For the sentiment analysis, previously defined emojis were used, which aimed to classify the tweets obtained as: positive, negative or neutral. All the
Data processing was done using Azure Databricks notebooks, together with PySpark, both to filter historical data (Batch Layer) and to use the
Spark Streaming to process data from twitter (Speed Layer) in real time. Azure Data Lake Storage Gen2 was used to store all data present in the sentiment analysis process, being
connected to Databricks, using mount point
