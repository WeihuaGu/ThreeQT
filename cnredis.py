import redis   # 导入redis 模块
r = redis.Redis(host='localhost', port=6379, decode_responses=True) 
