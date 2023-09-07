from database.schema import User
from utils.validate_bson import get_object_id
from mongoengine.errors import MongoEngineException
from models.model import UserField
from exceptions.custom_exception import BadRequestException, ServerErrorException




class UserRepository:

    @staticmethod
    async def create_user(user_model:UserField):

        try:

            user = User(
                firstname=user_model.firstname,
                lastname = user_model.lastname, 
                email = user_model.email,
                password = user_model.password)
            
            user.save()

            return user.to_dict()
        
        except MongoEngineException as e:

            raise BadRequestException(str(e))
        
        except Exception as e:

            raise ServerErrorException(str(e))

    @staticmethod
    async def get_by_id(user_id:str):

        try:

            user_id = get_object_id(user_id)

            user = User(id=user_id)

            return user.to_dict()


        except MongoEngineException as e:

            raise BadRequestException(str(e))
        
        except Exception as e:

            raise ServerErrorException(str(e))
        
    

    @staticmethod
    async def get_all():

        try:

            all_users = [user.to_dict() for user in User.objects.all()]

            return all_users


        except MongoEngineException as e:

            raise BadRequestException(str(e))
        
        except Exception as e:

            raise ServerErrorException(str(e))


    