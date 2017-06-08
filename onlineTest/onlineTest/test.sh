SED_CMD="s/'USER': 'root'/'USER': '123'/g"
SED_CMD2="s/'PASSWORD': 'ROOT'/'PASSWORD': '1278'/g"
sed $SED_CMD settings.py |>settings.py