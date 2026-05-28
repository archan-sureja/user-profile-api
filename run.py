import uvicorn 
from main import app 
from config import settings 
port = settings.BACKEND_PORT 
if __name__ == "__main__":
        uvicorn.run(
            app,
            host="0.0.0.0",
            port=port 
        )