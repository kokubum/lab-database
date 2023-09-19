import fam
import pess
import mun
import psycopg2

# creating the connection
conn = psycopg2.connect(
  database="lab",
  user="lab_user",
  password="lab_password",
  host="localhost",
  port="5432"
)

conn.autocommit = True 
cursor = conn.cursor()

# Setup of the "municipios" table
cursor.execute(mun.sql_create_table_mun)
print("Mun table created successfully!\n")

cursor.execute(mun.sql_copy_csv_mun)
print("Mun table populated successfully!\n")

# Setup of the "tb_familia" and "tb_domicilio" tables
cursor.execute(fam.sql_create_staging_table_fam)
print("Staging fam table created successfully!\n")

cursor.execute(fam.sql_copy_csv_fam)
print("Staging fam table populated from csv files successfully!\n")

cursor.execute(fam.sql_create_table_fam)
print("Fam table created successfully!\n")

cursor.execute(fam.sql_create_table_dom)
print("Dom table created successfully!\n")

cursor.execute(fam.sql_populating_table_fam)
print("Fam table populated successfully!\n")

cursor.execute(fam.sql_populating_table_dom)
print("Dom table populated successfully!\n")

cursor.execute(fam.sql_drop_staging)
print("Drop staging successfully!\n")

# Setup of the "tb_pessoa", "tb_escolaridade" and "tb_trabalho_remun" tables
cursor.execute(pess.sql_create_staging_table_pess)
print("Staging pess table created successfully!\n")

cursor.execute(pess.sql_copy_csv_pess)
print("Staging pess table populated from csv files successfully!\n")

cursor.execute(pess.sql_create_table_esc)
print("Esc table created successfully!\n")

cursor.execute(pess.sql_create_table_pess)
print("Pess table created successfully!\n")

cursor.execute(pess.sql_create_table_trab)
print("Trab table created successfully!\n")

cursor.execute(pess.sql_populating_table_esc)
print("Esc table populated successfully!\n")

cursor.execute(pess.sql_populating_table_pess)
print("Pess table populated successfully!\n")

cursor.execute(pess.sql_populating_table_trab)
print("Trab table populated successfully!\n")

cursor.execute(pess.sql_drop_staging)
print("Drop staging successfully!\n")

conn.close()
print("DONE!\n")