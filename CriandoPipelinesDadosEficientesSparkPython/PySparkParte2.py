
# Path - dataset1
path_dataset1 = "/FileStore/tables/country_vaccinations.csv"
 
# Path - RDD
path_rdd = "/FileStore/tables/arquivo_rdd.txt"
# Leitura de Dataframe
 
## Opção 1
df1 = spark.read.format("csv").option("header","true").option("inferSchema","false").load(path_dataset1)
 
## Opção 2
# df1 = spark.read.csv(path_dataset1)
# df1 = spark.read.option("header","true").option("inferSchema","true").csv(path_dataset1)
 
## Exibindo dataframe
df1.show(2)
#df1.dtypes
+---------+--------+----------+------------------+-----------------+-----------------------+----------------------+------------------+------------------------------+-----------------------------+-----------------------------------+------------------------------+---------+------------------+--------------------+
|  country|iso_code|      date|total_vaccinations|people_vaccinated|people_fully_vaccinated|daily_vaccinations_raw|daily_vaccinations|total_vaccinations_per_hundred|people_vaccinated_per_hundred|people_fully_vaccinated_per_hundred|daily_vaccinations_per_million| vaccines|       source_name|      source_website|
+---------+--------+----------+------------------+-----------------+-----------------------+----------------------+------------------+------------------------------+-----------------------------+-----------------------------------+------------------------------+---------+------------------+--------------------+
|Argentina|     ARG|2020-12-29|             700.0|             null|                   null|                  null|              null|                           0.0|                         null|                               null|                          null|Sputnik V|Ministry of Health|http://datos.salu...|
|Argentina|     ARG|2020-12-30|              null|             null|                   null|                  null|           15656.0|                          null|                         null|                               null|                         346.0|Sputnik V|Ministry of Health|http://datos.salu...|
+---------+--------+----------+------------------+-----------------+-----------------------+----------------------+------------------+------------------------------+-----------------------------+-----------------------------------+------------------------------+---------+------------------+--------------------+
only showing top 2 rows

df1.take(1)[0]
Out[18]: Row(country='Argentina', iso_code='ARG', date='2020-12-29', total_vaccinations='700.0', people_vaccinated=None, people_fully_vaccinated=None, daily_vaccinations_raw=None, daily_vaccinations=None, total_vaccinations_per_hundred='0.0', people_vaccinated_per_hundred=None, people_fully_vaccinated_per_hundred=None, daily_vaccinations_per_million=None, vaccines='Sputnik V', source_name='Ministry of Health', source_website='http://datos.salud.gob.ar/dataset/vacunas-contra-covid-19-dosis-aplicadas-en-la-republica-argentina')
df1.write.format("parquet").mode("overwrite").save("/FileStore/tables/RAW_ZONE_PARQUET/")
df1.take(3)
Out[115]: [Row(country='Argentina', iso_code='ARG', date='2020-12-29', total_vaccinations='700.0', people_vaccinated=None, people_fully_vaccinated=None, daily_vaccinations_raw=None, daily_vaccinations=None, total_vaccinations_per_hundred='0.0', people_vaccinated_per_hundred=None, people_fully_vaccinated_per_hundred=None, daily_vaccinations_per_million=None, vaccines='Sputnik V', source_name='Ministry of Health', source_website='http://datos.salud.gob.ar/dataset/vacunas-contra-covid-19-dosis-aplicadas-en-la-republica-argentina'),
 Row(country='Argentina', iso_code='ARG', date='2020-12-30', total_vaccinations=None, people_vaccinated=None, people_fully_vaccinated=None, daily_vaccinations_raw=None, daily_vaccinations='15656.0', total_vaccinations_per_hundred=None, people_vaccinated_per_hundred=None, people_fully_vaccinated_per_hundred=None, daily_vaccinations_per_million='346.0', vaccines='Sputnik V', source_name='Ministry of Health', source_website='http://datos.salud.gob.ar/dataset/vacunas-contra-covid-19-dosis-aplicadas-en-la-republica-argentina'),
 Row(country='Argentina', iso_code='ARG', date='2020-12-31', total_vaccinations='32013.0', people_vaccinated=None, people_fully_vaccinated=None, daily_vaccinations_raw=None, daily_vaccinations='15656.0', total_vaccinations_per_hundred='0.07', people_vaccinated_per_hundred=None, people_fully_vaccinated_per_hundred=None, daily_vaccinations_per_million='346.0', vaccines='Sputnik V', source_name='Ministry of Health', source_website='http://datos.salud.gob.ar/dataset/vacunas-contra-covid-19-dosis-aplicadas-en-la-republica-argentina')]
