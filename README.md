# Python and SQL Portfolio Documentation

Welcome to my Python and SQL portfolio! This repository showcases a collection of examples demonstrating data processing, analysis, and manipulation using Apache Spark, PySpark, and SQL. Each example emphasizes key data engineering and data science concepts. Below is a detailed explanation of the included code and methodologies.

---

## Table of Contents
1. [Python and PySpark: RDD Examples](#python-and-pyspark-rdd-examples)  
2. [Spark SQL: DataFrame and SQL Queries](#spark-sql-dataframe-and-sql-queries)  
3. [Spark Structured Streaming Example](#spark-structured-streaming-example)  
4. [Techniques and Tools](#techniques-and-tools)  
5. [How to Run the Notebooks](#how-to-run-the-notebooks)  

---

## Python and PySpark: RDD Examples
This section explores **Resilient Distributed Datasets (RDDs)** in Spark and demonstrates various transformations and actions.

### Key Sections
- **RDD Creation**  
  - Examples of creating RDDs from local collections and external files.  
  - **Key Insight**: How Spark parallelizes tasks for distributed computation.

- **Transformations**  
  - `map`, `filter`, `flatMap`: Basic data transformations on RDDs.

- **Actions**  
  - `collect`, `count`, `reduce`: Actions that compute results and return values to the driver.

- **Advanced Concepts**  
  - **Partitioning**: How to partition data effectively for performance.  
  - **Key-Value RDDs**: Working with paired data, such as for word counts.

---

## Spark SQL: DataFrame and SQL Queries
This section covers the use of **DataFrames** and **Spark SQL** for structured data processing.

### Key Sections
- **DataFrame Operations**  
  - How to load data into DataFrames and perform transformations.  
  - Key operations include `select`, `filter/where`, and more.

- **SQL Integration**  
  - Writing and executing SQL queries on Spark DataFrames.

- **Performance Optimization**  
  - The **Catalyst Optimizer** and how it automatically optimizes Spark queries.  
  - Reading and writing data in different file formats (CSV, Parquet, JSON, etc.).

---

## Spark Structured Streaming Example
In addition to batch processing with RDDs and DataFrames, this repository also includes an example of **real-time data processing** using Spark Structured Streaming. The streaming code:

- **Monitors** a directory (e.g., `../resources/logs`) for new log files.  
- **Parses** each log line using regular expressions to extract fields such as host, timestamp, request method, and status.  
- **Aggregates** the data by grouping on the HTTP status code and counting occurrences in real-time.  
- **Outputs** the running counts to the console continuously until the stream is terminated.  

This example demonstrates how Spark’s Structured Streaming API can be used to handle continuous data ingestion while applying transformations and aggregations on the fly.

---

## Techniques and Tools
- **Python and PySpark Techniques**  
  - Functional programming with `lambda`, `map`, and `reduce`.  
  - Lazy evaluation: How Spark defers computation until necessary.

- **SQL Techniques**  
  - Writing complex queries involving aggregations, joins, and window functions.

- **Big Data Best Practices**  
  - Using Spark’s lazy execution for performance optimization.  
  - Employing partitioning strategies to efficiently parallelize tasks.

---

## How to Run the Notebooks
### Requirements
- Python 3.x  
- Jupyter Notebook  
- Apache Spark (latest version recommended)  
- `pyspark` library:  
  ```bash
  pip install pyspark
