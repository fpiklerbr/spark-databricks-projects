from pyspark.sql.types import StructType,StructField, StringType, IntegerType,DateType,FloatType,DoubleType

schema1 = StructType([
    StructField('Education_Level',StringType()),
    StructField('Line_Number',IntegerType()),
    StructField('Employed',IntegerType()),
    StructField('Unemployed',IntegerType()),
    StructField('Industry',StringType()),
    StructField('Gender',StringType()),
    StructField('Date_Inserted',StringType()),
    StructField('dense_rank',IntegerType()),
    StructField('Max_Salary_USD',IntegerType())
])


# COMMAND ----------

df_moreCols = (spark.read.format('csv')
                        .schema(schema1)
                        .option('header','true')
                        .load(f'{source}/SchemaEvol/SchemaMoreCols.csv'))

# COMMAND ----------

df_moreCols.printSchema()

# COMMAND ----------

df_moreCols.write.format('delta').mode('append').saveAsTable('`delta`.deltaspark')

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Source with Less Columns

# COMMAND ----------


from pyspark.sql.types import StructType,StructField, StringType, IntegerType,DateType,FloatType,DoubleType

schema = StructType([
    StructField('Education_Level',StringType()),
    StructField('Line_Number',IntegerType()),
    StructField('Employed',IntegerType()),
    StructField('Unemployed',IntegerType()),
    StructField('Industry',StringType()),
    StructField('Gender',StringType())
])

# COMMAND ----------

df_lessCols = (spark.read.format('csv')
                        .schema(schema)
                        .option('header','true')
                        .load(f'{source}/SchemaEvol/SchemaLessCols.csv'))

# COMMAND ----------

df_lessCols.write.format('delta').mode('append').saveAsTable('`delta`.deltaspark')

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM `delta`.deltaspark

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Source data with different data type

# COMMAND ----------

df_diff = (spark.read.format('csv')
            .option('header','true')
            .load(f'{source}/files/*.csv'))

# COMMAND ----------

df_diff.write.format('delta').mode('append').saveAsTable('`delta`.deltaspark')

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC #Schema Evolution

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Allow changes for extra cols

# COMMAND ----------

df_moreCols.write.format('delta').mode('append').option('mergeSchema','True').saveAsTable('`delta`.deltaspark')

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM `delta`.deltaspark

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Allow different schema to evolve
# MAGIC

# COMMAND ----------

df_diff.write.format('delta').mode('overwrite').option('overwriteSchema','True').saveAsTable('`delta`.deltaspark')

# COMMAND ----------