## Outras formas de leitura de arquivos com PySpark
 
path = "/../../arquivoXPTO"
 
# Criando um dataframe a partir de um JSON
dataframe = spark.read.json(path)
 
# Criando um dataframe a partir de um ORC
dataframe = spark.read.orc(path)
 
# Criando um dataframe a partir de um PARQUET
dataframe = spark.read.parquet(path)
## Imprimindo tipos de campos
 
df1.dtypes
#df1.printSchema
Out[30]: [('country', 'string'),
 ('iso_code', 'string'),
 ('date', 'string'),
 ('total_vaccinations', 'double'),
 ('people_vaccinated', 'double'),
 ('people_fully_vaccinated', 'double'),
 ('daily_vaccinations_raw', 'double'),
 ('daily_vaccinations', 'double'),
 ('total_vaccinations_per_hundred', 'double'),
 ('people_vaccinated_per_hundred', 'double'),
 ('people_fully_vaccinated_per_hundred', 'double'),
 ('daily_vaccinations_per_million', 'double'),
 ('vaccines', 'string'),
 ('source_name', 'string'),
 ('source_website', 'string')]
# Leitura de um RDD
 
rdd = sc.textFile(path_rdd)
#rdd.show() = Errado, não é possível exibir um SHOW() de um RDD, somente um Dataframe
rdd.collect()
Out[24]: ['XXXXXcerveja8.99XXXbohemialata',
 'refrigerante6.50XXcocacolalata',
 'XXXXXXXXaguaXX20bonafontegalao']
dfff = spark.read.format("csv").load(path_rdd)
display(dfff)
 
_c0
1
2
3
XXXXXcerveja8.99XXXbohemialata
refrigerante6.50XXcocacolalata
XXXXXXXXaguaXX20bonafontegalao
Showing all 3 rows.

