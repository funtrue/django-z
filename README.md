# django-z
简介：自定义django功能，优化添加django常用功能，用于快速搭建后台服务

# 1. 下载该项目
```shell
git clone https://github.com/funtrue/django-z.git
```

# 2. 运行该项目(启动方式)
## 1. 依赖安装
```shell
cd django-z

pip3 install -r requirements.txt
# pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

## 2. 单点启动服务
```shell
python3 manage.py runserver 0.0.0.0:7777
python3 manage.py qcluster  # 异步任务启动
```

## 3. gunicorn托管启动服务+nginx（nginx需要自行配置）
```shell
python3 manage.py collectstatic

gunicorn django_z.wsgi -c django_z/gunicorn_config.py
python3 manage.py qcluster  # 异步任务启动
```

# 3. 项目依赖与功能
## 1. 项目依赖
1. 项目依赖于mysql或sqlite3
2. redis支持哨兵模式，也可以单点配置
3. python3 >= 3.6.8; django==3.2.22
## 2. 项目功能
1. 美化admin界面
2. 配置admin导出导入功能，集成API开发文档
3. 使用django-q异步框架，支持定时，异步，监控功能
4. 自定义中间件与日志配置，供开发人员二次选择
5. 提供双因子认证功能，可插拔式使用
6. 使用Gunicorn与nginx对接，更加方便丝滑

# 4. 项目nginx文件配置
```nginx
server {
        listen       80;
        server_name  localhost;
        
        location / {
            client_max_body_size 50m;
            proxy_pass http://127.0.0.1:7777;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
        }
        location /static/ {
            root django-z静态文件的地址; # 此地需要修改
        }
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }
    }

```