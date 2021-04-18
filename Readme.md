Create virtual env 

```powershell
python -m venv env-name
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