# Criando uma tabela temporária
nome_tabela_temporiaria = "tempTableTerere"
df1.createOrReplaceTempView(nome_tabela_temporiaria)
# Lendo a tabela temporaria opcao 1
spark.read.table(nome_tabela_temporiaria).show()
+---------+--------+----------+------------------+-----------------+-----------------------+----------------------+------------------+------------------------------+-----------------------------+-----------------------------------+------------------------------+---------+------------------+--------------------+
|  country|iso_code|      date|total_vaccinations|people_vaccinated|people_fully_vaccinated|daily_vaccinations_raw|daily_vaccinations|total_vaccinations_per_hundred|people_vaccinated_per_hundred|people_fully_vaccinated_per_hundred|daily_vaccinations_per_million| vaccines|       source_name|      source_website|
+---------+--------+----------+------------------+-----------------+-----------------------+----------------------+------------------+------------------------------+-----------------------------+-----------------------------------+------------------------------+---------+------------------+--------------------+
|Argentina|     ARG|2020-12-29|             700.0|             null|                   null|                  null|              null|                           0.0|                         null|                               null|                          null|Sputnik V|Ministry of Health|http://datos.salu...|
|Argentina|     ARG|2020-12-30|              null|             null|                   null|                  null|           15656.0|                          null|                         null|                               null|                         346.0|Sputnik V|Ministry of Health|http://datos.salu...|
|Argentina|     ARG|2020-12-31|           32013.0|             null|                   null|                  null|           15656.0|                          0.07|                         null|                               null|                         346.0|Sputnik V|Ministry of Health|http://datos.salu...|
|Argentina|     ARG|2021-01-01|              null|             null|                   null|                  null|           11070.0|                          null|                         null|                               null|                         245.0|Sputnik V|Ministry of Health|http://datos.salu...|
|Argentina|     ARG|2021-01-02|              null|             null|                   null|                  null|            8776.0|                          null|                         null|                               null|                         194.0|Sputnik V|Ministry of Health|http://datos.salu...|
|Argentina|     ARG|2021-01-03|              null|             null|                   null|                  null|            7400.0|                          null|                         null|                               null|                         164.0|Sputnik V|Ministry of Health|http://datos.salu...|
|Argentina|     ARG|2021-01-04|           39599.0|             null|                   null|                  null|            6483.0|                          0.09|                         null|                               null|                         143.0|Sputnik V|Ministry of Health|http://datos.salu...|
|Argentina|     ARG|2021-01-05|              null|             null|                   null|                  null|            7984.0|                          null|                         null|                               null|                         177.0|Sputnik V|Ministry of Health|http://datos.salu...|
|Argentina|     ARG|2021-01-06|              null|             null|                   null|                  null|            8173.0|                          null|                         null|                               null|                         181.0|Sputnik V|Ministry of Health|http://datos.salu...|
|Argentina|     ARG|2021-01-07|              null|             null|                   null|                  null|            8363.0|                          null|                         null|                               null|                         185.0|Sputnik V|Ministry of Health|http://datos.salu...|
|Argentina|     ARG|2021-01-08|          107542.0|             null|                   null|                  null|           10519.0|                          0.24|                         null|                               null|                         233.0|Sputnik V|Ministry of Health|http://datos.salu...|
|Argentina|     ARG|2021-01-09|              null|             null|                   null|                  null|           11942.0|                          null|                         null|                               null|                         264.0|Sputnik V|Ministry of Health|http://datos.salu...|
|Argentina|     ARG|2021-01-10|              null|             null|                   null|                  null|           13365.0|                          null|                         null|                               null|                         296.0|Sputnik V|Ministry of Health|http://datos.salu...|
|Argentina|     ARG|2021-01-11|              null|             null|                   null|                  null|           14788.0|                          null|                         null|                               null|                         327.0|Sputnik V|Ministry of Health|http://datos.salu...|
|Argentina|     ARG|2021-01-12|              null|             null|                   null|                  null|           14056.0|                          null|                         null|                               null|                         311.0|Sputnik V|Ministry of Health|http://datos.salu...|
|Argentina|     ARG|2021-01-13|          166833.0|             null|                   null|                  null|           13323.0|                          0.37|                         null|                               null|                         295.0|Sputnik V|Ministry of Health|http://datos.salu...|
|Argentina|     ARG|2021-01-14|              null|             null|                   null|                  null|           13320.0|                          null|                         null|                               null|                         295.0|Sputnik V|Ministry of Health|http://datos.salu...|
|Argentina|     ARG|2021-01-15|          200759.0|             null|                   null|                  null|           13317.0|                          0.44|                         null|                               null|                         295.0|Sputnik V|Ministry of Health|http://datos.salu...|
|Argentina|     ARG|2021-01-16|              null|             null|                   null|                  null|           12971.0|                          null|                         null|                               null|                         287.0|Sputnik V|Ministry of Health|http://datos.salu...|
|Argentina|     ARG|2021-01-17|              null|             null|                   null|                  null|           12624.0|                          null|                         null|                               null|                         279.0|Sputnik V|Ministry of Health|http://datos.salu...|
+---------+--------+----------+------------------+-----------------+-----------------------+----------------------+------------------+------------------------------+-----------------------------+-----------------------------------+------------------------------+---------+------------------+--------------------+
only showing top 20 rows

dfterere = spark.sql("SELECT count(*) tt, country FROM tempTableTerere Group By country")
dfterere.dtypes
Out[125]: [('tt', 'bigint'), ('country', 'string')]
# Visualização do Databricks
display(spark.sql("SELECT * FROM tempTableDataFrame1"))
 
