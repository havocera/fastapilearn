import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware

import models
from database import SessionLocal, engine
from log import logger
from schemas import CreatTask

app = FastAPI()

# models.Base.metadata.create_all(bind=engine)
app.add_middleware(
    CORSMiddleware,
    # 允许跨域的源列表， 例如 ["http://www.example.org"] 等等，["*"] 表示允许任何源
    allow_origins=["*"],
    # 跨域请求是否支持 cookie，默认是 False，如果为 True，allow_origins 必须为具体的源，不可以是 ["*"]
    allow_credentials=True,
    # 允许跨域请求的 HTTP 方法列表，默认是 ["GET"]
    allow_methods=["*"],
    # 允许跨域请求的 HTTP 请求头列表，默认是 []，可以使用 ["*"] 表示允许所有的请求头
    # 当然 Accept、Accept-Language、Content-Language 以及 Content-Type 总之被允许的
    allow_headers=["*"],
    # 可以被浏览器访问的响应头, 默认是 []，一般很少指定
    expose_headers=["*"],
    # 设定浏览器缓存 CORS 响应的最长时间，单位是秒。默认为 600，一般也很少指定
    max_age=1000
)
def get_db():
    """
    每一个请求处理完毕后会关闭当前连接，不同的请求使用不同的连接
    :return:
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    logger.info("success")
    return {"message": "Hello World"}


@app.get("/hello/")
async def say_hello(task: CreatTask, db: Session = Depends(get_db)):
    data = db.query(models.Task).filter().all()
    return {"message": f"Hello {task.name}"}


if __name__ == '__main__':
    uvicorn.run(app=app, host="0.0.0.0", port=2372)
