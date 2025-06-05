# Smart Home API

这是一个基于 FastAPI 构建的智能家居系统后端项目，支持用户管理、设备管理、使用记录、安全事件及用户反馈等功能。

## 📦 技术栈

- Python 3.12+
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic

## 🔧 功能模块

- 用户注册与登录
- 房屋与设备绑定
- 设备使用记录追踪
- 安全事件记录与处理
- 用户反馈收集与分析
- 数据可视化分析接口

## 📂 项目结构

smarthomeapi/
├── app/
│ ├── models/ # 数据模型
│ ├── schemas/ # Pydantic 数据验证模型
│ ├── routers/ # 路由文件
│ └── main.py # FastAPI 启动入口
├── requirements.txt # Python依赖文件
└── README.md


## 启动项目

```bash
# 安装依赖
pip install -r requirements.txt

# 运行 FastAPI 应用
uvicorn app.main:app --reload
