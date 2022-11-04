#!/usr/bin/bash

set -euo pipefail

mkdir -p out

python3 normalize_kalpi.py --parties expb.csv > out/expb_parties.csv
python3 normalize_kalpi.py expb.csv > out/expb_results.csv

cd out

sqlite3 res.db ".read ../import_to_sqlite.sql"
sqlite3 res.db -csv ".read ../query.sql" > bibi.csv
