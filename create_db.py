import oracledb

# Definindo a conexão com o banco de dados
dsn = oracledb.makedsn("localhost", 1521, sid="XE")
connection = oracledb.connect(user="system", password="oracle123", dsn=dsn)

try:
    cursor = connection.cursor()
    
    # Criação das tabelas do banco de dados
    queries = [
        """
        CREATE TABLE culturas (
            idcultura INTEGER NOT NULL,
            nome      NVARCHAR2(30) NOT NULL
        )
        """,
        """
        ALTER TABLE culturas ADD CONSTRAINT pk_culturas PRIMARY KEY (idcultura)
        """,
        """
        ALTER TABLE culturas ADD CONSTRAINT un_culturas_nome UNIQUE (nome)
        """,
        """
        CREATE TABLE sensor_nutrientes (
            idsensornutriente INTEGER NOT NULL,
            valorfosforo      NUMBER NOT NULL,
            valorpotassio     NUMBER NOT NULL,
            datamedicao       DATE NOT NULL,
            idcultura         INTEGER NOT NULL
        )
        """,
        """
        ALTER TABLE sensor_nutrientes ADD CONSTRAINT pk_sensor_nutrientes PRIMARY KEY (idsensornutriente)
        """,
        """
        CREATE TABLE sensor_phs (
            idsensorph  INTEGER NOT NULL,
            valor       NUMBER NOT NULL,
            datamedicao DATE NOT NULL,
            idcultura   INTEGER NOT NULL
        )
        """,
        """
        ALTER TABLE sensor_phs ADD CONSTRAINT pk_sensor_ph PRIMARY KEY (idsensorph)
        """,
        """
        CREATE TABLE sensor_umidades (
            idsensorumidade INTEGER NOT NULL,
            valor           NUMBER NOT NULL,
            datamedicao     DATE NOT NULL,
            idcultura       INTEGER NOT NULL
        )
        """,
        """
        ALTER TABLE sensor_umidades ADD CONSTRAINT pk_sensor_umidade PRIMARY KEY (idsensorumidade)
        """,
        """
        ALTER TABLE sensor_nutrientes
            ADD CONSTRAINT fk_sensor_nutrientes_culturas FOREIGN KEY (idcultura)
            REFERENCES culturas (idcultura)
        """,
        """
        ALTER TABLE sensor_phs
            ADD CONSTRAINT fk_sensor_ph_culturas FOREIGN KEY (idcultura)
            REFERENCES culturas (idcultura)
        """,
        """
        ALTER TABLE sensor_umidades
            ADD CONSTRAINT fk_sensor_umidade_culturas FOREIGN KEY (idcultura)
            REFERENCES culturas (idcultura)
        """
    ]
    
    # Loop para executar todas as queries
    for x in queries:
        cursor.execute(x)
finally:  
    # Fecha a conexão
    cursor.close()
    connection.close()