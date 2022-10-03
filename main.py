from fastapi import FastAPI
import uvicorn
from mylib.logic import wiki as wikilogic, phrase as wikiphrases, search

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Wikipedia API. Use functionalities up to your requirements."}


@app.get("/wikipedia/{name}")
async def wiki(name: str):
    """Retrieve wikipedia page"""

    page = wikilogic(name)
    return {"page": page}


@app.get("/search/{value}")
async def look_for(value: str):
    """Look for anything in wikipedia"""

    results = search(value)
    return {"result": results}


@app.get("/phrases/{name}")
async def phrase(name: str):
    """Retrieve wikipedia page"""

    phrases = wikiphrases(name)
    return {"page": phrases}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
