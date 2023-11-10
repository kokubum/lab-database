# Cenário 1: "Ênfase no Cache"
tuning_scenario_1_query_1 = '''
-- Ajustar shared_buffers para 4GB
ALTER SYSTEM SET shared_buffers = '4GB';

-- Manter work_mem em 32MB
-- Não é necessário alteração
'''

tuning_scenario_1_query_2 = '''
-- Ajustar effective_cache_size para 8GB
ALTER SYSTEM SET effective_cache_size = '8GB';
'''

# Cenário 2: "Ênfase na Classificação e Mesclagem"
tuning_scenario_2_query_1 = '''
-- Manter shared_buffers em 128MB
-- Não é necessário alteração

-- Ajustar work_mem para 64MB
ALTER SYSTEM SET work_mem = '64MB';

-- Manter effective_cache_size em 4GB
-- Não é necessário alteração
'''

# Cenário 3: "Equilíbrio entre Cache e Mesclagem"
tuning_scenario_3_query_1 = '''
-- Ajustar shared_buffers para 2GB
ALTER SYSTEM SET shared_buffers = '2GB';
'''

tuning_scenario_3_query_2 = '''
-- Ajustar work_mem para 48MB
ALTER SYSTEM SET work_mem = '48MB';
'''

tuning_scenario_3_query_3 = '''
-- Ajustar effective_cache_size para 6GB
ALTER SYSTEM SET effective_cache_size = '6GB';
'''

reset_shared_buffers_query = 'ALTER SYSTEM RESET shared_buffers;'

reset_work_mem_query = 'ALTER SYSTEM RESET work_mem;'

reset_effective_cache_size_query = 'ALTER SYSTEM RESET effective_cache_size;'