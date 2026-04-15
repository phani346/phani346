# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# MAGIC %run /Workspace/Users/346phani@gmail.com/nike/nike-prac/src/scripts/de_utils

# COMMAND ----------

#testing 

# COMMAND ----------



data =[('ravi',30,'hyd'),('kumar',35,'pune'),('raju',25,'blr'),('suresh',40,'hyd'),('ramesh',20,'blr')]
schema=['name','age','city']
df=spark.createDataFrame(data,schema)
display(df)

# COMMAND ----------

df = df.withColumn(
    "salary",
    when(col("age") >= 35, 70000)
    .when(col("age") >= 30, 50000)
    .otherwise(30000)
)

# COMMAND ----------

df.groupBy("city").agg(
    sum("salary").alias("total_salary"),
    avg("salary").alias("avg_salary")
).show()

# COMMAND ----------


df = convert_to_upper(df, "name")
display(df)

# COMMAND ----------

# MAGIC %pip install pandas

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

dbutils.widgets.text("integration_name", "test")

dbutils.widgets.dropdown(
    "load_type",
    "INCREMENTAL",                # default
    ["FULL", "INCREMENTAL"]       # options
)

integration_name = dbutils.widgets.get("integration_name").strip()
load_type = dbutils.widgets.get("load_type").strip()

print(f"integration_name Arg: {integration_name}")
print(f"load_type Arg: {load_type}")

# COMMAND ----------

spark.conf.set("spark.sql.shuffle.partitions", "200")
spark.conf.set("spark.sql.session.timeZone", "Asia/Kolkata")