country
iso_code
date
total_vaccinations
people_vaccinated
people_fully_vaccinated
daily_vaccinations_raw
daily_vaccinations
total_vaccinations_per_hundred
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
Argentina
ARG
2020-12-29
700
null
null
null
null
0
Argentina
ARG
2020-12-30
null
null
null
null
15656
null
Argentina
ARG
2020-12-31
32013
null
null
null
15656
0.07
Argentina
ARG
2021-01-01
null
null
null
null
11070
null
Argentina
ARG
2021-01-02
null
null
null
null
8776
null
Argentina
ARG
2021-01-03
null
null
null
null
7400
null
Argentina
ARG
2021-01-04
39599
null
null
null
6483
0.09
Argentina
ARG
2021-01-05
null
null
null
null
7984
null
Argentina
ARG
2021-01-06
null
null
null
null
8173
null
Argentina
ARG
2021-01-07
null
null
null
null
8363
null
Argentina
ARG
2021-01-08
107542
null
null
null
10519
0.24
Argentina
ARG
2021-01-09
null
null
null
null
11942
null
Argentina
ARG
2021-01-10
null
null
null
null
13365
null
Argentina
ARG
2021-01-11
null
null
null
null
14788
null
Argentina
ARG
2021-01-12
null
null
null
null
14056
null
Argentina
ARG
2021-01-13
166833
null
null
null
13323
0.37
Argentina
ARG
2021-01-14
null
null
null
null
13320
null
Showing the first 1000 rows.

# Scala
#import org.apache.spark.sql.functions._
 
# Python
from pyspark.sql.functions import col, column
 
# Usando function col ou column
df1.select(col("country"), col("date"), column("iso_code")).show()
+---------+----------+--------+
|  country|      date|iso_code|
+---------+----------+--------+
|Argentina|2020-12-29|     ARG|
|Argentina|2020-12-30|     ARG|
|Argentina|2020-12-31|     ARG|
|Argentina|2021-01-01|     ARG|
|Argentina|2021-01-02|     ARG|
|Argentina|2021-01-03|     ARG|
|Argentina|2021-01-04|     ARG|
|Argentina|2021-01-05|     ARG|
|Argentina|2021-01-06|     ARG|
|Argentina|2021-01-07|     ARG|
|Argentina|2021-01-08|     ARG|
|Argentina|2021-01-09|     ARG|
|Argentina|2021-01-10|     ARG|
|Argentina|2021-01-11|     ARG|
|Argentina|2021-01-12|     ARG|
|Argentina|2021-01-13|     ARG|
|Argentina|2021-01-14|     ARG|
|Argentina|2021-01-15|     ARG|
|Argentina|2021-01-16|     ARG|
|Argentina|2021-01-17|     ARG|
+---------+----------+--------+
only showing top 20 rows

df1.selectExpr("country", "date", "iso_code").show()
+---------+----------+--------+
|  country|      date|iso_code|
+---------+----------+--------+
|Argentina|2020-12-29|     ARG|
|Argentina|2020-12-30|     ARG|
|Argentina|2020-12-31|     ARG|
|Argentina|2021-01-01|     ARG|
|Argentina|2021-01-02|     ARG|
|Argentina|2021-01-03|     ARG|
|Argentina|2021-01-04|     ARG|
|Argentina|2021-01-05|     ARG|
|Argentina|2021-01-06|     ARG|
|Argentina|2021-01-07|     ARG|
|Argentina|2021-01-08|     ARG|
|Argentina|2021-01-09|     ARG|
|Argentina|2021-01-10|     ARG|
|Argentina|2021-01-11|     ARG|
|Argentina|2021-01-12|     ARG|
|Argentina|2021-01-13|     ARG|
|Argentina|2021-01-14|     ARG|
|Argentina|2021-01-15|     ARG|
|Argentina|2021-01-16|     ARG|
|Argentina|2021-01-17|     ARG|
+---------+----------+--------+
only showing top 20 rows

# Scala import
# org.apache.spark.sql.types._
 
