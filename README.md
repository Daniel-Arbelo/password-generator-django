# Generador de Contraseñas Seguras

Este es un generador de contraseñas seguras desarrollado en Django. Permite generar contraseñas personalizadas con opciones como números, símbolos y mayúsculas, además de evaluar su nivel de seguridad.

## 🚀 Demo

La aplicación está desplegada en Railway y puedes probarla aquí:  
🔗 [Generador de Contraseñas](https://web-production-c13ca.up.railway.app/)

## 📌 Características
- Generación de contraseñas seguras con opciones personalizables.
- Evaluación del nivel de seguridad de la contraseña.
- Opción para copiar la contraseña generada.

## 🛠 Instalación y configuración

### 1️⃣ Clonar el repositorio
```sh
git clone https://github.com/tuusuario/tu-repositorio.git
cd tu-repositorio
```

### 2️⃣ Crear un entorno virtual e instalar dependencias
```sh
python -m venv env
source env/bin/activate  # En Windows: env\\Scripts\\activate
pip install -r requirements.txt
```

### 3️⃣ Configurar Django
Asegúrate de agregar tu dominio en `ALLOWED_HOSTS` en `settings.py` si planeas desplegarlo:
```python
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'web-production-c13ca.up.railway.app']
```

### 4️⃣ Ejecutar el servidor
```sh
python manage.py runserver
```

## 🔧 Despliegue en Railway
1. **Subir el código a un repositorio en GitHub.**
2. **Crear un nuevo proyecto en [Railway](https://railway.app/).**
3. **Conectar el repositorio y configurar los ajustes:**  
   - Agregar las variables de entorno necesarias.
   - Definir el comando de inicio: `python manage.py migrate && gunicorn password_generator.wsgi:application`.
4. **Desplegar la aplicación y obtener la URL generada.**

## 📝 Licencia
Este proyecto está bajo la licencia MIT.

---

¡Espero que este `README.md` te sea útil! 🚀