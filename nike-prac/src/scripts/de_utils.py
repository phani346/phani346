# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
from pyspark.sql.functions import upper
from pyspark.sql.functions import *
from pyspark.sql.types import *

def convert_to_upper(df, column_name):
    """
    Converts a column to uppercase in a PySpark DataFrame.

    :param df: Input DataFrame
    :param column_name: Column to convert
    :return: Updated DataFrame
    """
    df= df.withColumn(column_name, upper(column_name))
    return df
