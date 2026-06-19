from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("CRM Campaign Lakehouse")
    .master("local[*]")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")