## Declarar las variables de entorno

Para que nuestro sitio web funcione de forma correcta, vamos a necesitar crear 3 variables de entorno, dos de ellas vendrán de nuestra wallet desde donde deseamos hacer "mint" de nuestro NFTs (en esa cuenta deben estar los tokens), la variable restante será nuestra secretkey para nuestro sitio web.

Esta secretkey nos ayuda a firmar toda la información sensible de nuestro sitio web (cookies y tokens), de igual forma nos ayuda a encriptar datos, asi como proteger sesiones y generar otras claves únicas.

Para generar esta clave, vamos a poner en la terminal:
```
python manage.py getsecretkey
```
Y nos va a generar una clave parecida a esto:
```
iji*ehx$6(*iq^(kvq)tezqy4qc!9$u7j2#l&z2=e+nb+)o7ny
```
Esta clave debemos copiarla para agregarla en nuestro archivo `.env` que ahora vamos a crear. En nuestro directorio root vamos a crear nuestro archivo .env, donde estará contenida todas nuestras variables de entorno, para ello, dentro de nuestro archivo escribiremos lo siguiente:

```
SECRET_KEY=Código que generamos con anterioridad
ACCOUNT_ADDRESS=Dirección de nuestra wallet
PRIVATE_KEY=Llave privada de nuestra wallet
```
Guardamos nuestro archivo como `.env` (asi es, no lleva nombre, solo formato).

## Declarar host

En Django por temas de seguridad, también debemos informarle cual es la url del sitio donde estaremos hosteando nuestra página web, para ello nos vamos a dirigir al archivo de `settings.py`, en donde encontraremos las configuraciones de nuestra aplicación. Dentro de las configuraciones debemos buscar un apartado que se vea asi:

```
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
# Aquí debe de ir el nombre del dominio entre comillas   
]

```
Si deseamos correr nuestra aplicación en un host con un dominio establecido, debemos agregar en `ALLOWED_HOSTS = []` el nombre del dominio donde vamos a desplegar nuestra aplicación, y guardamos el archivo.

Por otro lado si deseamos correr nuestra aplicación en local, unicamente debemos cambiar `DEBUG = False` a `DEBUG = True`, y guardamos el archivo.

NOTA: Si vas poner `DEBUG = True`, ten en cuenta que este sitio no deberá ser desplegado ya que puede presentar problemas de seguridad, de igual forma el cambio de `ALLOWED_HOSTS = []` debe estar vacío, de lo contrario saltarán errores.

## Crear súper usuario

Django cuenta con un apartado para administradores, que será donde crearemos nuestros NFTs y donde podremos supervisar las wallets que ya han reclamado algún NFT. Para acceder a esta apartado es necesario crear una cuenta de administrador en nuestras bases de datos, para ello vamos a correr los siguientes comandos en nuestra terminal:

```
python manage.py makemigrations  #Crea los modelos de las bases de datos en caso de algún error
python manage.py migrate         #Agrega a nuestra aplicación las bases de datos creadas
python manage.py createsuperuser #Creamos nuestra cuenta de administrador
```

Este comando nos pedirá que asignemos un nombre de usuario a nuestra cuenta de administrador, asi como un correo y una contraseña, la terminal debe verse algo asi:

```
Username (leave blank to use 'admin'): admin
Email address: admin@example.com
Password:
Password (again):
Superuser created successfully.
```

## Correr nuestro sitio web

### Local

Si deseas correr tu sitio web que previamente a sido configurado para correr como servicio local, solo hace falta correr el siguiente comando en la termina, para desplegar nuestro sitio web:

```
python manage.py runserver
```

### Servidor

Para asegurarnos que nuestros archivos estáticos estén disponibles, debemos correr:

```
python manage.py collectstatic
```
Django no esta diseñado para correr en servidores con `runserver` por ende, debemos usar algún servidor de aplicaciones como Gunicorn, para ello debemos instalar esta librería corriendo el siguiente comando:

```
pip install gunicorn
```

Una vez instalado ya seremos capaces de correr el siguiente comando para hacer que Gunicorn escuche en todas las interfaces de red disponibles, si deseas cambiar el puerto puedes hacerlo en el siguiente comando, sustituyendo el 8000 por el puerto deseado:

```
gunicorn --bind 0.0.0.0:8080 Core_NFTs.wsgi
```

## ¿Cómo manejar el dominio?

Tu dominio debe estar configurado en el servidor DNS y en tu servidor web (como Nginx) para que apunte a la dirección IP del servidor donde está desplegado tu sitio.

Si tienes un dominio y ya está apuntando correctamente a tu servidor, Nginx puede encargarse de redirigir las solicitudes desde tudominio.com a Gunicorn, sin necesidad de cambiar el comando de Gunicorn.