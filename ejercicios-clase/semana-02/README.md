# Semana 2

Como arme el entorno para este laboratorio:

```bash
python -m venv venv
venv\Scripts\activate
pip install matplotlib
pip freeze > requirements.txt
```

El venv se crea en la raiz del repo (no aca adentro) y no se sube a git, para eso esta el requirements.txt. Para reproducir el entorno en otra maquina: crear el venv, activarlo y correr `pip install -r requirements.txt` desde la raiz.
