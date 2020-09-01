import graphene

from users.schema import Mutation as UserMutation


class Mutation(UserMutation):
    pass


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")


schema = graphene.Schema(query=Query, mutation=Mutation)
