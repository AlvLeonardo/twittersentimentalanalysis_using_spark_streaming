# Twitter Sentimental Analysis Usando PySpark

# Objetivo do Projeto

O projeto busca realizer uma análise de sentimentos de Tweets obtidos da plataforma Twitter, tendo como  foco principal o sentimento relacionado com o atual presidente da república, gerando uma comparação entre os dados históricos do ano de 2018 e dados atuais, de 2021.

# Forma de análise

Para análise de sentimentos foram utilizados emojis previamente definidos, os quais tiveram como intuito, classificar os tweets obtidos como: positivo, negativo ou neutro. Todo o 
processamento de dados foi feito utilizando notebooks do Azure Databricks, juntamente com PySpark, tanto para filtar os dados históricos (Batch Layer), quanto para utilizar o
Spark Streaming para processar os dados oriundos do twitter (Speed Layer) em tempo real.
