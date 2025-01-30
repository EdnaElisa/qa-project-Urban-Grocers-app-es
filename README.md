SPRINT 7
EDNA ELISA RIOS ACEVEDO
PROYECTO URBAN GROCERS

El objetivo de este proyecto es comprobar cómo la aplicación Urban Grocers crea kits de productos. Se han creado varias listas de comprobación,
una de ellas es para el campo name en la solicitud de creación de un kit de productos; la tarea es automatizar las pruebas, cargar el código en GitHub y enviar el repositorio a revisión.

DOCUMENTACIÓN:

Abre la documentación para estudiar la API de la aplicación de Urban Grocers: <the url of the launched server>/docs/.
Busca "Main.Kits" →" Crear un kit.” (/api/v1/kits)


CREACIÓN DE UN KIT PARA EL USUARIO(A):

Vas a crear un kit dentro de un usuario o usuaria particular, no una tarjeta. Para ello, sigue estos pasos:
Envía una solicitud para crear un nuevo usuario o usuaria y recuerda el token de autenticación (authToken).
Envía una solicitud para crear un kit personal para este usuario o usuaria. Asegúrate de pasar también el encabezado Autorization.


LISTA DE COMPROBACIÓN

№		
1	DESCRIPCION: El número permitido de caracteres (1): kit_body = { "name": "a"}	
ER: Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud

2	DESCRIPCION: El número permitido de caracteres (511): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"}	
ER: Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud

3	DESCRIPCION: El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }	
ER: Código de respuesta: 400

4	DESCRIPCION: El número de caracteres es mayor que la cantidad permitida (512): 
kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” }	
ER: Código de respuesta: 400

5	DESCRIPCION: Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }	
ER: Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud

6	DESCRIPCION: Se permiten espacios: kit_body = { "name": " A Aaa " }	
ER: Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud

7	DESCRIPCION: Se permiten números: kit_body = { "name": "123" }	
ER: Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud

8	DESCRIPCION: El parámetro no se pasa en la solicitud: kit_body = { }	
ER: Código de respuesta: 400

9	DESCRIPCION: Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }	
ER: Código de respuesta: 400


PAQUETES INSTALADOS 

* requests
* pytest

6 ARCHIVOS DEL PROYECTO:

configuration.py: almacenamiento de las rutas del archivo
data.py: cuerpos de la solicitud POST
sender_stand_request.py
create_kit_name_kit_test.py
README.md: información descriptiva del proyecto
.gitignore: archivos a ignorar en el repositorio


ENVÍO DE LAS SOLICITUDES: 

Todas las solicitudes que necesitas para resolver la tarea se pueden almacenar en el archivo sender_stand_request.py.
Copia la solicitud para crear un nuevo usuario o usuaria de la lección sobre solicitudes POST.
La función para crear un nuevo kit de producto puede denominarse post_new_client_kit
Utiliza dos parámetros en la función para crear un nuevo kit de producto: kit_body (el cuerpo de solicitud) y auth_token (el token de autenticación).
Si utilizas el diccionario de datos del archivo data.py una vez más, aplícale la función copy(). Es mejor no hacer ningún cambio en el diccionario de origen, ya que esto puede generar errores.
Si la solicitud se envía con un error, comprueba las barras (//), especialmente las del final.


PRUEBAS:

La lista de comprobación completa debe estar en el archivo create_kit_name_kit_test.py.
Lo ideal es que especifiques los archivos y directorios para iniciar Pytest. De lo contrario, Pytest buscará las pruebas en el directorio y los subdirectorios de trabajo actuales. Necesita los archivos que comienzan con test_ o terminan con _test. La búsqueda no distingue entre mayúsculas y minúsculas, por lo que puede encontrar tanto Test_1.py como test_1.py.
Puedes crear una función que cambiará el contenido del cuerpo de solicitud, nómbrala get_kit_body y agrega el parámetro name.
Hay dos tipos de pruebas en la lista de comprobación: positivas y negativas (código 400). Su lógica se puede expresar en funciones separadas: positive_assert(kit_body) y negative_assert_code_400(kit_body):.
Recibir el token también puede ser una función separada. Llámala get_new_user_token().
Cada prueba debe estar en una función separada con el prefijo test, de lo contrario, Pytest las ignorará.


#INFORMACIÓN A COMPLETAR

El proyecto se realizó a través de PyCharm, terminal y Github.

Se creó repositorio en Github llamado: qa-project-Urban-Grocers-app-es.
Terminal: se creó carpeta "projects" a traves del comando *mkdir projects* donde se guardó el proyecto.
Se realizó clonacion del repositorio por SSH: git clone git@github.com:EdnaElisa/qa-project-Urban-Grocers-app-es.git

Se instaló git a través de homebrew en la terminal: brew install git
Continuamos para la actualizacion del código: 
git init: inicialización 
git add .: para agregar los nuevos archivos o actualizaciones del codigo
git commit -m "Proyecto Sprint 7"

Se enviaron correciones: para actualizar repositorio se ejecutó el comando: git push origin main
