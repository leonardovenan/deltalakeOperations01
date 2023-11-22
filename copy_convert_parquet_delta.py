from delta.tables import DeltaTable

df = spark.sql("select * from temp_tb_df_trusted")

(df
    .write
    .format("parquet")
    .mode("overWrite")
    .save("/mnt/DATALAKE/stage/your_table/")
)

deltaTable = DeltaTable.convertToDelta(spark, "parquet.`/mnt/DATALAKE/stage/your_table/`")

# testing if the convertion was successfuly
spark.sql("create table dbtrusted.dev_tb_adjust_metrics_melt using delta location '/mnt/DATALAKE/stage/your_table/'")
spark.sql("describe history delta.`/mnt/DATALAKE/stage/your_table/`")
