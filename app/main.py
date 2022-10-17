from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome_page():
    return {"message": "Hello Docker!"}

@app.get("/{username}")
def welcome_user(username):
    return {"message": f'Greetings! {username} Ji!. Welcome to this Docker Demo! '}