import graphql_jwt
import graphene
from django.contrib.auth import get_user_model

from users.inputs import CreateUserInput
from users.types import UserType


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)
    ok = graphene.Boolean(required=True)
    errors = graphene.List(graphene.String, required=True)

    class Arguments:
        create_input = CreateUserInput(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, create_input, password):
        user = get_user_model()(**create_input)
        user.set_password(password)
        user.save()

        return CreateUser(user=user, ok=True, errors=[])


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    create_user = CreateUser.Field()

# class Mutation(graphene.ObjectType):
#     pass