# Criando um Schema manualmente no PySpark
from pyspark.sql.types import *
 
dataframe_ficticio = StructType([
                      StructField("col_String_1", StringType()),
                      StructField("col_Integer_2", IntegerType()),
                      StructField("col_Decimal_3", DecimalType())
                              ])
dataframe_ficticio
Out[2]: StructType(List(StructField(col_String_1,StringType,true),StructField(col_Integer_2,IntegerType,true),StructField(col_Decimal_3,DecimalType(10,0),true)))
# Função para gerar Schema (campos/colunas/nomes de colunas)
 
'''
# Scala
 
org.apache.spark.sql.types._
 
def getSchema(fields : Array[StructField]) : StructType = {
  new StructType(fields)
}
'''
 
# PySpark
def getSchema(fields):
  return StructType(fields)
  
schema = getSchema([StructField("coluna1", StringType()), StructField("coluna2", StringType()), StructField("coluna3", StringType())])
schema
Out[4]: StructType(List(StructField(coluna1,StringType,true),StructField(coluna2,StringType,true),StructField(coluna3,StringType,true)))
# Gravando um novo CSV
 
path_destino="/FileStore/tables/CSV/"
nome_arquivo="arquivo.csv"
path_geral= path_destino + nome_arquivo
df1.write.format("csv").mode("overwrite").option("sep", "\t").save(path_geral)
# Gravando um novo JSON
 
path_destino="/FileStore/tables/JSON/"
nome_arquivo="arquivo.json"
path_geral= path_destino + nome_arquivo
df1.write.format("json").mode("overwrite").save(path_geral)
# Gravando um novo PARQUET
 
path_destino="/FileStore/tables/PARQUET/"
nome_arquivo="arquivo.parquet"
path_geral= path_destino + nome_arquivo
df1.write.format("parquet").mode("overwrite").save(path_geral)
# Gravando um novo ORC
 
path_destino="/FileStore/tables/ORC/"
nome_arquivo="arquivo.orc"
path_geral= path_destino + nome_arquivo
df1.write.format("orc").mode("overwrite").save(path_geral)
# Outros tipos de SELECT
 
#Diferentes formas de selecionar uma coluna
 
from pyspark.sql.functions import *
 
df1.select("country").show(5)
df1.select('country').show(5)
df1.select(col("country")).show(5)
df1.select(column("country")).show(5)
df1.select(expr("country")).show(5)
 
+---------+
|  country|
+---------+
|Argentina|
|Argentina|
|Argentina|
|Argentina|
|Argentina|
+---------+
only showing top 5 rows

# Define uma nova coluna com um valor constante
df2 = df1.withColumn("nova_coluna", lit(1))
#display(df1)
#display(df2)
 
# Adicionar coluna
teste = expr("total_vaccinations < 40")
#df1.select("country", "total_vaccinations").withColumn("teste", teste).show(5)
 
 
# Renomear uma coluna
df1.select(expr("total_vaccinations as total_de_vacinados")).show(5)
df1.select(col("country").alias("pais")).show(5)
df1.select("country").withColumnRenamed("country", "pais").show(5)
 
# Remover uma coluna
df3 = df1.drop("country")
df3.columns
 
+---------+------------------+-----+
|  country|total_vaccinations|teste|
+---------+------------------+-----+
|Argentina|             700.0|false|
|Argentina|              null| null|
|Argentina|           32013.0|false|
|Argentina|              null| null|
|Argentina|              null| null|
+---------+------------------+-----+
only showing top 5 rows

Out[129]: '\n# Renomear uma coluna\ndf1.select(expr("total_vaccinations as total_de_vacinados")).show(5)\ndf1.select(col("country").alias("pais")).show(5)\ndf1.select("country").withColumnRenamed("country", "pais").show(5)\n\n# Remover uma coluna\ndf3 = df1.drop("country")\ndf3.columns\n'
# Filtrando dados e ordenando
# where() é um alias para filter().
 
# Seleciona apenas os primeiros registros da coluna "total_vaccinations"
df1.filter(df1.total_vaccinations > 55).orderBy(df1.total_vaccinations).show(2)
 
