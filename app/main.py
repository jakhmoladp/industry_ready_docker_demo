from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome_page():
    return "<h2>Welcome!</h2><p> This is a demo application.</p>"

@app.get("/{username}")
def welcome_user(username):
    return {"message": f'Greetings! {username}!. Welcome to this Docker Demo! '}