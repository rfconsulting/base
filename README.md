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

`DJANGO_SECRET_KEY` es obligatoria. Puedes definirla en un archivo `.env` local:

```env
DJANGO_SECRET_KEY=tu-clave-secreta
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
```

Tambien puedes configurar las variables desde PowerShell:

```powershell
$env:DJANGO_SECRET_KEY="cambia-esta-clave"
$env:DJANGO_DEBUG="True"
$env:DJANGO_ALLOWED_HOSTS="localhost,127.0.0.1"
```

Para produccion, usa una clave secreta real, `DJANGO_DEBUG=False` y define los dominios permitidos en `DJANGO_ALLOWED_HOSTS`.

## Clave secreta para produccion

Genera una clave aleatoria segura con Django:

```powershell
.\env\Scripts\python.exe -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Guarda el resultado como `DJANGO_SECRET_KEY` en el entorno del servidor o en el gestor de secretos de tu proveedor:

```env
DJANGO_SECRET_KEY=clave-generada
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=midominio.com,www.midominio.com
```

La clave se genera una sola vez por entorno y se conserva. No debe generarse automaticamente en cada arranque, porque invalidaria sesiones, tokens firmados y otros datos protegidos por Django.

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

## Estilos y frontend

La interfaz usa una hoja de estilos central en:

```text
static/css/styles.css
```

`templates/base.html` carga el CSS con el sistema de archivos estaticos de Django:

```django
{% load static %}
<link rel="stylesheet" href="{% static 'css/styles.css' %}">
```

`config/settings.py` incluye `STATICFILES_DIRS = [BASE_DIR / "static"]` para que Django encuentre los archivos dentro de la carpeta `static/` durante el desarrollo.

Los estilos actuales incluyen:

- Layout centrado con contenedor `app-shell`.
- Panel principal reutilizable con clase `panel`.
- Variables CSS para colores, sombras, radios y estados.
- Inputs con estados de foco accesibles.
- Botones y enlaces tipo boton con interaccion visual.
- Mensajes de error, aviso y estado con estilos diferenciados.
- Ajustes responsive para pantallas pequenas.

## Pruebas

```powershell
.\env\Scripts\python.exe manage.py test
```

## Estructura

- `config/`: configuracion principal del proyecto.
- `core/`: aplicacion base con vistas, rutas y pruebas.
- `static/`: archivos estaticos como CSS, imagenes o JavaScript.
- `templates/`: plantillas HTML compartidas y de autenticacion.
