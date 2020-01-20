import json
import multiprocessing

threads = 1
cores = multiprocessing.cpu_count()
workers = cores * 2
bind = 'unix:/tmp/gunicorn.sock'
errorlog = "-"
worker_class = 'egg:meinheld#gunicorn_worker'

log_data = {
    "bind": bind,
    "workers": workers,
    "threads": threads,
    "worker_class": worker_class
}
print(json.dumps(log_data))
