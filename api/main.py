import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
from schema import *
from models import *
from methods import *

import os
from dotenv import load_dotenv

load_dotenv('.env')

app = FastAPI()
# to avoid csrftokenError
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])

@app.get("/")
async def root():
    return {"message": "Welcome to Facebook public page scraping with Python"}


@app.post('/fbscrap/', response_model=Fbdata)
async def fbscrap(scrap_info): #contient : pagename, pageurl, scrollnbr
    dates,posts_texts,reactions_nbr,shares_nbr,comments_nbr,comments,post_images,post_videos = scrap_fb(scrap_info.pagrurl,scrap_info.scrollnbr)
    for k in range(len(dates)):
        db_fb = Fbdata(page_name=scrap_info.pagename, date=dates[k], text = posts_texts[k],reactions_nbr=reactions_nbr[k],
                       shares_nbr=shares_nbr[k],comments_nbr=comments_nbr[k],comments=comments[k],images_url=post_images[k],videos_url=post_videos[k])
        db.session.add(db_fb)
        db.session.commit()
    return 1

@app.get('/fbscrap/')
async def fbscrap():
    posts = db.session.query(Fbdata).all()
    return posts

# To run locally
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)