# Cenário 1: "Otimização das Consultas de Seleção Rápida"
index_scenario_1_query = '''
-- Adicionar índice na tabela tb_pessoa para a coluna id_familia
CREATE INDEX idx_pessoa_id_familia
ON tb_pessoa (id_familia);
'''

# Cenário 2: "Otimização de Consultas de Filtragem e Agregação"
index_scenario_2_query = '''
-- Adicionar índice na tabela tb_familia para a coluna qtde_pessoas
CREATE INDEX idx_familia_qtde_pessoas
ON tb_familia (qtde_pessoas);

-- Adicionar índice na tabela tb_domicilio para a coluna cod_agua_canalizada_fam
CREATE INDEX idx_domicilio_agua_canalizada
ON tb_domicilio (cod_agua_canalizada_fam);
'''

# Cenário 3: "Otimização de Consultas de JOIN e Seleção"
index_scenario_3_query = '''
-- Adicionar índice na tabela tb_pessoa para as colunas id_familia e id_pessoa
CREATE INDEX idx_pessoa_familia_pessoa
ON tb_pessoa (id_familia, id_pessoa);

-- Adicionar índice na tabela tb_familia para a coluna cd_ibge
CREATE INDEX idx_familia_cd_ibge
ON tb_familia (cd_ibge);

-- Adicionar índice na tabela tb_escolaridade para a coluna id_pessoa
CREATE INDEX idx_escolaridade_id_pessoa
ON tb_escolaridade (id_pessoa);
'''

# Cenário 4: "Otimização de Consultas de Resumo Estatístico"
index_scenario_4_query = '''
-- Adicionar índice na tabela tb_pessoa para a coluna cod_raca_cor_pessoa
CREATE INDEX idx_pessoa_cod_raca_cor
ON tb_pessoa (cod_raca_cor_pessoa);

-- Adicionar índice na tabela tb_familia para a coluna vlr_renda_media_fam
CREATE INDEX idx_familia_renda_media
ON tb_familia (vlr_renda_media_fam);

-- Adicionar índice na tabela tb_domicilio para a coluna cod_material_piso_fam
CREATE INDEX idx_domicilio_material_piso
ON tb_domicilio (cod_material_piso_fam);
'''

# Cenário 1: "Otimização das Consultas de Seleção Rápida"
reset_scenario_1_query = '''
-- Remover índice na tabela tb_pessoa para a coluna id_familia
DROP INDEX IF EXISTS idx_pessoa_id_familia;
'''

# Cenário 2: "Otimização de Consultas de Filtragem e Agregação"
reset_scenario_2_query = '''
-- Remover índice na tabela tb_familia para a coluna qtde_pessoas
DROP INDEX IF EXISTS idx_familia_qtde_pessoas;

-- Remover índice na tabela tb_domicilio para a coluna cod_agua_canalizada_fam
DROP INDEX IF EXISTS idx_domicilio_agua_canalizada;
'''

# Cenário 3: "Otimização de Consultas de JOIN e Seleção"
reset_scenario_3_query = '''
-- Remover índice na tabela tb_pessoa para as colunas id_familia e id_pessoa
DROP INDEX IF EXISTS idx_pessoa_familia_pessoa;

-- Remover índice na tabela tb_familia para a coluna cd_ibge
DROP INDEX IF EXISTS idx_familia_cd_ibge;

-- Remover índice na tabela tb_escolaridade para a coluna id_pessoa
DROP INDEX IF EXISTS idx_escolaridade_id_pessoa;
'''

# Cenário 4: "Otimização de Consultas de Resumo Estatístico"
reset_scenario_4_query = '''
-- Remover índice na tabela tb_pessoa para a coluna cod_raca_cor_pessoa
DROP INDEX IF EXISTS idx_pessoa_cod_raca_cor;

-- Remover índice na tabela tb_familia para a coluna vlr_renda_media_fam
DROP INDEX IF EXISTS idx_familia_renda_media;

-- Remover índice na tabela tb_domicilio para a coluna cod_material_piso_fam
DROP INDEX IF EXISTS idx_domicilio_material_piso;
'''