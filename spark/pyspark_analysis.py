from pyspark.sql.functions import col
from pyspark.sql import functions as F

df_load = spark.read.format("csv") \
    .option("delimiter", ",") \
    .option("header", "false") \
    .load("s3://mynifioutput3105/1aaa6c26-776d-47ca-b8e3-0f5ced5d8aab.txt")

df_load.show(5)

statistics_df = df_load.select(col("_c4").alias("number_injured")).describe()
statistics_df.show()

borough_freq_df = df_load.select(col("_c10").alias("borough")) \
    .groupBy("borough") \
    .count() \
    .sort("count", ascending=False)

borough_freq_df.show()

paths_df = df_load.select(col("_c3").alias("on_street_name")) \
    .groupBy("on_street_name") \
    .count() \
    .sort("count", ascending=False) \
    .limit(20)

paths_df.show()

notsedan_df = df_load.filter(df_load["_c9"] != "Sedan")

freq_vehicle_df = notsedan_df.select(col("_c9").alias("vehicle_type")) \
    .groupBy("vehicle_type") \
    .count() \
    .sort("count", ascending=False) \
    .limit(5)

freq_vehicle_df.show()

collision_day_df = df_load.select(
    df_load._c0.alias("collision_id"),
    F.dayofmonth("_c1").alias("day")
)

collision_day_df.show(5)

final_df = df_load.select(
    df_load._c0.alias("collision_id"),
    df_load._c1.alias("crash_date"),
    df_load._c2.alias("crash_time"),
    df_load._c10.alias("borough"),
    df_load._c3.alias("on_street_name"),
    df_load._c4.alias("number_of_persons_injured"),
    df_load._c5.alias("number_of_persons_killed"),
    df_load._c9.alias("vehicle_type")
)

final_df.coalesce(1).write.format("csv").save("s3://mynifioutput3105/pyspark_results")
