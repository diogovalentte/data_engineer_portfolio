# Project: Covid Daily Update
OBJETIVO: Criar duas tabelas no Banco de Dados "Covid_Daily_Update" no SGDB Postgres e então popular essas tabelas com dados diários do Covid-19 no Brazil e seus estados. A tabela "covid_brazil" contém dados diários do Covid no Brazil, enquanto a tabela "covid_states" contém dados diários do Covid para cada estado brasileiro.

Primeiro o Banco de dados e suas duas tabelas são criados, então várias requisições são feitas na API [covid-api](http://covid-api.com/api/) para adquirir os dados, então esses dados diários são inseridos nas tabelas.
 
 # Abaixo uma demonstração das tabelas.

#### "covid_brazil": Dados diários do Covid no Brasil.

| date       | confirmed_accumulated                 | confirmated_difference                                 | deaths_accumulated                     | deaths_difference                                       | last_update       |
|------------|---------------------------------------|--------------------------------------------------------|----------------------------------------|---------------------------------------------------------|-------------------|
| Data | Número acumulativo de casos confimados | Diferença de casos confimados do dia anterior para atual | Número acumulativo de mortes confimadas | Diferença de mortes confimadas do dia anterior para o atual | Data da última atualização |

#### "covid_states": Dados diários do Covid em cada estado brasileiro.

| state  | date       | confirmed_accumulated                 | confirmated_difference                                 | deaths_accumulated                     | deaths_difference                                       | last_update       |
|--------|------------|---------------------------------------|--------------------------------------------------------|----------------------------------------|---------------------------------------------------------|-------------------|
| Estado | Data | Número acumulativo de casos confimados | Diferença de casos confimados do dia anterior para atual | Número acumulativo de mortes confimadas | Diferença de mortes confimadas do dia anterior para o atual | Data da última atualização |
---
### Arquivos importantes>
O arquivo "run.sh" configura o ambiente dentro dos containers.

---
O arquivo "run.py" cria as tabelas do Banco de dados, após isso faz várias requisições da API e adiciona esses dados diários do Covid até o dia anterior a execução do arquivo dentro das tabelas.

---
O arquivo "dag.py" contém as configurações da DAG do Airflow, assim diariamente serão feitas requisições na API para adicionar dados do Covid do dia anterior.

---
# Como utilizar esse projeto:

##### Pré requisitos: Ter o [Docker](https://www.docker.com) e [Docker Compose](https://docs.docker.com/compose/install/#install-compose) instalados. A imagem original docker está disponivel aqui [here](https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml)

---
1º Execute o comando abaixo dentro da pasta "covid_daily_update". Esse comando cria váriaveis de ambiente úteis na execução dos serviços:

    ```sh
    echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
    ```

---
2. Execute o comando abaixo dentro da pasta "covid_daily_update". Esse comando cria os containers (serviços) necessários para utilização do projeto:
- Os serviços serão executados em segundo plano. O serviço do Airflow está disponivel na porta 8080, e o serviço do Postgres na porta 5434. (Os usuários e senhas dos serviços são "airflow")

    ```sh
    sudo docker-compose up -d
    ```
- Espere um minuto até que os serviços tenham sidos iniciados totalmente para continuar.

---
3. Dentro da pasta "covid_daily_update" execute o arquivo "run.sh" através do comando abaixo:
    ###### WARNING: Execute esse comando apenas uma ves, mesmo que os serviçoes parem em algum momento.

- Esse script instala o gerenciador de pacotes Python, "pip", além das bibliotecas Python necessárias no "requiriments.txt".
- Por fim o script despausa a DAG "daily_update_covid_tables".

    ```sh
    bash run.sh
    ```
---
4. Execute o seguinte comando:
    
- Esse script cria as tabelas do banco de dados e insere os dados diários do Covid nelas.

    ```sh
    sudo docker exec covid_daily_update_airflow-webserver_1 python3 /opt/airflow/project/run.py
    ```

---
5. Agora os dados serão inseridos nas tabelas e os serviços do Airflow e Postgres serão executados em segundo plano, então diariamente as 13:01 UTC, dados do Covid do dia anterior serão adicionados nas tabelas
- Se prefirir, acesse no navegador o link "localhost:8080" para acessar a interface do Airflow, tanto o usuário quanto a senha são "airflow".
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
