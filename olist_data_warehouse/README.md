### OBJETIVO: Criar um Banco de dados populado com dados de vários arquivos ".csv". Posteriormente copiar os dados significantes do Banco de dados para um Banco de dados com estrutura de Data Warehouse.
---

### Os arquivos ".csv" foram baixados [aqui](https://www.kaggle.com/olistbr/brazilian-ecommerce). São dados contendo informações sobre pedidos, compradores, vendedores, pagamentos e produtos referentes aos serviços da empresa Olist. A imagem abaixo representa as relações entre os dados dos arquuivos .csv e do Banco de Dados "olist_database".

![imageDB](https://i.imgur.com/HRhd2Y0.png)

---
### No problema ficticio de negócio, deveria ser criado um Data Warehouse especifico para responder determinadas perguntas que seriam abordadas semanalmente pelo time de decisões.

1. Média do valor pago em cada metódo de pagamento

2. Média de compradores da cidade de São Paulo e Goiás

3. Mediana de estrelas para cada categoria de produto

4. Média do preço total para cada quantidade de parcelamento do total

5. Média dos 25% maiores valores pagos no boleto

6. Quantidade de vezes que um pedido foi entrega após a data prevista

7. Média de preço para cada catégoria de produto

8. Dia da semana com mais vendas

### Para responder essas perguntas, o seguinte esquema de Data Warehouse foi criado.

![imageDW](https://i.imgur.com/7BkaiJH.png)

---

# Como utilizar esse projeto:

##### Pré requisitos: Ter o [Docker](https://www.docker.com) e [Docker Compose](https://docs.docker.com/compose/install/#install-compose) instalados. A imagem original docker está disponivel aqui [here](https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml)

---
1º Execute o comando abaixo dentro da pasta "olist_data_warehouse". Esse comando criará o container (serviço) do Postgres:
    ```sh
    sudo docker-compose up -d
    ```
- O serviço será executado em segundo plano. 
- O serviço do Postgres pode ser acessado atráves da porta 5434, com o usuário "username", senha "password" e banco de dados "olist_database"

---
2º Execute o comando abaixo dentro da pasta "olist_data_warehouse". Esse comando irá configurar o ambiente dentro do container (serviço) do Postgres.
   ```sh
   docker exec olist_data_warehouse_db_postgres13_1 /bin/bash /project/run.sh
   ```
   
- Atualizará os repositorios do container, instalará o Python, o "pip" e as bibliotecas Python necessárias dentro do container.
- Além disso executará o arquivo "run.py", que criará e adicionará dados dentro das tabelas do Banco de Dados "olist_database" e do Data Warehouse "olist_data_warehouse"
  

---

## Comandos adicionais:

#### Mostrar os serviços (containers) Docker ativos em segundo plano.
```sh
sudo docker ps
```

---
#### Parar os serviços do projeto (Execute dentro da pasta "covid_daily_update").
```sh
sudo docker-compose down
``` 
---
#### Executar um comando dentro do serviço do airflow.
```sh
sudo docker exec covid_daily_update_airflow-webserver_1 <comando>
```

---
#### Mostrar as logs de um serviço (container)
```sh
sudo docker logs <nome do serviço (ver no comando "sudo docker ps")>
```
---
