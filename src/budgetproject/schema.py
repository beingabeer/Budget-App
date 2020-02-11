import graphene
from core.schema import Query as products_query


class Query(products_query):
    pass


schema = graphene.Schema(query=Query)