# Filtra por país igual Argentina
df1.select(df1.total_vaccinations, df1.country).filter(df1.country == "Argentina").show(5)
 
# Filtra por país diferente Argentina
df1.select(df1.total_vaccinations, df1.country).where(df1.country != "Argentina").show(5) # python type
 
# Mostra valores únicos
df1.select("country").distinct().show()
 
# Especificando vários filtros em comando separados
filtro_vacinas = df1.total_vaccinations < 100
filtro_pais = df1.country.contains("Argentina")
df1.select(df1.total_vaccinations, df1.country, df1.vaccines).where(df1.vaccines.isin("Sputnik V", "Sinovac")).filter(filtro_vacinas).show(5)
df1.select(df1.total_vaccinations, df1.country, df1.vaccines).where(df1.vaccines.isin("Sputnik V", "Sinovac")).filter(filtro_vacinas).withColumn("filtro_pais", filtro_pais).show(5)
 
 
+------------+--------+----------+------------------+-----------------+-----------------------+----------------------+------------------+------------------------------+-----------------------------+-----------------------------------+------------------------------+--------------------+--------------------+--------------------+
|     country|iso_code|      date|total_vaccinations|people_vaccinated|people_fully_vaccinated|daily_vaccinations_raw|daily_vaccinations|total_vaccinations_per_hundred|people_vaccinated_per_hundred|people_fully_vaccinated_per_hundred|daily_vaccinations_per_million|            vaccines|         source_name|      source_website|
+------------+--------+----------+------------------+-----------------+-----------------------+----------------------+------------------+------------------------------+-----------------------------+-----------------------------------+------------------------------+--------------------+--------------------+--------------------+
|Saudi Arabia|     SAU|2021-01-06|          100000.0|             null|                   null|                  null|              null|                          0.29|                         null|                               null|                          null|     Pfizer/BioNTech|Saudi Health Council|https://coronamap.sa|
| Netherlands|     NLD|2021-01-20|          100000.0|             null|                   null|                  null|            7571.0|                          0.58|                         null|                               null|                         442.0|Moderna, Pfizer/B...|National Institut...|https://coronadas...|
+------------+--------+----------+------------------+-----------------+-----------------------+----------------------+------------------+------------------------------+-----------------------------+-----------------------------------+------------------------------+--------------------+--------------------+--------------------+
only showing top 2 rows

+------------------+---------+
|total_vaccinations|  country|
+------------------+---------+
|             700.0|Argentina|
|              null|Argentina|
|           32013.0|Argentina|
|              null|Argentina|
|              null|Argentina|
+------------------+---------+
only showing top 5 rows

+------------------+-------+
|total_vaccinations|country|
+------------------+-------+
|           61012.0|Austria|
|           71508.0|Austria|
|           88895.0|Austria|
|          108252.0|Austria|
|          124756.0|Austria|
+------------------+-------+
only showing top 5 rows

+----------+
|   country|
+----------+
|   Germany|
|    France|
| Argentina|
|   Belgium|
|   Ecuador|
|   Finland|
|     China|
|     Chile|
|   Croatia|
|   Czechia|
|   Denmark|
|    Cyprus|
|   Estonia|
|    Canada|
|    Brazil|
|   England|
|  Bulgaria|
|   Austria|
|Costa Rica|
|   Bermuda|
+----------+
only showing top 20 rows

+------------------+---------+--------+
|total_vaccinations|  country|vaccines|
+------------------+---------+--------+
|               0.0|   Brazil| Sinovac|
|               0.0|Indonesia| Sinovac|
|               0.0|   Turkey| Sinovac|
+------------------+---------+--------+

+------------------+---------+--------+-----------+
|total_vaccinations|  country|vaccines|filtro_pais|
+------------------+---------+--------+-----------+
|               0.0|   Brazil| Sinovac|      false|
|               0.0|Indonesia| Sinovac|      false|
|               0.0|   Turkey| Sinovac|      false|
+------------------+---------+--------+-----------+

