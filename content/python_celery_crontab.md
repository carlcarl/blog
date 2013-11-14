Title: Python celery crontab
Date: 2013-11-15 00:19
Author: carlcarl
Post_ID: 1379
Category: python
Tags: celery
Slug: python_celery_crontab


記錄一下 celery crontab 的用法，分成兩個部分：service 和 worker。service 負責定期塞 job 到 message queue 裡面，worker 則將 queue 裡的 job 拿出來執行，message queue 的部分這裡使用 `rabbitmq`。這邊為了方便，用了一個簡單的加法為例。

## Worker

### tasks.py

	:::python
	from celery import Celery
	from celery import task

	celery = Celery('tasks', backend='amqp', broker='amqp://guest@localhost//')

	@task
	def add(x, y):
    	print(x + y)
    	return x + y

### 執行

	:::bash
	# 叫三個 worker，每個 worker 有三個 process，然後取 tasks[.py] 內的 task
	celeryd-multi start 3 -c 3 -A tasks
	# 想叫一個 worker，有三個 process，然後是用 eventlet，並且取 tasks[.py] 內的 task
	celeryd-multi start 1 -P eventlet -c 3 -A tasks

### Daemon script

[/etc/init.d/celeryd][]  
[/etc/default/celeryd][]  




## Service

### celeryconfig.py

	:::python
	from datetime import timedelta

	CELERYBEAT_SCHEDULE = {
    	'add-every-30-seconds': {  # 可以自己決定怎麼取名字
        	'task': 'tasks.add',  # 塞 tasks[.py] 內的 add 到 job queue 裡
        	'schedule': timedelta(seconds=30),  # 每隔 30 秒
        	'args': (16, 16)  # 加法的兩個數字
    	},
	}

	CELERY_TIMEZONE = 'UTC'

### 執行

	:::bash
	celery beat 
	
### Daemon script

[/etc/init.d/celerybeat][]  
[/etc/default/celerybeat][]
	
	
	
[/etc/init.d/celeryd]: https://github.com/celery/celery/blob/3.1/extra/generic-init.d/celeryd
[/etc/default/celeryd]: http://docs.celeryproject.org/en/master/tutorials/daemonizing.html
[/etc/init.d/celerybeat]: https://github.com/celery/celery/blob/3.1/extra/generic-init.d/celerybeat
[/etc/default/celerybeat]: http://docs.celeryproject.org/en/master/tutorials/daemonizing.html
