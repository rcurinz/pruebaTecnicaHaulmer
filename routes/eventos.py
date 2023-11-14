import json
from flask import Blueprint, jsonify, request
from models import *
eventos = Blueprint('eventos', __name__, url_prefix='/eventos')


# all events
@eventos.route('/events', methods=['GET'])
def get_events():
    eventos = Events.query.all()
    data = []
    for event in eventos:
        data.append({
            'id': event.id,
            'name': event.name,
            'start_hour': event.start_hour,
            'date': event.date,
            'place': event.place,
            'price': event.price,
            'tickets_max': event.tickets_max,
            'tickets_sold': event.tickets_sold,
            'description': event.description
        })

    return jsonify(data)


# event by id
@eventos.route('/event/<id>', methods=['GET'])
def get_event(id):
    evento = Events.query.filter_by(id=id).first()
    data = []
    data.append({
        'id': evento.id,
        'name': evento.name,
        'start_hour': evento.start_hour,
        'date': evento.date,
        'place': evento.place,
        'price': evento.price,
        'tickets_max': evento.tickets_max,
        'tickets_sold': evento.tickets_sold,
        'description': evento.description
    })

    return jsonify(data)


# sell ticket
@eventos.route('/purchase', methods=['POST'])
def sell_ticket():
    try:
        data = request.get_json()
        id_event = int(data.get('id_event'))
        id_client = int(data.get('id_client'))

        event = Events.query.filter_by(id=id_event).first()

        if event and event.tickets_sold < event.tickets_max:
            # agregar compra a la base de datos
            compra = Purchases(event_id=id_event, client_id=id_client, quantity=1)
            db.session.add(compra)

            event.tickets_sold += 1

            # realizar los cambios en la base de datos
            db.session.commit()

            return jsonify({'message': 'Ticket vendido'})
        else:
            return jsonify({'message': 'No hay más tickets o evento no encontrado'})

    except Exception as e:
        # Si ocurre un error, realiza un rollback para deshacer cualquier cambio en la transacción actual
        db.session.rollback()
        print(e)
        return jsonify({'error': 'Error interno del servidor'}), 500


# list purchases by client
@eventos.route('/orders/<id>', methods=['GET'])
def list_purchases(id):
    # obtener toda la información de las compras del cliente
    purchases = Purchases.query.filter_by(client_id=id).all()

    data = []
    for purchase in purchases:
        event = Events.query.filter_by(id=purchase.event_id).first()
        data.append({
            'id': purchase.id,
            'event_id': purchase.event_id,
            'client_id': purchase.client_id,
            'quantity': purchase.quantity,
            'event': {
                'id': event.id,
                'name': event.name,
                'start_hour': event.start_hour,
                'date': event.date,
                'place': event.place,
                'price': event.price,
                'tickets_max': event.tickets_max,
                'tickets_sold': event.tickets_sold,
                'description': event.description
            }
        })

    return jsonify(data)


# get all clients
@eventos.route('/clients', methods=['GET'])
def get_clients():
    clientes = Clients.query.all()
    data = []
    for cliente in clientes:
        data.append({
            'id': cliente.id,
            'name': cliente.first_name,
            'last_name': cliente.last_name,
            'email': cliente.email,
            'address': cliente.address
        })

    return jsonify(data)
