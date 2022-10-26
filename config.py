import random

ip = 'ip_goes_here'

def rand_port():
    port = int(random.randrange(10000,10099))
    return port
