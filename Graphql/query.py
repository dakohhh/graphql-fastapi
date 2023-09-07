import strawberry
from typing import List
from .schema import UserType
from repository.user import UserRepository




@strawberry.type
class Query:

    @strawberry.field
    def hello(self) ->str:
        return "Hello World"



    @strawberry.field
    async def get_all(self) -> List[UserType]:

        all_user = await UserRepository.get_all()

        return all_user
    

        