import graphene


class CreateUserInput(graphene.InputObjectType):
    username = graphene.String(required=True)
    email = graphene.String(required=True)
