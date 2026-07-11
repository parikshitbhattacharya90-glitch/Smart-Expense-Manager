from pydantic import BaseModel, Field, field_validator, model_validator


class RegisterUser(BaseModel):
    username : str = Field(
    min_length=3,
    max_length=30,
    pattern=r"^[A-Za-z][A-Za-z0-9_]*$"                 # ^ means start, * indicates remaining letters, $ means end
    ) 


    password : str
    confirm_password : str


    @field_validator("password")                     # For one field, we need field validator, 
    @classmethod
    def validate_password(cls, password):
        if not password:
            raise ValueError(
                "Password must not be empty"
            )
        if len(password) < 8:
            raise ValueError(
                "Password must contain at least 8 characters"
            )
        
        if not any(char.isupper() for char in password):
            raise ValueError(
                "Password must contain at least one capital letter"
            )
        
        if not any(char.isdigit() for char in password):
            raise ValueError(
                "Password must contain at least one digit"
            )
        
        if password.isalnum():
            raise ValueError(
                "Password must contain at least one special character"
            )
        
        return password
        

    @model_validator(mode="after")                                # To compare multiple fields, we need model validator
    def validate_confirm_password(self):

        if self.password != self.confirm_password:
            raise ValueError(
                "Passwords do not match"
            )

        return self





                      
