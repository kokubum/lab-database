sql_create_staging_table_fam = '''
  CREATE TABLE IF NOT EXISTS tb_familia_staging (
    cd_ibge VARCHAR(7),
    estrato TEXT,
    classf TEXT,
    id_familia VARCHAR(11),
    dat_cadastramento_fam TEXT,
    dat_alteracao_fam VARCHAR(10),
    vlr_renda_media_fam NUMERIC(9),
    dat_atualizacao_familia TEXT,
    cod_local_domic_fam NUMERIC(1),
    cod_especie_domic_fam NUMERIC(1),
    qtd_comodos_domic_fam NUMERIC(2),
    qtd_comodos_dormitorio_fam NUMERIC(2),
    cod_material_piso_fam NUMERIC(1),
    cod_material_domic_fam NUMERIC(1),
    cod_agua_canalizada_fam NUMERIC(1),
    cod_abaste_agua_domic_fam NUMERIC(1),
    cod_banheiro_domic_fam NUMERIC(1),
    cod_escoa_sanitario_domic_fam NUMERIC(1),
    cod_destino_lixo_domic_fam NUMERIC(1),
    cod_iluminacao_domic_fam NUMERIC(1),
    cod_calcamento_domic_fam NUMERIC(1),
    cod_familia_indigena_fam TEXT,
    ind_familia_quilombola_fam TEXT,
    nom_estab_assist_saude_fam TEXT,
    cod_eas_fam TEXT,
    nom_centro_assist_fam TEXT,
    cod_centro_assist_fam TEXT,
    ind_parc_mds_fam TEXT,
    qtde_pessoas NUMERIC(2),
    peso_fam TEXT,
    marc_pbf TEXT
  )
'''

sql_copy_csv_fam = '''
  COPY 
    tb_familia_staging (
      cd_ibge,
      estrato,
      classf,
      id_familia,
      dat_cadastramento_fam,
      dat_alteracao_fam,
      vlr_renda_media_fam,
      dat_atualizacao_familia,
      cod_local_domic_fam,
      cod_especie_domic_fam,
      qtd_comodos_domic_fam,
      qtd_comodos_dormitorio_fam,
      cod_material_piso_fam,
      cod_material_domic_fam,
      cod_agua_canalizada_fam,
      cod_abaste_agua_domic_fam,
      cod_banheiro_domic_fam,
      cod_escoa_sanitario_domic_fam,
      cod_destino_lixo_domic_fam,
      cod_iluminacao_domic_fam,
      cod_calcamento_domic_fam,
      cod_familia_indigena_fam,
      ind_familia_quilombola_fam,
      nom_estab_assist_saude_fam,
      cod_eas_fam,
      nom_centro_assist_fam,
      cod_centro_assist_fam,
      ind_parc_mds_fam,
      qtde_pessoas,
      peso_fam,
      marc_pbf
    ) 
  FROM '/var/lib/postgresql/data/amostra_familia_2016.csv'
  DELIMITER ';'
  CSV HEADER;

  COPY 
    tb_familia_staging (
      cd_ibge,
      estrato,
      classf,
      id_familia,
      dat_cadastramento_fam,
      dat_alteracao_fam,
      vlr_renda_media_fam,
      dat_atualizacao_familia,
      cod_local_domic_fam,
      cod_especie_domic_fam,
      qtd_comodos_domic_fam,
      qtd_comodos_dormitorio_fam,
      cod_material_piso_fam,
      cod_material_domic_fam,
      cod_agua_canalizada_fam,
      cod_abaste_agua_domic_fam,
      cod_banheiro_domic_fam,
      cod_escoa_sanitario_domic_fam,
      cod_destino_lixo_domic_fam,
      cod_iluminacao_domic_fam,
      cod_calcamento_domic_fam,
      cod_familia_indigena_fam,
      ind_familia_quilombola_fam,
      nom_estab_assist_saude_fam,
      cod_eas_fam,
      nom_centro_assist_fam,
      cod_centro_assist_fam,
      ind_parc_mds_fam,
      qtde_pessoas,
      peso_fam,
      marc_pbf
    ) 
  FROM '/var/lib/postgresql/data/amostra_familia_2017.csv'
  DELIMITER ';'
  CSV HEADER;

  COPY 
    tb_familia_staging (
      cd_ibge,
      estrato,
      classf,
      id_familia,
      dat_cadastramento_fam,
      dat_alteracao_fam,
      vlr_renda_media_fam,
      dat_atualizacao_familia,
      cod_local_domic_fam,
      cod_especie_domic_fam,
      qtd_comodos_domic_fam,
      qtd_comodos_dormitorio_fam,
      cod_material_piso_fam,
      cod_material_domic_fam,
      cod_agua_canalizada_fam,
      cod_abaste_agua_domic_fam,
      cod_banheiro_domic_fam,
      cod_escoa_sanitario_domic_fam,
      cod_destino_lixo_domic_fam,
      cod_iluminacao_domic_fam,
      cod_calcamento_domic_fam,
      cod_familia_indigena_fam,
      ind_familia_quilombola_fam,
      nom_estab_assist_saude_fam,
      cod_eas_fam,
      nom_centro_assist_fam,
      cod_centro_assist_fam,
      ind_parc_mds_fam,
      marc_pbf,
      qtde_pessoas,
      peso_fam
    )
  FROM '/var/lib/postgresql/data/amostra_familia_2018.csv'
  DELIMITER ';'
  CSV HEADER;
'''


