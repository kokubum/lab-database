consulta_1 = """
SELECT id_familia, id_pessoa, idade
FROM tb_pessoa
WHERE id_familia = '500';
"""

consulta_2 = """
SELECT AVG(vlr_renda_media_fam)
FROM tb_familia;
"""

consulta_3 = """
SELECT id_familia, qtde_pessoas
FROM tb_familia
WHERE qtde_pessoas > 4;
"""

consulta_4 = """
SELECT id_pessoa, ind_frequenta_escola_memb, cod_ano_serie_frequenta_memb
FROM tb_escolaridade
WHERE id_pessoa = '255';
"""

consulta_5 = """
SELECT p.id_pessoa, f.vlr_renda_media_fam, e.ind_frequenta_escola_memb
FROM tb_pessoa p
JOIN tb_familia f ON p.id_familia = f.id_familia
LEFT JOIN tb_escolaridade e ON p.id_pessoa = e.id_pessoa;
"""

consulta_6 = """
SELECT p.cod_raca_cor_pessoa, AVG(f.vlr_renda_media_fam) as media_renda
FROM tb_pessoa p
JOIN tb_familia f ON p.id_familia = f.id_familia
GROUP BY p.cod_raca_cor_pessoa;
"""

consulta_7 = """
SELECT d.cod_agua_canalizada_fam, AVG(f.vlr_renda_media_fam) as media_renda
FROM tb_familia f
JOIN tb_domicilio d ON f.id_familia = d.id_familia
GROUP BY d.cod_agua_canalizada_fam;
"""

consulta_8 = """
SELECT d.cod_agua_canalizada_fam, AVG(f.vlr_renda_media_fam) as media_renda
FROM tb_familia f
JOIN tb_domicilio d ON f.id_familia = d.id_familia
GROUP BY d.cod_agua_canalizada_fam;
"""

consulta_9 = """
SELECT faixa_etaria, AVG(idade) as media_idade
FROM (
    SELECT idade, 
           CASE
             WHEN idade <= 18 THEN '0-18'
             WHEN idade <= 30 THEN '19-30'
             ELSE '31+'
           END AS faixa_etaria
    FROM tb_pessoa
) AS subquery
GROUP BY faixa_etaria;
"""

consulta_10 = """
SELECT id_familia, vlr_renda_media_fam
FROM tb_familia
WHERE vlr_renda_media_fam > (SELECT AVG(vlr_renda_media_fam) FROM tb_familia)
  AND qtde_pessoas > 2;
"""

consulta_11 = """
SELECT cod_material_piso_fam, AVG(media_comodos) as media_comodos
FROM (
    SELECT cod_material_piso_fam, qtd_comodos_domic_fam as media_comodos
    FROM tb_domicilio
) AS subquery
GROUP BY cod_material_piso_fam;
"""