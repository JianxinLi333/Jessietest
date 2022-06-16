# Databricks notebook source
my_secret = dbutils.secrets.getBytes(scope="kvtest0324", key="kv57632")
my_secret.decode("utf-8")

# COMMAND ----------

dbutils.fs.mkdirs("dbfs:/init-script/")

# COMMAND ----------

dbutils.fs.rm("dbfs:/init-script/sparkconf.sh")

# COMMAND ----------

dbutils.fs.put("dbfs:/init-script/sparkconf.sh", """
cat << EOF > /databricks/driver/conf/00-custom-spark.conf
[driver] {
    "spark.hadoop.javax.jdo.option.ConnectionURL" = "jdbc:mysql://dbfshivetest.mysql.database.chinacloudapi.cn:3306/hive2?useSSL=true"
    "spark.hadoop.javax.jdo.option.ConnectionUserName" = "jessie@dbfshivetest"
    "spark.hadoop.javax.jdo.option.ConnectionPassword" = "${PASSWORD}"
    "spark.hadoop.javax.jdo.option.ConnectionDriverName" = "org.mariadb.jdbc.Driver"
    "spark.sql.hive.metastore.version" = "2.3.7"
    "spark.sql.hive.metastore.jars" = "builtin"
    "spark.databricks.delta.preview.enabled" = "true"
    "datanucleus.schema.autoCreateTables" = "true"
    "datanucleus.fixedDatastore" = "false"
    }
EOF
""",True)

# COMMAND ----------

# MAGIC %sh
# MAGIC cat /dbfs/init-script/sparkconf.sh

# COMMAND ----------

spark.conf.get("spark.hadoop.javax.jdo.option.ConnectionPassword")

# COMMAND ----------

spark.conf.get("spark.hadoop.javax.jdo.option.ConnectionUserName")

# COMMAND ----------

# MAGIC %sh
# MAGIC cat << EOF > /dbfs/init-script/test.sh 
# MAGIC "spark.hadoop.javax.jdo.option.ConnectionPassword" = "${PASSWORD}"
# MAGIC EOF

# COMMAND ----------

# MAGIC %sh
# MAGIC cat /databricks/driver/conf/00-custom-spark.conf

# COMMAND ----------

# MAGIC %sql
# MAGIC show databases;

# COMMAND ----------

# MAGIC %sql
# MAGIC create database db02;

# COMMAND ----------

# MAGIC %sql
# MAGIC create table db01.t1(id int, details string);

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into db01.t1 values(1,'a'),(2,'b');

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from db01.t1;

# COMMAND ----------

t1 = spark.sql("select * from db01.t1")
display(t1.select("*"))

# COMMAND ----------


