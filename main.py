from typing import Literal
from fastapi import FastAPI
from utils.extractor.gogo_extractor import get_m3u8
from utils.gogo import GoGoApi
from utils.db import DB
from fastapi.responses import FileResponse
from fastapi.openapi.utils import get_openapi
from utils.animeworldin import AnimeWorldIN
import aiohttp

app = FastAPI()

session = []
AIO_SESSIONS = 1


def get_session():
    session.sort(key=lambda i: i[1])
    ses = session[0]
    for i in session:
        if i == ses:
            session[session.index(i)][1] += 1

    return ses[0]


@app.on_event("startup")
async def startup_event():
    app.openapi_schema = get_openapi(
        title="FastAnimeApi",
        version="1.3",
        description="Use powerfull api features provided by AnimeApi",
        routes=app.routes,
    )

    print("Creating Aiohttp Sessions...")
    global session
    for i in range(AIO_SESSIONS):
        session.append([aiohttp.ClientSession(), 0])


@app.on_event("shutdown")
async def shutdown_event():
    for i in session:
        await i[0].close()


@app.get("/", name="home", tags=["Home"])
async def home():
    return {
        "status": "AnimeApi - Api is ready to work...",
        "documentation": "/docs",
    }



# Gogoanime


@app.get("/gogo/latest", name="gogo latest", tags=["Gogo Anime"])
async def gogo_latest(api_key: str, page: int = 1):
    """Get latest released animes from gogoanime

    - page: Page number (default: 1)

    Price: 1 credits"""
    if not await DB.is_user(api_key):
        return {"success": False, "error": "Invalid api key"}

    try:
        await DB.reduce_credits(api_key, 1)
    except Exception as e:
        pass

    data = await GoGoApi(get_session()).latest(page)
    return {"success": True, "results": data}


@app.get("/gogo/search", name="gogo search", tags=["Gogo Anime"])
async def gogo_search(api_key: str, query: str):
    """Search animes on gogoanime

    - query: Search query

    Price: 1 credits"""
    if not await DB.is_user(api_key):
        return {"success": False, "error": "Invalid api key"}

    try:
        await DB.reduce_credits(api_key, 1)
    except Exception as e:
        return {"success": False, "error": str(e)}

    data = await GoGoApi(get_session()).search(query)
    return {"success": True, "results": data}


@app.get("/gogo/anime", name="gogo anime", tags=["Gogo Anime"])
async def gogo_anime(api_key: str, id: str):
    """Get anime info from gogoanime

    - id : Anime id, Ex : horimiya-dub

    Price: 1 credits"""
    if not await DB.is_user(api_key):
        return {"success": False, "error": "Invalid api key"}

    try:
        await DB.reduce_credits(api_key, 1)
    except Exception as e:
        return {"success": False, "error": str(e)}

    data = await GoGoApi(get_session()).anime(id)
    return {"success": True, "results": data}


@app.get("/gogo/episode", name="gogo episode", tags=["Gogo Anime"])
async def gogo_episode(
    api_key: str, id: str, lang: Literal["sub", "dub", "both", "any"] = "sub"
):
    """Get episode embed links from gogoanime

    - id : Episode id, Ex : horimiya-dub-episode-3
    - lang : sub | dub | both | any

    Price: 1 credits for sub and dub, 2 credits for both"""
    if not await DB.is_user(api_key):
        return {"success": False, "error": "Invalid api key"}

    try:
        await DB.reduce_credits(api_key, 2 if lang == "both" else 1)
    except Exception as e:
        return {"success": False, "error": str(e)}

    data = await GoGoApi(get_session()).episode(id, lang)
    return {"success": True, "results": data}


@app.get("/gogo/stream", name="gogo stream", tags=["Gogo Anime"])
async def gogo_stream(api_key: str, url: str):
    """Get episode stream links (m3u8) from gogoanime

    - url : Episode url, Ex : https://anihdplay.com/streaming.php?id=MTUyODYy&title=Horimiya+%28Dub%29+Episode+3

    Price: 1 credits"""
    if not await DB.is_user(api_key):
        return {"success": False, "error": "Invalid api key"}

    try:
        await DB.reduce_credits(api_key, 1)
    except Exception as e:
        return {"success": False, "error": str(e)}

    data = await get_m3u8(get_session(), url)
    return {"success": True, "results": data}



@app.get("/animeworldin/stream", name="animeworldin stream", tags=["AnimeWorldIN"])
async def animeworldin_stream(api_key: str, url: str):
    """Get episode stream links (m3u8) from anime-world.in

    - url : Episode url, Ex : https://awstream.net/watch?v=91Vzzmx2Ez

    Price: 1 credits"""
    if not await DB.is_user(api_key):
        return {"success": False, "error": "Invalid api key"}

    try:
        await DB.reduce_credits(api_key, 1)
    except Exception as e:
        return {"success": False, "error": str(e)}

    data = await AnimeWorldIN(get_session()).stream(url)
    return {"success": True, "results": data}
