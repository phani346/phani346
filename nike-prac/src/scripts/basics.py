"""Small helper utilities for basic data loading in Spark.

This file was converted from a Databricks notebook JSON export to a
plain Python module so it can be imported without syntax errors in
non-Notebook environments.
"""

def load_student_data(spark, path="/FileStore/tables/StudentData.csv"):
    """Load student data from CSV using the provided Spark session.

    :param spark: SparkSession instance
    :param path: CSV file path
    :return: DataFrame
    """
    df = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load(path)
    df.show()
    return df


if __name__ == "__main__":
    try:
        from pyspark.sql import SparkSession

        spark = SparkSession.builder.getOrCreate()
        load_student_data(spark)
    except Exception as e:
        print("This script requires a Spark session to run interactively:", e)
