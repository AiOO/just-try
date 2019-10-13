import graphene
from graphene.relay import Connection, Node
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from .models import Customer, Scooter, db_session


class CustomerNode(SQLAlchemyObjectType):
    class Meta:
        model = Customer
        interfaces = (Node, )


class CustomerConnection(Connection):
    class Meta:
        node = CustomerNode


class ScooterNode(SQLAlchemyObjectType):
    class Meta:
        model = Scooter
        interfaces = (Node, )


class ScooterConnection(Connection):
    class Meta:
        node = ScooterNode


class Query(graphene.ObjectType):
    node = Node.Field()
    all_customers = SQLAlchemyConnectionField(CustomerConnection)
    all_scooters = SQLAlchemyConnectionField(ScooterConnection, sort=None)


schema = graphene.Schema(query=Query)