"""#######################################################################################################################
Convertendo dados
#######################################################################################################################"""
 
df5 = df1.withColumn("PAISSSSS", col("country").cast("string").alias("PAISSSSSSS"))
df5.select(df5.PAISSSSS).show(2)
 
"""#######################################################################################################################
Trabalhando com funções
#######################################################################################################################"""
 
# Usando funções
df1.select(upper(df1.country)).show(3)
df1.select(lower(df1.country)).show(4)
+---------+
| PAISSSSS|
+---------+
|Argentina|
|Argentina|
+---------+
only showing top 2 rows

+--------------+
|upper(country)|
+--------------+
|     ARGENTINA|
|     ARGENTINA|
|     ARGENTINA|
+--------------+
only showing top 3 rows

+--------------+
|lower(country)|
+--------------+
|     argentina|
|     argentina|
|     argentina|
|     argentina|
+--------------+
only showing top 4 rows

# Criando um dataframe genérico
 
d = [{'name': 'Alice', 'age': 1}]
df_A = spark.createDataFrame(d)
df_A.show()
+---+-----+
|age| name|
+---+-----+
|  1|Alice|
+---+-----+

rdd1 = [{"nome": "Marco","idade": 33,"status": 'true'},
{"nome": "Antonio","idade":33,"status": 'true'},
{"nome":"Pereira","idade":33,"status": 'true'},
{"nome":"Helena","idade":30,"status": 'true'},
{"nome":"Fernando","idade":35,"status": 'true'},
{"nome":"Carlos","idade":28,"status": 'true'},
{"nome":"Lisa","idade":26,"status": 'true'},
{"nome":"Candido","idade":75,"status": 'false'},
{"nome":"Vasco","idade":62,"status": 'true'}
]
dff1 = spark.createDataFrame(rdd1)
dff1.show()
 
 
rdd2 = [
{"nome":"Marco","PaisOrigem":"Brasil"},
{"nome":"Helena","PaisOrigem":"Brasil"},
{"nome":"Gabriel","PaisOrigem":"Brasil"},
{"nome":"Vasco","PaisOrigem":"Portugal"},
{"nome":"Medhi","PaisOrigem":"Marocco"}]
 
dff2 = spark.createDataFrame(rdd2)
dff2.show()
 
'''
join_type = "inner"
 
+------+-----+------+------+----------+
|  nome|idade|status|  nome|PaisOrigem|
+------+-----+------+------+----------+
| Vasco|   62|  true| Vasco|  Portugal|
| Marco|   33|  true| Marco|    Brasil|
|Helena|   30|  true|Helena|    Brasil|
+------+-----+------+------+----------+
'''
 
'''val join_type = "left_semi"
 
+------+-----+------+
|  nome|idade|status|
+------+-----+------+
| Vasco|   62|  true|
| Marco|   33|  true|
|Helena|   30|  true|
+------+-----+------+
'''
 
'''val join_type = "right_outer"
 
+------+-----+------+-------+----------+
|  nome|idade|status|   nome|PaisOrigem|
+------+-----+------+-------+----------+
| Vasco|   62|  true|  Vasco|  Portugal|
| Marco|   33|  true|  Marco|    Brasil|
|  null| null|  null|Gabriel|    Brasil|
|Helena|   30|  true| Helena|    Brasil|
|  null| null|  null|  Medhi|   Marocco|
+------+-----+------+-------+----------+
'''
 
'''val join_type = "left_outer"
 
+--------+-----+------+------+----------+
|    nome|idade|status|  nome|PaisOrigem|
+--------+-----+------+------+----------+
| Antonio|   33|  true|  null|      null|
|   Vasco|   62|  true| Vasco|  Portugal|
|   Marco|   33|  true| Marco|    Brasil|
| Pereira|   33|  true|  null|      null|
|  Carlos|   28|  true|  null|      null|
|Fernando|   35|  true|  null|      null|
| Candido|   75| false|  null|      null|
|  Helena|   30|  true|Helena|    Brasil|
|    Lisa|   26|  true|  null|      null|
+--------+-----+------+------+----------+
'''
 
