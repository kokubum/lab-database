sql_create_table_mun = '''
  CREATE TABLE IF NOT EXISTS municipios (
    COD_MUNICIPIO VARCHAR(11),
    NOME_MUNICIPIO VARCHAR(50),
    UF VARCHAR(2),
    CD_MUNICIPIO_IBGE VARCHAR(8),
    CD_SEDES_TCE NUMERIC(2),
    SIGLA_SEDE_TCE VARCHAR(4),
    NOME_SEDE_TCE TEXT
  );
'''

sql_copy_csv_mun = '''
  COPY 
    municipios 
  FROM '/var/lib/postgresql/data/municipios.csv'
  DELIMITER ','
  CSV HEADER;
'''