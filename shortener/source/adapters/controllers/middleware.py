from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt

from source.infraestructure.env import jwt_secret

class BearerTokenAuthBackend(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(BearerTokenAuthBackend, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        # do something with the request object, for example
        credentials: HTTPAuthorizationCredentials = await super(BearerTokenAuthBackend, self).__call__(request)
        if credentials:
            
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication token.")
            validated_jwt = self.verify_jwt(credentials.credentials)
            if not validated_jwt:
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            return validated_jwt.get("user_id")
        else:
            raise HTTPException(status_code=403, detail="Credentials not found.")
        
    def verify_jwt(self, jwtoken: str) -> dict:
        decoded_token = jwt.decode(jwtoken, jwt_secret, algorithms=["HS256"])
        return decoded_token        
