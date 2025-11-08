from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return "Hello world"

@app.get("/hello")
def html_hello():
    html = """
    <html>
        <head>
        <title>Моё первое web-приложение</title>
        </head>
        <body>
            <h1>Hello world</h1>
            <p>Наша первая страница</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html)

@app.get("/file")
def from_file():
    with open("templates/index.html", "r", encoding="utf-8") as fl:
        content = fl.read()
    return HTMLResponse(content=content)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)