import requests
address = 'https://maker.ifttt.com/trigger/{event}/with/key/{key}'

def notify():
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
                requests.post(address, data = {"value1": f"{func.__name__} finished running"})
            except Exception as e:
                requests.post(address, data = {"value1":str(e)})
                raise
        return wrapper
    return decorator
