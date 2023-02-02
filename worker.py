import os
import time
from transcript import Transcribe

from celery import Celery
celery = Celery(__name__)
celery.conf.broker_url = os.environ.get(
    "CELERY_BROKER_URL", "redis://default:w5s6LGcV0CL4O1MbyuH2uecZnNWo72S4@redis-15989.c267.us-east-1-4.ec2.cloud.redislabs.com:15989")
celery.conf.result_backend = os.environ.get(
    "CELERY_RESULT_BACKEND", "redis://default:w5s6LGcV0CL4O1MbyuH2uecZnNWo72S4@redis-15989.c267.us-east-1-4.ec2.cloud.redislabs.com:15989")


@celery.task(name="create_task")
def create_task(url: str):
    Transcribe(url)
    # time.sleep(int(task_type) * 10)
    return True