sql_create_table_fam = '''
  CREATE TABLE IF NOT EXISTS tb_familia (
    id_familia VARCHAR(11),
    cd_ibge VARCHAR(7),
    dat_alteracao_fam VARCHAR(10),
    vlr_renda_media_fam NUMERIC(9),
    qtde_pessoas NUMERIC(2)
  )
'''


sql_create_table_dom = '''
  CREATE TABLE IF NOT EXISTS tb_domicilio (
    id_familia VARCHAR(11),
    cod_local_domic_fam NUMERIC(1),
    cod_especie_domic_fam NUMERIC(1),
    qtd_comodos_domic_fam NUMERIC(2),
    qtd_comodos_dormitorio_fam NUMERIC(2),
    cod_material_piso_fam NUMERIC(1),
    cod_material_domic_fam NUMERIC(1),
    cod_agua_canalizada_fam NUMERIC(1),
    cod_abaste_agua_domic_fam NUMERIC(1),
    cod_banheiro_domic_fam NUMERIC(1),
    cod_escoa_sanitario_domic_fam NUMERIC(1),
    cod_destino_lixo_domic_fam NUMERIC(1),
    cod_iluminacao_domic_fam NUMERIC(1),
    cod_calcamento_domic_fam NUMERIC(1)
  )
'''

sql_populating_table_fam = '''
  INSERT INTO tb_familia (
    id_familia,
    cd_ibge,
    dat_alteracao_fam,
    vlr_renda_media_fam,
    qtde_pessoas
  )(
    SELECT
      id_familia,
      cd_ibge,
      dat_alteracao_fam,
      vlr_renda_media_fam,
      qtde_pessoas  
    FROM tb_familia_staging
  );
'''

sql_populating_table_dom = '''
  INSERT INTO tb_domicilio (
    id_familia,
    cod_local_domic_fam,
    cod_especie_domic_fam,
    qtd_comodos_domic_fam,
    qtd_comodos_dormitorio_fam,
    cod_material_piso_fam,
    cod_material_domic_fam,
    cod_agua_canalizada_fam,
    cod_abaste_agua_domic_fam,
    cod_banheiro_domic_fam,
    cod_escoa_sanitario_domic_fam,
    cod_destino_lixo_domic_fam,
    cod_iluminacao_domic_fam,
    cod_calcamento_domic_fam
  )(
    SELECT
      id_familia,
      cod_local_domic_fam,
      cod_especie_domic_fam,
      qtd_comodos_domic_fam,
      qtd_comodos_dormitorio_fam,
      cod_material_piso_fam,
      cod_material_domic_fam,
      cod_agua_canalizada_fam,
      cod_abaste_agua_domic_fam,
      cod_banheiro_domic_fam,
      cod_escoa_sanitario_domic_fam,
      cod_destino_lixo_domic_fam,
      cod_iluminacao_domic_fam,
      cod_calcamento_domic_fam 
    FROM tb_familia_staging
  );
'''

sql_drop_staging = '''
  DROP TABLE tb_familia_staging;
'''