Sistema de Gestión de Restaurante - Semana 14

Propósito de la Semana 14

El propósito de esta actividad es evolucionar la aplicación gráfica `restaurante_app` mediante el uso adecuado de componentes, contenedores y gestores de geometría de Tkinter/ttk. Se busca mejorar la experiencia de usuario (UX) ofreciendo una interfaz organizada mediante formularios y tablas, manteniendo la arquitectura modular, la persistencia en archivos JSON y la separación estricta de responsabilidades sin recargar la capa visual con lógica de negocio.

Estructura del Proyecto

restaurante_app/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── main.py
└── README.md

Componentes y Contenedores Utilizados

Contenedores:

ttk.Notebook: Gestión de la navegación principal mediante pestañas separadas (Gestión de Productos y Consulta de Usuarios).

ttk.LabelFrame: Organización contenedora para agrupar visualmente el formulario de ingreso y las tablas de datos.

ttk.Frame: Estructuración de la barra superior de usuario y contenedores de botones de acción.

Componentes de Interfaz:

ttk.Entry: Campos de entrada de texto para ID, Nombre y Precio.

ttk.Combobox: Control desplegable de selección de categoría de producto.

ttk.Treeview y ttk.Scrollbar: Tablas avanzadas para visualización de registros con desplazamiento vertical.

ttk.Button: Botones de comando vinculados explícitamente mediante el parámetro command=.

Mejoras Realizadas en la Interfaz

Distribución Limpia y Modular: Organización mediante un diseño de dos paneles (Formulario a la izquierda y Tabla de visualización a la derecha) dentro de la sección de productos.

Encabezado Informativo: Barra superior persistente que muestra la aplicación y el usuario que ha iniciado sesión junto con su rol.

Pestaña de Usuarios: Incorporación de una pestaña dedicada a la consulta en tiempo real de los usuarios registrados en el sistema.

Limpieza Automática: Reseteo dinámico de los campos del formulario tras completar exitosamente una operación.

Operaciones Implementadas sobre Productos

Registrar: Captura los datos ingresados en el formulario y agrega un nuevo producto a la lista.

Cargar / Consultar: Permite buscar un producto mediante su identificador (ID) y rellenar automáticamente los campos del formulario con su información.

Actualizar: Modifica la información del producto previamente cargado o indicado.

Eliminar: Remueve el producto seleccionado del sistema previa confirmación de usuario.

Persistencia Utilizada

La persistencia se gestiona mediante archivos en formato JSON (productos.json y usuarios.json).

Separación de Responsabilidades: La capa de interfaz (ui/main_view.py) no manipula ni lee directamente los archivos JSON.

Toda solicitud de lectura, modificación o guardado de datos se solicita directamente a la capa de servicios (RestauranteServicio y ArchivoServicio), garantizando que la información persista al cerrar y reabrir la aplicación.

Pasos Necesarios para Ejecutar main.py

Clone o descargue el repositorio en su equipo local.

Asegúrese de contar con Python 3.x instalado.

Abra una terminal o consola de comandos en la carpeta raíz del proyecto (restaurante_app).

Ejecute el siguiente comando:

Bash
python main.py
Inicie sesión utilizando las credenciales predeterminadas:

Usuario: admin

Contraseña: 123