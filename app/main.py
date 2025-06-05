# app/main.py

from fastapi import FastAPI
from app.database import engine, Base
from app.routers import user, house, device, usage_record, security_event, user_feedback

# 创建表
Base.metadata.create_all(bind=engine)

app = FastAPI(title="智能家居系统 API")

# 注册路由
app.include_router(user.router)
app.include_router(house.router)
app.include_router(device.router)
app.include_router(usage_record.router)
app.include_router(security_event.router)
app.include_router(user_feedback.router)

@app.get("/")
def read_root():
    return {"message": "欢迎使用智能家居系统 API"}
