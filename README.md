# Proyecto Base Django

Base minima en Django con autenticacion, login, logout y dashboard protegido.

## Requisitos

- Python 3.14
- Django 6.0.6

Las dependencias estan en `requirements.txt`.

## Instalacion

En Windows PowerShell:

```powershell
python -m venv env
.\env\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Configuracion

El proyecto funciona localmente con valores por defecto. Para configurar el entorno:

```powershell
$env:DJANGO_SECRET_KEY="cambia-esta-clave"
$env:DJANGO_DEBUG="True"
$env:DJANGO_ALLOWED_HOSTS="localhost,127.0.0.1"
```

Para produccion, usa una clave secreta real, `DJANGO_DEBUG=False` y define los dominios permitidos en `DJANGO_ALLOWED_HOSTS`.

## Base de datos

```powershell
.\env\Scripts\python.exe manage.py migrate
```

Para crear un administrador:

```powershell
.\env\Scripts\python.exe manage.py createsuperuser
```

## Ejecutar

```powershell
.\env\Scripts\python.exe manage.py runserver
```

Rutas principales:

- `/` redirige al dashboard.
- `/login/` inicia sesion.
- `/logout/` cierra sesion.
- `/dashboard/` muestra el panel protegido.
- `/admin/` abre el administrador de Django.

## Pruebas

```powershell
.\env\Scripts\python.exe manage.py test
```

## Estructura

- `config/`: configuracion principal del proyecto.
- `core/`: aplicacion base con vistas, rutas y pruebas.
- `templates/`: plantillas HTML compartidas y de autenticacion.
