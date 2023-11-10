import psycopg2
import queries
import tunning
import indexes
from time import time

TUNNING_SCENARIO = 1
INDEX_SCENARIO = 1

# Função para calcular o tempo de execução de uma consulta
def measure_query_time(cursor, query):
    try:
        # Medir o tempo de execução
        start_time = time()
        
        # Executar a consulta
        cursor.execute(query)

        end_time = time()
        execution_time = end_time - start_time

        print(f"Tempo de execução da consulta: {execution_time:.4f} segundos")

    except Exception as e:
        print(f"Erro ao executar a consulta: {e}")

def reset(cursor):
  cursor.execute(tunning.reset_shared_buffers_query)
  cursor.execute(tunning.reset_work_mem_query)
  cursor.execute(tunning.reset_effective_cache_size_query)

  reset_index_list = [
    indexes.reset_scenario_1_query,
    indexes.reset_scenario_2_query,
    indexes.reset_scenario_3_query,
  ]

  if INDEX_SCENARIO > 0:
    cursor.execute(reset_index_list[INDEX_SCENARIO-1])




if __name__ == "__main__":
  # Estabelecer conexão com o banco de dados
  connection = psycopg2.connect(
    database="lab",
    user="lab_user",
    password="lab_password",
    host="localhost",
    port="5432"
  )
  connection.autocommit = True 
  cursor = connection.cursor()
  

  queries_list = [
    queries.consulta_1,
    queries.consulta_2,
    queries.consulta_3,
    queries.consulta_4,
    # queries.consulta_5,
    # queries.consulta_6,
    # queries.consulta_7,
    # queries.consulta_8,
    # queries.consulta_9,
    # queries.consulta_10,
    # queries.consulta_11,
  ]

  tunning_list = [
    [tunning.tuning_scenario_1_query_1, tunning.tuning_scenario_1_query_2],
    [tunning.tuning_scenario_2_query_1],
    [tunning.tuning_scenario_3_query_1, tunning.tuning_scenario_3_query_2, tunning.tuning_scenario_3_query_3],
  ]

  indexes_list = [
    indexes.index_scenario_1_query,
    indexes.index_scenario_2_query,
    indexes.index_scenario_3_query,
  ]

  if TUNNING_SCENARIO > 0:
    for query in tunning_list[TUNNING_SCENARIO-1]:
      cursor.execute(query)
    
  if INDEX_SCENARIO > 0:
    cursor.execute(indexes_list[INDEX_SCENARIO-1])


  print(f"TUNNING SCENARIO: {TUNNING_SCENARIO} | INDEX SCENARIO: {INDEX_SCENARIO}\n")

  for index, query in enumerate(queries_list):
    print(f"[INICIO] CONSULTA NUMERO: {index+1}\n")

    measure_query_time(cursor,query)

    print(f"[FINAL] CONSULTA NUMERO: {index+1}\n")


  reset(cursor)
  # Fechar a conexão
  cursor.close()
  connection.close()