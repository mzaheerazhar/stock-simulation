import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stock_market_simulation.settings')

app = Celery('stock_market_simulation')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
