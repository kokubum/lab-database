

sql_create_staging_table_pess = '''
  CREATE TABLE IF NOT EXISTS tb_pessoa_staging (
    cd_ibge INT,
    estrato INT,
    classf INT,
    id_familia VARCHAR(11),
    id_pessoa VARCHAR(11),
    cod_sexo_pessoa NUMERIC(1),
    idade NUMERIC(3),
    cod_parentesco_rf_pessoa NUMERIC(2),
    cod_raca_cor_pessoa NUMERIC(1),
    cod_local_nascimento_pessoa NUMERIC(1),
    cod_certidao_registrada_pessoa INT,
    cod_deficiencia_memb INT,
    cod_sabe_ler_escrever_memb INT,
    ind_frequenta_escola_memb NUMERIC(1),
    cod_escola_local_memb INT,
    cod_curso_frequenta_memb INT,
    cod_ano_serie_frequenta_memb NUMERIC(2),
    cod_curso_frequentou_pessoa_memb NUMERIC(2),
    cod_ano_serie_frequentou_memb NUMERIC(2),
    cod_concluiu_frequentou_memb NUMERIC(1),
    cod_trabalhou_memb INT,
    cod_afastado_trab_memb INT,
    cod_agricultura_trab_memb INT,
    cod_principal_trab_memb NUMERIC(2),
    val_remuner_emprego_memb NUMERIC(5),
    cod_trabalho_12_meses_memb NUMERIC(1),
    qtd_meses_12_meses_memb NUMERIC(2),
    val_renda_bruta_12_meses_memb NUMERIC(5),
    val_renda_doacao_memb NUMERIC(5),
    val_renda_aposent_memb NUMERIC(5),
    val_renda_seguro_desemp_memb NUMERIC(5),
    val_renda_pensao_alimen_memb NUMERIC(5),
    val_outras_rendas_memb NUMERIC(5),
    peso_fam FLOAT,
    peso_pes FLOAT
  );
'''

sql_copy_csv_pess = '''
  COPY 
    tb_pessoa_staging
  FROM '/var/lib/postgresql/data/amostra_pessoa_2016.csv'
  DELIMITER ';'
  CSV HEADER;

  COPY 
    tb_pessoa_staging
  FROM '/var/lib/postgresql/data/amostra_pessoa_2017.csv'
  DELIMITER ';'
  CSV HEADER;

  COPY 
    tb_pessoa_staging
  FROM '/var/lib/postgresql/data/amostra_pessoa_2018.csv'
  DELIMITER ';'
  CSV HEADER;
'''

sql_create_table_pess = '''
 CREATE TABLE IF NOT EXISTS tb_pessoa (
    id_familia VARCHAR(11),
    id_pessoa VARCHAR(11),
    cod_sexo_pessoa NUMERIC(1),
    idade NUMERIC(3),
    cod_parentesco_rf_pessoa NUMERIC(2),
    cod_raca_cor_pessoa NUMERIC(1),
    cod_local_nascimento_pessoa NUMERIC(1)
  );
'''


sql_create_table_trab = '''
 CREATE TABLE IF NOT EXISTS tb_trabalho_remun (
    id_familia VARCHAR(11),
    id_pessoa VARCHAR(11),
    cod_principal_trab_memb NUMERIC(2),
    val_remuner_emprego_memb NUMERIC(5),
    cod_trabalho_12_meses_memb NUMERIC(1),
    qtd_meses_12_meses_memb NUMERIC(2),
    val_renda_bruta_12_meses_memb NUMERIC(5),
    val_renda_doacao_memb NUMERIC(5),
    val_renda_aposent_memb NUMERIC(5),
    val_renda_seguro_desemp_memb NUMERIC(5),
    val_renda_pensao_alimen_memb NUMERIC(5),
    val_outras_rendas_memb NUMERIC(5)
  );
'''

sql_create_table_esc = '''
 CREATE TABLE IF NOT EXISTS tb_escolaridade (
    id_familia VARCHAR(11),
    id_pessoa VARCHAR(11),
    ind_frequenta_escola_memb NUMERIC(1),
    cod_ano_serie_frequenta_memb NUMERIC(2),
    cod_curso_frequentou_pessoa_memb NUMERIC(2),
    cod_ano_serie_frequentou_memb NUMERIC(2),
    cod_concluiu_frequentou_memb NUMERIC(1)
  );
'''

sql_populating_table_pess = '''
  INSERT INTO tb_pessoa (
    id_familia,
    id_pessoa,
    cod_sexo_pessoa,
    idade,
    cod_parentesco_rf_pessoa,
    cod_raca_cor_pessoa,
    cod_local_nascimento_pessoa
  )(
    SELECT
      id_familia,
      id_pessoa,
      cod_sexo_pessoa,
      idade,
      cod_parentesco_rf_pessoa,
      cod_raca_cor_pessoa,
      cod_local_nascimento_pessoa
    FROM tb_pessoa_staging
  );
'''

sql_populating_table_trab = '''
  INSERT INTO tb_trabalho_remun (
    id_familia,
    id_pessoa,
    cod_principal_trab_memb,
    val_remuner_emprego_memb,
    cod_trabalho_12_meses_memb,
    qtd_meses_12_meses_memb,
    val_renda_bruta_12_meses_memb,
    val_renda_doacao_memb,
    val_renda_aposent_memb,
    val_renda_seguro_desemp_memb,
    val_renda_pensao_alimen_memb,
    val_outras_rendas_memb
  )(
    SELECT
      id_familia,
      id_pessoa,
      cod_principal_trab_memb,
      val_remuner_emprego_memb,
      cod_trabalho_12_meses_memb,
      qtd_meses_12_meses_memb,
      val_renda_bruta_12_meses_memb,
      val_renda_doacao_memb,
      val_renda_aposent_memb,
      val_renda_seguro_desemp_memb,
      val_renda_pensao_alimen_memb,
      val_outras_rendas_memb
    FROM tb_pessoa_staging
  );
'''

sql_populating_table_esc = '''
  INSERT INTO tb_escolaridade (
    id_familia,
    id_pessoa,
    ind_frequenta_escola_memb,
    cod_ano_serie_frequenta_memb,
    cod_curso_frequentou_pessoa_memb,
    cod_ano_serie_frequentou_memb,
    cod_concluiu_frequentou_memb
  )(
    SELECT
      id_familia,
      id_pessoa,
      ind_frequenta_escola_memb,
      cod_ano_serie_frequenta_memb,
      cod_curso_frequentou_pessoa_memb,
      cod_ano_serie_frequentou_memb,
      cod_concluiu_frequentou_memb
    FROM tb_pessoa_staging
  );
'''

sql_drop_staging = '''
  DROP TABLE tb_pessoa_staging;
'''