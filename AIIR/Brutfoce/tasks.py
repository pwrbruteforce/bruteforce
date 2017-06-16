import subprocess
from time import sleep

from celery import shared_task, task, current_task
from numpy import random
from scipy.fftpack import fft

from models import Task


@shared_task
def handle_task(hash, dictionary, length, task_id):

    password = subprocess.Popen('python C:\\MPI\\brute.py %s %s %s' % (hash, str(dictionary), str(length)),
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    while True:
        line = password.stdout.readline()
        print line
        if line.startswith('progress'):
            process_percent = int(line.split()[-1])
            current_task.update_state(state='PROGRESS', meta={'process_percent': process_percent})
        else:
            break
    if password:
        task = Task.objects.get(pk=int(task_id))
        task.output_password = line
        task.save()
    return line


@task()
def fft_random(n):
    """
    Brainless number crunching just to have a substantial task:
    """
    for i in range(n):
        print i
        x = random.normal(0, 0.1, 2000)
        y = fft(x)
        sleep(0.1)
        if (i%30 == 0):
            process_percent = int(100 * float(i) / float(n))
            current_task.update_state(state='PROGRESS', meta={'process_percent': process_percent})
    return random.random()
