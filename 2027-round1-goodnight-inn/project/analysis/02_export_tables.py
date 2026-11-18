import sys, os
from pbixray import PBIXRay
m = PBIXRay(sys.argv[1]); out = sys.argv[2]; os.makedirs(out, exist_ok=True)
for t in m.tables:
    df = m.get_table(t); df.to_parquet(os.path.join(out, f"{t}.parquet")); print(t, df.shape)
