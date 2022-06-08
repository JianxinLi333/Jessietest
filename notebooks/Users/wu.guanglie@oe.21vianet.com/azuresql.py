# Databricks notebook source
# MAGIC %scala
# MAGIC 
# MAGIC val jdbcHostname = "testdfd.database.chinacloudapi.cn"
# MAGIC val jdbcPort="1433"
# MAGIC val jdbcDatabase = "test"
# MAGIC     
# MAGIC val jdbcUrl = s"jdbc:sqlserver://${jdbcHostname}:${jdbcPort};database=${jdbcDatabase}"
# MAGIC 
# MAGIC val jdbcUsername = "alex"
# MAGIC val jdbcPassword = "123456_qwerT"
# MAGIC 
# MAGIC // Create a Properties() object to hold the parameters.
# MAGIC import java.util.Properties
# MAGIC val connectionProperties = new Properties()
# MAGIC 
# MAGIC connectionProperties.put("user", s"${jdbcUsername}")
# MAGIC connectionProperties.put("password", s"${jdbcPassword}")
# MAGIC 
# MAGIC //df2.write.mode("append").jdbc(url=jdbcUrl,table="student",properties=connectionProperties)
# MAGIC 
# MAGIC val employees_table = spark.read.jdbc(jdbcUrl, "CDS", connectionProperties) 