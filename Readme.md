Create virtual env 

```powershell
python -m venv env-name
```

Create requirements file

```powershell
pip freeze > requirements.txt
```

# Run flask app

Setting env variables

```powershell
$env:FLASK_APP = "entrypoint_name.py"
```

```powershell
$env:FLASK_env = "development"
```

```powershell
flask run
```
