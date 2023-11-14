# Prueba Tecnica Haulmer

## Descripción
Prueba técnica para Haulmer

## Ejecución
Para ejecutar el proyecto se debe crear la imagen de docker con el siguiente comando:
```
docker build -t pruebatecnica .
```
Luego se debe ejecutar el contenedor con el siguiente comando:
```
docker run -p 5001:5001 pruebatecnica
```

## Collection de Postman
Se adjunta una collection de Postman con los endpoints del proyecto.
Con nombre: 
- EventosPruebaTecnica.postman_collection.json


## Uso
Para usar el proyecto se debe hacer una petición GET a la siguiente URL:
```
http://localhost:5001/eventos/getevents
```
La respuesta debe tener el siguiente formato:
```
[   
    {
        "date": "15-11-2023",
        "description": "Graduacion de alumnos de 4° medio",
        "id": 1,
        "name": "Evento de graduacion",
        "place": "Gimnacio municipal",
        "price": 10000,
        "start_hour": "10:00",
        "tickets_max": 150,
        "tickets_sold": 1
    }
]
```

Donde los campos son:
- date: Fecha del evento
- description: Descripción del evento
- id: Identificador del evento
- name: Nombre del evento
- place: Lugar del evento
- price: Precio del evento
- start_hour: Hora de inicio del evento
- tickets_max: Cantidad máxima de tickets
- tickets_sold: Cantidad de tickets vendidos


Para comprar un ticket se debe hacer una petición POST a la siguiente URL:
```
http://localhost:5001/eventos/sellticket
```
La petición debe tener el siguiente formato:
```
{
    "id_client": "1",
    "id_event": "1"
}
```
Donde los campos son:
- id_client: Identificador del cliente
- id_event: Identificador del evento

La respuesta debe tener el siguiente formato:
```
{
    "message": "Ticket vendido con éxito"
}
```

Para obtener los tickets de un cliente se debe hacer una petición GET a la siguiente URL:
```
http://localhost:5001/eventos/orders/1
```
Donde el último número es el identificador del cliente.


La respuesta debe tener el siguiente formato:
```
[
{
        "client_id": 1,
        "event": {
            "date": "15-11-2023",
            "description": "Graduacion de alumnos de 4° medio",
            "id": 1,
            "name": "Evento de graduacion",
            "place": "Gimnacio municipal",
            "price": 10000,
            "start_hour": "10:00",
            "tickets_max": 150,
            "tickets_sold": 1
        },
        "event_id": 1,
        "id": 1,
        "quantity": 1
    }
]
```

Donde los campos son:
- client_id: Identificador del cliente
- event: Evento
- event_id: Identificador del evento
- id: Identificador del ticket
- quantity: Cantidad de tickets comprados (siempre será 1, ya que solo se puede comprar un ticket a la vez)



Para obtener la información de un evento se debe hacer una petición GET a la siguiente URL:
```
http://localhost:5001/eventos/getevent/3
```
Donde el último número es el identificador del evento.

La respuesta debe tener el siguiente formato:
```
{
    "date": "15-11-2023",
    "description": "Graduacion de alumnos de 4° medio",
    "id": 1,
    "name": "Evento de graduacion",
    "place": "Gimnacio municipal",
    "price": 10000,
    "start_hour": "10:00",
    "tickets_max": 150,
    "tickets_sold": 1
}
```

Donde los campos son:
- date: Fecha del evento
- description: Descripción del evento
- id: Identificador del evento
- name: Nombre del evento
- place: Lugar del evento
- price: Precio del evento
- start_hour: Hora de inicio del evento
- tickets_max: Cantidad máxima de tickets
- tickets_sold: Cantidad de tickets vendidos


Para listar todos los clientes se debe hacer una petición GET a la siguiente URL:
```
http://localhost:5001/eventos/getclients
```

La respuesta debe tener el siguiente formato:
```
[
    {
        "address": "Temuco",
        "email": "r@r.com",
        "id": 1,
        "last_name": "Curin",
        "name": "Rene"
    }
]
```

Donde los campos son:
- address: Dirección del cliente
- email: Correo electrónico del cliente
- id: Identificador del cliente
- last_name: Apellido del cliente
- name: Nombre del cliente


## Herramientas utilizadas
- Base de datos: SQLite
- Lenguaje de programación: Python
- Framework: Flask
- ORM: SQLAlchemy
