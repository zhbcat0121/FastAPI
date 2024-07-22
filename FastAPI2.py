from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
import uvicorn
from fastapi import Request
from api.book import api_book
from api.cbs import api_cbs
from api.zz import api_zz
import logging


# 配置日志记录
logging.basicConfig(level=logging.INFO)


# 创建一个 FastAPI 应用程序实例
app = FastAPI()

app.include_router(api_book, prefix="/book", tags=["图书接口"])
app.include_router(api_cbs, prefix="/cbs", tags=["出版社接口"])
app.include_router(api_zz, prefix="/zz", tags=["作者接口"])

app.mount("/upimg", StaticFiles(directory="upimg"), name="umimg")

# 定义一个处理 GET 请求的路由装饰器，当访问根路径 ('/') 时触发此函数
@app.get("/")
# 定义异步处理函数，返回一个 JSON 响应，内容为 {"message": "Hello B站程序员科科"}
async def root():
    return {"message": "Hello ZHB"}

# 定义一个处理 GET 请求的路由装饰器，当访问路径 '/get' 时触发此函数
@app.get("/get")
# 定义处理函数，返回一个 JSON 响应，内容为 {"method": "get方法"}
def get_test():
    return {"method": "get方法"}

# 定义一个处理 POST 请求的路由装饰器，当访问路径 '/post' 时触发此函数
@app.post("/post")
# 定义处理函数，返回一个 JSON 响应，内容为 {"method": "post方法"}
def post_test():
    return {"method": "post方法"}

# 定义一个处理 PUT 请求的路由装饰器，当访问路径 '/put' 时触发此函数
@app.put("/put")
# 定义处理函数，返回一个 JSON 响应，内容为 {"method": "put方法"}
def put_test():
    return {"method": "put方法"}

# 定义一个处理 DELETE 请求的路由装饰器，当访问路径 '/delete' 时触发此函数
@app.delete("/delete")
# 定义处理函数，返回一个 JSON 响应，内容为 {"method": "delete方法"}
def delete_test():
    return {"method": "delete方法"}

@app.get('/get_test')
async def get_test(request: Request):
    get_test = request.query_params
    logging.info("Received GET request with the following query parameters:")
    for key, value in get_test.items():
        logging.info(f"{key}: {value}")
    print(get_test)
    return {"message": "get_test111"}

@app.post('/post_test')
async def post_test(request: Request):
    post_test = await request.json()

    print(post_test)
    return {"message": "post_test"}

# 检查是否直接运行此脚本（而不是作为模块导入）
if __name__ == '__main__':
    # 使用 uvicorn 运行 FastAPI 应用程序
    # "FastAPI2:app" 指定应用程序的路径（模块名称:应用实例名称）
    # host="127.0.0.1" 设置服务器监听的 IP 地址
    # port=8080 设置服务器监听的端口
    # reload=True 使服务器在代码更改时自动重新加载（适用于开发环境）
    uvicorn.run("FastAPI2:app", host="127.0.0.1", port=8080, reload=True)
