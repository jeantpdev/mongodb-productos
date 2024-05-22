# Tienda de productos - API

## Informacion general

Una tienda de productos que permite agregar productos al carrito Y realizar el pedido. Se recibe un correo con los datos del pedido 
realizado tanto para el cliente como para el administrador del sitio.

Cuenta con 2 aplicativos web los cuales son:

* **Tienda de productos**: Es la pagina que va a contener todos los productos
disponibles para comprar

* **Dashboard**: Permite controlar el inventario de los productos pudiendo eliminar
editar o agregar nuevos productos

Y un backend:

* **Productos**: Es la API que nos permite hacer las consultas a la BD y poder mostrarla a la pagina.
Va a contener todas las funciones relacionadas a eliminar, agregar o editar

## Funciones

* Ver productos disponibles
* Agregar productos al carrito
* Eliminar productos del carrito
* Enviar productos del carrito al administrador del sitio

## Repositorios

Tienda [Repositorio Tienda](https://github.com/jeantpdev/tienda-landingPage).

Dashboard [Repositorio Dashboard](https://github.com/jeantpdev/admin-dashboard).

API - Productos [Repositorio Backend](https://github.com/jeantpdev/mongodb-productos).

## Tecnologias a usar

**Frontend**:
  * Astro
  * React
    
**Backend**:
  * Python
  * Flask
    
**Base de datos**:
  * MongoDB
  
**Hosting**:
  * Pagina: Vercel o Netlify
  * API: Render o PythonAnyWhere

**Documentación**:
  * Api: Swagger
  * Pagina web: Notion o Obsidian
    
**Otros**:
 * Cloudinary: Servicio para subir multimedia
 * JWT: Autenticacion del usuario

## Flujo de trabajos:

VACIO

## Diagramas de flujo:

### Ver productos
![Diagrama ver productos](https://res.cloudinary.com/dkuw4zg2h/image/upload/f_auto,q_auto/Joyeria/Diagramas%20de%20flujo/ver-productos.png)

### Insertar productos
![Diagrama ver productos](https://res.cloudinary.com/dkuw4zg2h/image/upload/f_auto,q_auto/Joyeria/Diagramas%20de%20flujo/insertar-productos.png)

### Iniciar sesion
![Diagrama ver productos](https://res.cloudinary.com/dkuw4zg2h/image/upload/f_auto,q_auto/Joyeria/Diagramas%20de%20flujo/iniciar-sesion.png)
