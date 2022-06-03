from datetime import datetime

# from mongoengine import connect, Document, DateTimeField, StringField, SequenceField
from mongoengine import connect
from mongoengine import Document
from mongoengine import DateTimeField
from mongoengine import StringField
from mongoengine import SequenceField


# Mongo E operações
# Conectar
# connect(db="mongomock", host="mongomock://localhost")
connect(host="mongodb://root:example@localhost:27017/my_db?authSource=admin")


# Subir um mongo com Docker:
"""
docker run --name some-mongo -d mongo:latest
nerdctl run --name some-mongo -d mongo:latest
"""


# Document Model


class Customer(Document):
    sequential = SequenceField(required=True)
    name = StringField(required=True)
    created_at = DateTimeField(required=True, default=datetime.now())

    meta = {
        "collection": "my_project_customers",
        "indexes": [
            {"fields": ["name", "created_at"]},
            "name",
            "created_at"],
    }

# Salvar

# data = {"name": "Fulano"}
# Customer(**data).save()
#
#
# Customer(**{"name": "Fulaninho"}).save()
#
#
# customer = Customer()
# customer.name = "Fulanao"
# customer.save()


# Buscar

# Object:
# print(Customer.objects().all())
# print(Customer.objects().first())
# customer = Customer.objects(name="Fulano").first()
# print(customer.name)
# customer_list = Customer.objects().order_by("-sequential").all()

# for customer in customer_list:
#     print(customer.sequential)

# Alterar

# customer = Customer.objects(name="Fulano").first()
# print(customer.name)
# customer.name = "João"
# customer.save()


###deletar???
customer = Customer.objects(name="João").first()
customer.delete()
