Sistema de Inventario para la Librería "El Gran Poeta"

Descripción General

El sistema de inventario desarrollado para la librería El Gran Poeta es una aplicación web diseñada para gestionar productos. Proporciona herramientas para el control de inventarios, la generación de informes, y la administración de usuarios con roles específicos. Está implementado con Django como framework backend, MySQL como base de datos, y Bootstrap para la interfaz de usuario.

Colaboradores:
Eliseo Chavez


Damián Gutiérrez
https://github.com/DamianGutierrezLemus

Alfredo Hernández
https://github.com/Exoteklas

Funcionalidades

Gestión de Inventario

Creación, edición y eliminación de productos.

Registro de información detallada, como nombre, autor, stock, y descripción del producto.

Asociación de productos con bodegas específicas.

Movimientos de Productos

Transferencia de productos entre bodegas.

Generación de documentos de movimiento con detalles como:

Fecha del movimiento.

Bodega de origen y destino.

Usuario responsable del movimiento.

Gestión de Usuarios

Creación de perfiles con roles específicos:

Jefe de Bodegas: Gestión completa del inventario y generación de informes.

Bodeguero: Realización de movimientos entre bodegas.

Sistema de autenticación seguro con encriptación de contraseñas.

Redirección personalizada según el tipo de usuario.

Generación de Informes

Informes de cantidad de productos por bodega.

Listado de productos por editorial específica.

Historial de movimientos con detalles de fecha, bodegas involucradas y usuario responsable.

Restricciones de Seguridad

Impide la eliminación de:

Bodegas con productos asociados.

Productos asociados a movimientos.

Editoriales y autores con libros registrados.

Interfaz de Usuario

Diseño intuitivo y responsivo con Bootstrap.

Navegación simple y uso de colores para facilitar la comprensión.

Requisitos Técnicos

Software

Python: 3.8+

Django: 4.2+

MySQL: 8.0+

XAMPP: Para gestionar la base de datos localmente.

Bootstrap: 5.0+ para la interfaz.

Instalación

Clona el repositorio:

git clone https://github.com/EChavezDevs/ElGranPoeta

Instala las dependencias del proyecto:

pip install -r requirements.txt

Configura la base de datos en settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Libreria',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

Ejecuta las migraciones:

python manage.py makemigrations
python manage.py migrate

Inicia el servidor:

python manage.py runserver

Accede a la aplicación en tu navegador:
http://127.0.0.1:8000

Estructura del Proyecto

Gestor de Inventario: Módulo encargado de crear, actualizar y eliminar productos.

Gestor de Movimientos: Administra las transferencias de productos entre bodegas.

Gestor de Perfiles: El Administrador puede crear usuarios y asignar el rol.

Generador de Informes: Genera reportes personalizados de las bodegas.

Base de Datos: MySQL almacena toda la información del sistema.

Interfaz de Usuario: Diseño responsivo para una experiencia fluida.

Roles de Usuario

Administrador: Acceso completo al sistema, incluyendo la visualización de documentos de movimiento.

Jefe de Bodegas: Gestión de inventarios y generación de informes.

Bodeguero: Movimiento de productos para despacho.

Seguridad

Encriptación de contraseñas para proteger credenciales.

Control de acceso según roles.

Validación de datos para evitar inconsistencias.

