#IDE type hints , data validation, JSON serilisation
from pydantic import BaseModel , EmailStr , field_validator
class User (BaseModel):
    #fields of class
    name:str
    email:EmailStr
    account_id:int
#custom validation
    @field_validator("account_id")
    def field_validate_account_id(cls,value):
        if value <=0 :
             raise ValueError (f"account_id mst be positive :{value}")
        return value
user=User(name="Shirlyn",email="shirlynngure@gmail.com",account_id=-1234)
#IDE type hints(user...:name)
print(user)

#DATA VALIDATION
#user=User(name="Shirlyn",email="shirlynngure",account_id="hello")
#print(user)
#result to validation error,easier to debug

#JSON SERILIZATION(to from json)
#external application and api