# Sistema de irrigação automatico 

**Descrição Geral**
Este sistema de irrigação automatizado tem como objetivo otimizar a gestão da água e medir os nutrientes em plantações, garantindo um crescimento saudável e eficiente das culturas. Ele monitora a umidade do solo, temperatura, pH e os níveis de potássio e fósforo, acionando a bomba de água quando necessário.

**Componentes**
- Microcontrolador: ESP32
- Sensor de umidade e temperatura do solo: dht22
- Sensores de Potássio e Fósforo: São acionados manualmente para a leitura dos valores (números gerados aleatoriamente).
- Relé: Para controlar a bomba de água
- Bomba de água: representada pelo led azul
- Sensor de ph

**Funcionamento**
- Leitura dos Sensores: O microcontrolador lê continuamente (delay 1000) os dados dos sensores de umidade, temperatura, potássio, fósforo e pH.
- Acionamento da Bomba: Se a umidade do solo estiver abaixo do limite mínimo de 20% de umidade, o microcontrolador aciona a bomba de água através do relé.
- Indicação Visual: Os LEDs indicam o estado do sistema, como a bomba ligada ou desligada.
- Sensor de ph: Leitura do valor analógico do sensor de pH e mapeamento do valor para a escala de pH (4 a 7)

**Wokwi https://wokwi.com/projects/413103691995388929**

Para realizar o CRUD das tabelas de cultura e demais sensores decidimos fazer uma API em Python utlizando um framework chamado FastAPI.

**Por que FastAPI?**
- FastAPI é um framework popular para realização de aplicações REST escaláveis que necessitam de alto desempenho.
- É projetado para ser fácil de user, rápido e seguro.
- Suporte nativo para documentação OpenAPI (Swagger).

Achamos interessante também utilizar uma **ORM** chamada **SQLAlchemy** para a realização da criação das tabelas automaticamente na inicialização do aplicativo caso não existam.

**O que é uma ORM?**
- ORM é a sigla para Object-Relational Mapping, em português significa mapeamento objeto-relacional. É uma ferramenta que facilita o armazenamento e a recuperação de objetos de um banco de dados relacional sem a necessidade de escrever código SQL manualmente.

### Como inicializar a API?
- Para baixar as dependências da aplicação, abra o cmd no diretório do projeto e digite o seguinte comando:
```bash
    pip install -r requirements.txt
```

- Para inicializar o banco de dados Oracle, abra o cmd no diretório do projeto e digite o seguinte comando:
```bash
    docker-compose up -d
```

- Para iniciar a aplicação, é necessário abrir o cmd no diretório "app" e rodar o seguinte código:
```bash
    uvicorn main:app --reload
```

### Especificação de cada camada do projeto

**App**
- Contem toda a lógica para o funcionamento da Api.

**App/controllers**
- A camada controller é responsável por receber todas as requisições do usuário, no caso, o CRUD de culturas e sensores.

**App/main.py**
- Arquivo principal da configuração da API.

**App/models.py**
- Os modelos (ou domínios) são classes que representam a estrutura e o comportamento dos dados da aplicação.
- Os models geralmente se conectam ao banco de dados e mapeiam as tabelas para objetos que o código da API utiliza, isso é conhecido como Object-Relational Mapping (ORM).

**App/db_config.py**
- É responsável pela configuração de conexão ao banco de dados Oracle.

**.env**
- São as variáveis de ambiente necessárias para funcionamento da aplicação, no caso, estão as variáveis de conexão do banco de dados.

**docker-compose.yml**
- O docker-compose é um orquestrador de containers docker.
- Para este projeto utilizamos com a finalidade de criar uma imagem do banco de dados Oracle em um container.
