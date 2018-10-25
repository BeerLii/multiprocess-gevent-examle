# -*- coding: utf-8 -*-
from multiprocessing import Pool as MPool
import time


def time_request(n):
    from gevent import monkey;monkey.patch_time()
    print('4444')
    time.sleep(5)
    return n


def gevent_req(num_req):
    from gevent.pool import Pool
    import gevent
    pool = Pool(num_req / 2)
    glets = []
    for x in range(0, num_req):
        with gevent.Timeout(10, False):
            g = pool.spawn(time_request,x)
            glets.append(g)
        print(glets)
    pool.join()
    return [ g.value for g in glets ]



if __name__ == "__main__":

    num_reqs = 10
    num_procs = 2
    num_greqs = int(num_reqs / num_procs)
    results = []
    pool = MPool(processes=num_procs)
    print(pool)
    for i in range(0, num_procs):
        result = pool.apply_async(gevent_req, (num_greqs,))
        results.append(result)
    pool.close()
    pool.join()
    for result in results:
        print(result.get())



