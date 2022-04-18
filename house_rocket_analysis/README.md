# House Rocket Analysis
Nesse projeto será analisado um conjunto de dados com o objetivo de gerar "insights", responder o problema de negócio proposto pelo CEO ficticio da empresa ficticia "House Rocker", além de responder hipoteses próprias e por fim criar um Web App para que qualquer um possa ver as analises feitas.

#### WARNING: É recomendado ver primeiro os principais "insights" e reportes finais no Web App e por fim analisar os notbooks.

### O conjunto de dados foi pego no site Kaggle, no link [link](https://www.kaggle.com/harlfoxem/housesalesprediction). O conjunto de dados possuí a seguinte descrição:

"This dataset contains home sales prices for King County, which includes Seattle. It includes homes sold between May 2014 and May 2015.
It's a great dataset for evaluating simple regression models. "

## Problema ficticio de negócio:

O CEO da empresa imaginária "House Rocket" trabalha com a compra e revenda de propriedades no estado de Seattle, USA. Esse CEO me contratou para analisar um conjunto de dados com multiplas propriedades disponiveis para compra e responder quatro questões principais:

* 1 - Qual propriedades a House Rocket deveria comprar e por qual preço?

* 2 - Assim que as propriedades estiverem sob posse da House Rocker, por qual preço elas deveria ser vendidas?

* 3 - Qual o melhor momento para revendelas?

* 4 - A House Rocket deveria fazer reformas nessas propriedades para aumentar o preço de revenda? O que a House Rocker deveria reformar nessas propriedades para aumentar o preço de revenda?



---
## Para iniciar o Web App, siga as instruções:

1. Edit the following snippet of the "app.py" file inside the APP folder. Inside it put the path to the project's root folder.

```python
project_path = "Put/here/the/path/to/the/project's/root/folder/house_rocket_analysis"
```

2. Através da linha de comando execute o comando abaxio:
```bash
streamlit run APP/appy.py
```

#### Agora basta abrir o link provido no seu navegador.
---
---
# Notebooks

## Notebook: 1.0-Data_Exploratory

### Nessa seção o conjunto de dados foi explorado com os seguintes objetivos:

1. Identificar valores duplicados ou faltando no conjunto de dados, e se preciso trata-los.
2. Calcular estatísticas descritivas com relação aos dados.
3. Identificar "outliers" no conjunto e trata-los.
4. Explorar a correlação entre o preço das propriedades e outras váriaveis, como quantidade de andares, banheiros, etc.

## Notebook: 2.0-Main_Questions

### Nessa seção as perguntas do CEO foram respondidas.
* Em adicional foi gerada a tabela final com a recomendação de quais propriedades comprar, por qual preço revende-las se elas forem renovadas ou não. ALém do possível lucro.

#
## Notebook: 3.0-Hypotheses

### Nessa seção foram criadas e respondidas três hipoteses com relação aos dados.
