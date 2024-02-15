from typing import Literal
from fastapi import FastAPI
from utils.extractor.gogo_extractor import get_m3u8
from utils.gogo import GoGoApi
from utils.db import DB
from fastapi.responses import HTMLResponse
from fastapi.openapi.utils import get_openapi
import aiohttp
from theme import custom_ui_html, custom_ui_css

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
        title="FᴀsᴛAɴɪᴍᴇAᴘɪ",
        version="1.0",
        description="Usᴇ Pᴏᴡᴇʀꜰᴜʟʟ Aᴘɪ Fᴇᴀᴛᴜʀᴇs Pʀᴏᴠɪᴅᴇᴅ Bʏ Lᴏᴜɴɢᴇ Bᴏᴛs",
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


@app.get("/", name="home", tags=["Home"], response_class=HTMLResponse)
async def home():
    return custom_ui_html


# Gogoanime


@app.get("/latest", name="Latest Anime Scrapper")
async def gogo_latest(api_key: str, page: int = 1):
    """Get Latest Released Animes From

    - page: Page Number (Default: 1)

    Price: 1 BP"""
    if not await DB.is_user(api_key):
        return {"success": False, "error": "Invalid api key"}

    try:
        await DB.reduce_credits(api_key, 1)
    except Exception as e:
        pass

    data = await GoGoApi(get_session()).latest(page)
    return {"success": True, "results": data}


@app.get("/search", name="Search Anime")
async def gogo_search(api_key: str, query: str):
    """Search Animes

    - query: Search Query

    Price: 1 credits"""
    if not await DB.is_user(api_key):
        return {"success": False, "error": "Invalid api key"}

    try:
        await DB.reduce_credits(api_key, 1)
    except Exception as e:
        return {"success": False, "error": str(e)}

    data = await GoGoApi(get_session()).search(query)
    return {"success": True, "results": data}


@app.get("/anime", name="Anime Information")
async def gogo_anime(api_key: str, id: str):
    """Get Anime Information 

    - id : Anime Id, Example : naruto-dub

    Price: 1 credits"""
    if not await DB.is_user(api_key):
        return {"success": False, "error": "Invalid api key"}

    try:
        await DB.reduce_credits(api_key, 1)
    except Exception as e:
        return {"success": False, "error": str(e)}

    data = await GoGoApi(get_session()).anime(id)
    return {"success": True, "results": data}


@app.get("/episode", name="Episode Information")
async def gogo_episode(
    api_key: str, id: str, lang: Literal["sub", "dub", "both", "any"] = "sub"
):
    """Get Episode Information 

    - id : Episode id, Ex : naruto-dub-episode-3
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


@app.get("/stream", name="Episode Stream")
async def gogo_stream(api_key: str, url: str):
    """Get Episode Stream Links (m3u8 for Download Faster)

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
