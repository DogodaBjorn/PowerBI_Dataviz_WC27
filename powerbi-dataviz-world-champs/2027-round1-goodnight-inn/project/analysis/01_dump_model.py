import sys, pandas as pd
from pbixray import PBIXRay
pd.set_option('display.width', 250); pd.set_option('display.max_columns', 40); pd.set_option('display.max_colwidth', 120); pd.set_option('display.max_rows', 400)
m = PBIXRay(sys.argv[1])
print("== TABLES"); print(m.tables)
print("== SIZE"); print(m.size)
print("== STATS"); print(m.statistics)
print("== SCHEMA"); print(m.schema)
print("== RELATIONSHIPS"); print(m.relationships)
print("== DAX MEASURES"); print(m.dax_measures.to_string())
print("== DAX COLUMNS"); print(m.dax_columns.to_string())
print("== DAX TABLES"); print(m.dax_tables.to_string())
print("== POWER QUERY")
for _, r in m.power_query.iterrows(): print("--", r['TableName']); print(r['Expression'])
try:
  print("== M PARAMS"); print(m.m_parameters)
except Exception as e: print(e)
