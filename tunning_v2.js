
// Cenário 1: "Ênfase no Cache"
const tuningScenario1Query1 = `
-- Ajustar shared_buffers para 4GB
ALTER SYSTEM SET shared_buffers = '4GB';

-- Manter work_mem em 32MB
-- Não é necessário alteração
`;

const tuningScenario1Query2 = `
-- Ajustar effective_cache_size para 8GB
ALTER SYSTEM SET effective_cache_size = '8GB';
`;

// Cenário 2: "Ênfase na Classificação e Mesclagem"
const tuningScenario2Query1 = `
-- Manter shared_buffers em 128MB
-- Não é necessário alteração

-- Ajustar work_mem para 64MB
ALTER SYSTEM SET work_mem = '64MB';

-- Manter effective_cache_size em 4GB
-- Não é necessário alteração
`;

// Cenário 3: "Equilíbrio entre Cache e Mesclagem"
const tuningScenario3Query1 = `
-- Ajustar shared_buffers para 2GB
ALTER SYSTEM SET shared_buffers = '2GB';
`;

const tuningScenario3Query2 = `
-- Ajustar work_mem para 48MB
ALTER SYSTEM SET work_mem = '48MB';
`;

const tuningScenario3Query3 = `
-- Ajustar effective_cache_size para 6GB
ALTER SYSTEM SET effective_cache_size = '6GB';
`;

const resetSharedBuffersQuery = 'ALTER SYSTEM RESET shared_buffers;';

const resetWorkMemQuery = 'ALTER SYSTEM RESET work_mem;';

const resetEffectiveCacheSizeQuery = 'ALTER SYSTEM RESET effective_cache_size;';

module.exports = {
  tuningScenario1Query1,
  tuningScenario1Query2,
  tuningScenario2Query1,
  tuningScenario3Query1,
  tuningScenario3Query2,
  tuningScenario3Query3,
  resetSharedBuffersQuery,
  resetWorkMemQuery,
  resetEffectiveCacheSizeQuery,
};
