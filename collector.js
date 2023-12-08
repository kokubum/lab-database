const { Client } = require('pg');
const {
  resetEffectiveCacheSizeQuery,
  resetSharedBuffersQuery,
  resetWorkMemQuery,
  tuningScenario1Query1,
  tuningScenario1Query2,
  tuningScenario2Query1,
  tuningScenario3Query1,
  tuningScenario3Query2,
  tuningScenario3Query3
} = require('./tunning_v2');
const {
  resetScenario1Query,
  resetScenario2Query,
  resetScenario3Query,
  indexScenario1Query,
  indexScenario2Query,
  indexScenario3Query,
}= require('./indexes_v2')
const  {
  consulta1,
  consulta2,
  consulta3,
  consulta4
} = require('./queries_v2')

TUNNING_SCENARIO = 0
INDEX_SCENARIO = 0

async function executeQuery(client, query, dbName, queryNumber) {
  console.log("STARTING QUERY "+ queryNumber)
  const begin = new Date().getTime()
  // trecho de código que queremos mensurar
  

  try {
    await client.query(query);


  } catch (error) {
    console.error(`Error executing query in ${dbName}:`, error);
  }
  const total = new Date().getTime() - begin

  console.log("FINISHING QUERY "+ queryNumber + " - TIME: " + total/1000 + "s")

}

async function reset(client) {
  await client.query(resetEffectiveCacheSizeQuery)
  await client.query(resetSharedBuffersQuery)
  await client.query(resetWorkMemQuery)

  reset_index_list = [resetScenario1Query, resetScenario2Query, resetScenario3Query]

  if (INDEX_SCENARIO > 0){
    await client.query(reset_index_list[INDEX_SCENARIO-1])
  }
  console.log("FINISH RESET")
}

async function main() {
  // Configurações de conexão para os dois bancos de dados
  const dbConfig1 = {
    user: 'lab_user',
    password: 'lab_password',
    host: 'localhost',
    port: 5432,
    database: 'lab',
  };

  const dbConfig2 = {
    user: 'lab_user',
    password: 'lab_password',
    host: 'localhost',
    port: 5433,
    database: 'lab',
  };

  // Lista de consultas a serem executadas em paralelo
  const queries = [
    consulta1,
    consulta2,
    consulta3,
    consulta4
    //  queries.consulta_5,
    //  queries.consulta_6,
    // queries.consulta_7,
    // queries.consulta_8,
    //  queries.consulta_9,
    //  queries.consulta_10,
    //  queries.consulta_11,
  ];

  // Crie clientes para os dois bancos de dados
  const client1 = new Client(dbConfig1);
  const client2 = new Client(dbConfig2);
  const clients = [client1, client2];
  // Conecte aos bancos de dados
  await client1.connect();
  await client2.connect();
  await reset(client1)
  await reset(client2)

  const tunning_list = [
    [tuningScenario1Query1, tuningScenario1Query2],
    [tuningScenario2Query1],
    [tuningScenario3Query1, tuningScenario3Query2, tuningScenario3Query3],
  ]

  const indexes_list = [indexScenario1Query, indexScenario2Query, indexScenario3Query]

  if (TUNNING_SCENARIO > 0){
    console.log("Starting Tunning")

    for (let i = 0; i < tunning_list[TUNNING_SCENARIO-1].length; i++){
      await client1.query(tunning_list[TUNNING_SCENARIO-1][i])
      await client2.query(tunning_list[TUNNING_SCENARIO-1][i])
    }
    console.log("Finished Tuning")
  }


  if (INDEX_SCENARIO > 0){
    console.log(INDEX_SCENARIO)
    await Promise.all([
      client1.query(indexes_list[INDEX_SCENARIO-1]),
      client2.query(indexes_list[INDEX_SCENARIO-1])
    ])
  }

  console.log(`TUNNING SCENARIO: ${TUNNING_SCENARIO} | INDEX SCENARIO: ${INDEX_SCENARIO}\n`)


  try {
    // Execute as consultas em paralelo
    await Promise.all([
      ...queries.map((query,index) => executeQuery(clients[index%2], query, 'lab', index+1)),
    ]);
  } finally {
    // Feche as conexões
    await reset(client1)
    await reset(client2)
    await client1.end();
    await client2.end();
  }

  
}

// Execute o programa principal
main().catch((error) => console.error('Error in main:', error));
