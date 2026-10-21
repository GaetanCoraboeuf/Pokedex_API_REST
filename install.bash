!#/bin/bash
python3 -m venv .venv
source .venv/bin/activate
pip install fastapi[standard] requests
pip freeze > requirements.txt
python create_database.py

fastapi dev main.py