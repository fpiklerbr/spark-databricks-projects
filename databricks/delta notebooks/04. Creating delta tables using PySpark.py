df = (spark.read.format('parquet')
                .load(f'{source}/ParquetFolder/'))

# COMMAND ----------

display(df)

# COMMAND ----------

(df.write.format('delta')
        .mode('overwrite')
        .saveAsTable('`delta`.DeltaSpark'))

# COMMAND ----------

dbutils.fs.ls('dbfs:/user/hive/warehouse/delta.db/deltaspark')

# COMMAND ----------

dbutils.fs.ls('dbfs:/user/hive/warehouse/delta.db/deltaspark/_delta_log')

# COMMAND ----------

display(spark.read.format('text').load('dbfs:/user/hive/warehouse/delta.db/deltaspark/_delta_log/00000000000000000000.json'))

# COMMAND ----------

display(spark.read.format('delta').load('dbfs:/user/hive/warehouse/delta.db/deltaspark'))

# COMMAND ----------

