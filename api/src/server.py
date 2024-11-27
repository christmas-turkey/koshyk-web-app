from fastapi import FastAPI

app = FastAPI()


@app.get("/healthcheck")
def healthcheck():
    """
    Check if the server is up and running
    """

    return {"description": "Server is up and running"}