from fastapi import FastAPI, Request, HTTPException, Response
from fastapi.templating import Jinja2Templates
from models import User, UserResponse
from function import func


app = FastAPI()

templates = Jinja2Templates(directory="templates")
@app.get("/")
async def root(request:Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/signin")
async def signin(request:Request):
    return templates.TemplateResponse("signin.html", {"request": request})

@app.post("/api/login", response_model=UserResponse)
async def signin(user:User, request:Request, response: Response):
    userToken = func(user.email, user.password)
    if not userToken:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    response.set_cookie(key="X-Authorization", value=userToken, httponly=True)
    return UserResponse(usertoken=userToken)
    

@app.get("/orchestrator")
async def orchestrator(request:Request):
    return templates.TemplateResponse("orchestrator.html", {"request": request})
