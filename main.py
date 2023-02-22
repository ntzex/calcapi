from fastapi import FastAPI

api = FastAPI()


@api.get("/sum/{n1}/{n2}")
async def summary(n1: int, n2: int):
    return {"status": "ok", "result": n1+n2}


@api.get("/sub/{n1}/{n2}")
async def substract(n1: int, n2: int):
    return {"status": "ok", "result": n1-n2}


@api.get("/mult/{n1}/{n2}")
async def multiply(n1: int, n2: int):
    return {"status": "ok", "result": n1*n2}


@api.get("/div/{n1}/{n2}")
async def divide(n1: int, n2: int):
    if (n2 != 0):
        return {"status": "ok", "result": n1/n2}
    else:
        return {"status": "fail", "msg": "You cannot divide by 0!"}
