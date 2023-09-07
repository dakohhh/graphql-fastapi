import strawberry
from pprint import pprint
from .schema import UserInput, UserType, UserReturnType
from models.model import UserField
from repository.user import UserRepository




@strawberry.type
class Mutation:


    @strawberry.mutation
    async def create_user(self, user_input: UserInput) -> UserReturnType:

        # Validate user input with pydantic
        user_field = UserField(
            firstname=user_input.firstname, 
            lastname=user_input.lastname, 
            email=user_input.email, 
            password=user_input.password)


        user  = await UserRepository.create_user(user_field)

        return UserReturnType(**user)
    





