
# 🍽️ Smart Food 💪

Smart Food es una aplicación web desarrollada con Django que permite a los usuarios crear, editar y compartir recetas saludables. Diseñada con un enfoque moderno y funcional, combina Bootstrap con estilos personalizados para una experiencia profesional e intuitiva.

---

## 🚀 Funcionalidades principales

- ✅ Registro e inicio de sesión de usuarios.
- ✅ Perfil de usuario editable con avatar, biografía, redes sociales y más.
- ✅ Crear, ver, editar y eliminar recetas.
- ✅ Página pública con todas las recetas.
- ✅ Página privada con solo “Mis recetas”.
- ✅ Vista de detalle para cada receta.
- ✅ Cambio de contraseña desde el perfil.
- ✅ Panel administrativo de Django.

---

## 🧪 Tecnologías utilizadas

- Python + Django
- HTML5 + CSS3
- Bootstrap 5.3
- SQLite3 (base de datos por defecto)

---

## 🛠️ Instalación y ejecución

1. **Clona este repositorio:**

```bash
git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
cd TU_REPOSITORIO
```

2. **Crea y activa un entorno virtual:**

```bash
python -m venv env
# En Windows:
env\Scripts\activate
# En Mac/Linux:
source env/bin/activate
```

3. **Instala las dependencias:**

```bash
pip install -r requirements.txt
```

4. **Ejecuta las migraciones y corre el servidor:**

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

5. **Abre en tu navegador:**

```
http://localhost:8000
```

---

## 🧪 Usuario admin

Puedes crear un superusuario para ingresar al panel de administración:

```bash
python manage.py createsuperuser
```

---

## 📝 Notas

- Asegúrate de tener configurado `.gitignore` con las carpetas `env/`, `media/`, y demás archivos temporales.
- Las imágenes de los usuarios y recetas se guardan en `/media`.

---

## 🎥 Video de presentación

*Pendiente de grabación y entrega.*

---

## 👨🏻‍🎓 Autor

Desarrollado por Omar Velásquez como proyecto final del curso de Python con Django.
