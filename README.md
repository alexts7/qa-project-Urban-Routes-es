INDICE
-DESCRIPCIÓN
-LISTA DE COMPROBACIÓN
-ARCHIVOS DEL PROYECTO
-PAQUETES DE PYTHON
-COMANDOS DE EJECUCIÓN
-INSTRUCCIONES PARA LAS PRUEBAS

DESCRIPCION:
Este proyecto tiene como objetivo comprobar, mediante pruebas automatizadas, la funcionalidad de solicitud de taxi en la plataforma Urban Routes, específicamente para la tarifa Comfort. Se automatizan todos los pasos del proceso, desde la configuración de la ruta hasta la confirmación y llegada del taxista.

LISTA DE COMPROBACIÓN:
setup_class(cls): Configura las opciones del navegador.
test_set_route(self): Configura y verifica la dirección de la ruta.
test_click_call_taxi_button(self): Selecciona el botón para llamar al taxi.
test_select_comfort_rate(self): Selecciona y valida la tarifa Comfort.
set_select_number_button(self): Selecciona y rellena el número de teléfono.
add_number(self): Añade número de teléfono.
phone_number(self): Verifica el número de teléfono.
the_next_button(self): Avanza al siguiente paso.
code_number(self): Añade el código de verificación del teléfono.
payment_method(self): Configura y revisa los métodos de pago.
write_driver(self): Ingresa y confirma un mensaje personalizado para el conductor.
blanket_and_tissues(self): Selecciona y valida los requisitos adicionales (manta y pañuelos).
request_ice_cream(self): Selecciona la cantidad de helado.
search_taxi(self): Realiza la búsqueda de taxi y verifica que la orden se haya ejecutado.
test_wait_driver_details(self): Verifica la recepción de los detalles del conductor y que el viaje haya sido tomado.

LISTA DE COMPROBACIÓN DE PASOS:
URL de servidor
Configurar la dirección
Seleccionar personalización
Pedir taxi
Seleccionar la tarifa Comfort
Rellenar el número de teléfono
Agregar una tarjeta de crédito
Escribir un mensaje para el conductor
Pedir una manta y pañuelos
Pedir 2 helados
Aparece el modal: buscar un taxi
Esperar a que aparezca la información del conductor en el modal

ARCHIVOS DEL PROYECTO:
main.py
data.py
Urban_RoutesPage.py
SMS.py
README.md

PAQUETES DE PYTHON:
pip
pytest
requests


COMANDOS DE EJECUCIÓN:
Status
Branch
commit -m
Git
push
merge
stash
checkout master

INSTRUCCIONES PARA LAS PRUEBAS: 
1 Clona el repositorio de GitHub en tu PC.
2 Una vez que hayas vinculado tu cuenta de TripleTen con GitHub, se creará un repositorio automáticamente. El nombre del repositorio será qa-project-Urban-Routes-es Ve a GitHub y clona el nuevo repositorio en tu computadora local, siguiendo estos pasos: Abre tu terminal preferida. Si estás en Windows, deberás utilizar Git Bash. Si aún no lo has hecho, crea un directorio para almacenar todos tus proyectos.
3 Clona el repositorio.
4 Si usas un Sotfware como Pycharm ve a los paquetes e instala pip, pythes, requests
5 Comprobar que las pruebas funcionen con "run" en PyCharm
6 Hacer commit en GitHub
