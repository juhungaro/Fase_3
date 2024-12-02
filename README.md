# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo_fiap.jpg" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Sistema de irrigação automatico 

## Nome do grupo

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/bryanjfagundes/">Bryan Fagundes</a>
- <a href="https://br.linkedin.com/in/brenner-fagundes">Brenner Fagundes</a>
- <a href="https://www.linkedin.com/in/diogo-botton-46ba49197/">Diogo Botton</a> 
- <a href="https://www.linkedin.com/in/hyankacoelho/"> Hyanka Coelho</a> 
- <a href="https://www.linkedin.com/in/julianahungaro/"> Juliana Hungaro Fidelis </a> 

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do Tutor</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/in/andregodoichiovato/">André Godoi</a>


## 📜 Descrição

*Este sistema de irrigação automatizado tem como objetivo otimizar a gestão da água e medir os nutrientes em plantações, garantindo um crescimento saudável e eficiente das culturas. Ele monitora a umidade do solo, temperatura, pH e os níveis de potássio e fósforo, acionando a bomba de água quando necessário.*


## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>.github</b>: Nesta pasta ficarão os arquivos de configuração específicos do GitHub que ajudam a gerenciar e automatizar processos no repositório.

- <b>assets</b>: aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens.

- <b>config</b>: Posicione aqui arquivos de configuração que são usados para definir parâmetros e ajustes do projeto.

- <b>document</b>: aqui estão todos os documentos do projeto que as atividades poderão pedir. Na subpasta "other", adicione documentos complementares e menos importantes.

- <b>scripts</b>: Posicione aqui scripts auxiliares para tarefas específicas do seu projeto. Exemplo: deploy, migrações de banco de dados, backups.

- <b>src</b>: Todo o código fonte criado para o desenvolvimento do projeto ao longo das 7 fases.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

## 🔧 Como executar o código

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


## 🗃 Histórico de lançamentos

* 0.5.0 - XX/XX/2024
    * 
* 0.4.0 - XX/XX/2024
    * 
* 0.3.0 - XX/XX/2024
    * 
* 0.2.0 - XX/XX/2024
    * 
* 0.1.0 - XX/XX/2024
    *

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>









