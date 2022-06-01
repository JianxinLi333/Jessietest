# Databricks notebook source
configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": "11ea5abb-a25e-479a-94fc-cc0bfe2e77db",
           "fs.azure.account.oauth2.client.secret": "615GDJ~_zdXvvanM63.6-91GTCoy8H-lns",
           "fs.azure.account.oauth2.client.endpoint": "https://login.partner.microsoftonline.cn/b388b808-0ec9-4a09-a414-a7cbbd8b7e9b/oauth2/token"}

# Optionally, you can add <directory-name> to the source URI of your mount point.
dbutils.fs.mount(
  source = "abfss://input@adlseast2jessie.dfs.core.chinacloudapi.cn/",
  mount_point = "/mnt/adlseast2jessie",
  extra_configs = configs)

# COMMAND ----------

display(dbutils.fs.ls("dbfs:/mnt/adlseast2jessie"))

# COMMAND ----------

dbutils.fs.unmount( "/mnt/adlseast2jessie")

# COMMAND ----------

111
222