'''join_type = "full_outer"
 
+--------+-----+------+-------+----------+
|    nome|idade|status|   nome|PaisOrigem|
+--------+-----+------+-------+----------+
| Antonio|   33|  true|   null|      null|
|   Vasco|   62|  true|  Vasco|  Portugal|
|   Marco|   33|  true|  Marco|    Brasil|
| Pereira|   33|  true|   null|      null|
|  Carlos|   28|  true|   null|      null|
|    null| null|  null|Gabriel|    Brasil|
|Fernando|   35|  true|   null|      null|
| Candido|   75| false|   null|      null|
|  Helena|   30|  true| Helena|    Brasil|
|    Lisa|   26|  true|   null|      null|
|    null| null|  null|  Medhi|   Marocco|
+--------+-----+------+-------+----------+
'''
 
'''join_type = "left_anti"
 
+--------+-----+------+
|    nome|idade|status|
+--------+-----+------+
| Antonio|   33|  true|
| Pereira|   33|  true|
|  Carlos|   28|  true|
|Fernando|   35|  true|
| Candido|   75| false|
|    Lisa|   26|  true|
+--------+-----+------+
'''
 
join_type = "inner"
join_condition = dff1.nome == dff2.nome
df3 = dff1.join(dff2, join_condition, join_type)
df3.show()
 
#df1.groupBy("status").agg(countDistinct(col("idade"))).show()
+-----+--------+------+
|idade|    nome|status|
+-----+--------+------+
|   33|   Marco|  true|
|   33| Antonio|  true|
|   33| Pereira|  true|
|   30|  Helena|  true|
|   35|Fernando|  true|
|   28|  Carlos|  true|
|   26|    Lisa|  true|
|   75| Candido| false|
|   62|   Vasco|  true|
+-----+--------+------+

+----------+-------+
|PaisOrigem|   nome|
+----------+-------+
|    Brasil|  Marco|
|    Brasil| Helena|
|    Brasil|Gabriel|
|  Portugal|  Vasco|
|   Marocco|  Medhi|
+----------+-------+

+-----+------+------+----------+------+
|idade|  nome|status|PaisOrigem|  nome|
+-----+------+------+----------+------+
|   30|Helena|  true|    Brasil|Helena|
|   33| Marco|  true|    Brasil| Marco|
|   62| Vasco|  true|  Portugal| Vasco|
+-----+------+------+----------+------+

# Path - RDD
path_rdd = "/FileStore/tables/arquivo_rdd.txt"
rdd = sc.textFile(path_rdd)
df_pre = spark.read.text(path_rdd)
from pyspark.sql import functions as f
df_pre
Out[26]: DataFrame[value: string]
x = lambda y : y + 1
x(2
Out[17]: 3
## para TXT's com header
path_rdd = "/FileStore/tables/arquivo_rdd.txt" # especificar o caminho do Bucket
df_pre = spark.read.text(path_rdd)
posicao = ((0,1),(1,5), (5,8))
header= "nome;tipo;texto"
func = lambda p,name,df : df.withColumn(name, df['value'].substr(p[0], p[1]))
def concatenaCampo(posicao, header, df_): 
  i = 0
  header_ = header.split(";")
  for p in posicao:
    df_ = func(p,header_[i],df_)
    print(header_[i])
    i=i+1
  return df_.drop('value')
header.split(";")
Out[93]: ['nome', 'tipo', 'texto']
df_pre.show()
+--------------------+
|               value|
+--------------------+
|XXXXXcerveja8.99X...|
|refrigerante6.50X...|
|XXXXXXXXaguaXX20b...|
+--------------------+

dd = concatenaCampo(posicao, header, df_pre)
nome
tipo
texto
dd.show()
+----+-----+--------+
|nome| tipo|   texto|
+----+-----+--------+
|   X|XXXXX|Xcerveja|
|   r|refri|igerante|
|   X|XXXXX|XXXXagua|
+----+-----+--------+
