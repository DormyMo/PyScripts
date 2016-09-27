import multiprocessing
import time
import functools

def timeout(max_timeout):
    def timeout_decorator(item):
        @functools.wraps(item)
        def func_wrapper(*args, **kwargs):
            p = multiprocessing.Process(target=item, args=args, kwargs=kwargs)
            p.start()
            p.join(max_timeout)
            if p.is_alive():
                p.terminate()
                p.join()
                raise Exception("timeout")
        return func_wrapper
    return timeout_decorator

if __name__ == '__main__':
    
    @timeout(3)
    def func():
        print 'start'
        time.sleep(4)
        print 'end'

    func()
