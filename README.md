# 🔑 Generador de Contraseñas Seguras

Este es un generador de contraseñas seguras desarrollado con **Django**. Permite crear contraseñas aleatorias según los criterios seleccionados y evalúa su nivel de seguridad.

---

## 🌐 Demo en Vivo

Puedes probar el generador de contraseñas en la siguiente URL:  
[Demo del Generador de Contraseñas](https://web-production-c13ca.up.railway.app)


## 🚀 Características

✅ Generación de contraseñas seguras con:
- Longitud personalizable
- Inclusión opcional de números, símbolos y mayúsculas

✅ Evaluación de seguridad con **zxcvbn**

✅ Interfaz moderna con **Bootstrap**

✅ Copiar contraseña con un solo clic

---

## 📂 Instalación y Configuración

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/Daniel-Arbelo/password-generator-django.git
cd generador-contrasenas
```

### 2️⃣ Crear y activar un entorno virtual
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4️⃣ Ejecutar migraciones
```bash
python manage.py migrate
```

### 5️⃣ Iniciar el servidor
```bash
python manage.py runserver
```
Accede en tu navegador a: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🛠 Tecnologías Usadas
- **Django** - Framework principal
- **Bootstrap 5** - Estilos y componentes
- **zxcvbn** - Evaluación de seguridad de contraseñas

---

## 📜 Endpoints

| Método | URL | Descripción |
|---------|----------------------|------------------------------|
| GET | `/` | Página principal |
| POST | `/` | Genera y muestra una contraseña |
| GET | `/api/generar` | Devuelve una contraseña en JSON |

---

## 📌 Mejoras Futuras
- ✅ Personalización avanzada de exclusión de caracteres
- ✅ Implementación de una API con autenticación
- ✅ Guardado seguro de contraseñas en una base de datos

---

## 📜 Licencia
Este proyecto está bajo la licencia **MIT**.

💻 Desarrollado por Daniel Arbelo Hernández 🚀

