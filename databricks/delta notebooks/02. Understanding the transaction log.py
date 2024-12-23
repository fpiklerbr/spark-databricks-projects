dbutils.fs.ls(f'{source}/delta/')

# COMMAND ----------

dbutils.fs.ls(f'{source}/delta/_delta_log')

# COMMAND ----------

display(spark.read.format('text').load('abfss://test@deltadbstg.dfs.core.windows.net/delta/_delta_log/00000000000000000000.json'))

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Reading the delta lake file

# COMMAND ----------

df = (spark.read.format('delta')
                .load(f'{source}/delta/'))

# COMMAND ----------

df.printSchema()

# COMMAND ----------

display(df)

# COMMAND ----------

df_delta = df.filter("Education_Level =='High School'")

# COMMAND ----------

df_delta.count()

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Overwriting the same file in delta folder

# COMMAND ----------

(df_delta.write.format('delta')
        .mode('overwrite')
        .save(f'{source}/delta/'))

# COMMAND ----------

display(spark.read.format('text').load('abfss://test@deltadbstg.dfs.core.windows.net/delta/_delta_log/00000000000000000001.json'))

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Reading the overwritten file

# COMMAND ----------

df_overwrite = (spark.read.format('delta')
                .load(f'{source}/delta/'))

# COMMAND ----------

display(df_overwrite)

# COMMAND ----------

