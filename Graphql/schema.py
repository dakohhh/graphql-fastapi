import strawberry



@strawberry.type
class UserType:
    id:str
    user:str
    token:str



@strawberry.type
class UserReturnType:
    id:str
    firstname:str
    lastname:str
    email:str
    created_at:str
    updated_at:str




@strawberry.input
class UserInput:
    firstname:str
    lastname:str
    email:str
    password:str
