import gearman
import pymongo

c = pymongo.Connection()
db = c["ganapatih"]

gm_worker = gearman.GearmanWorker(["127.0.0.1"])

import json

#db.panics.insert({'nama': 'sopier'})

def insert_dbase(gearman_worker, gearman_job):
    print 'inserting dbase'
    c = pymongo.Connection()
    db = c["ganapatih"]

    print json.loads(json.dumps(gearman_job.data))
    db.panics.insert(json.loads(gearman_job.data))
    return json.dumps(gearman_job.data)
    #return db.panics.insert(gearman_job.data)

gm_worker.set_client_id('insert_dbase_worker')
gm_worker.register_task('register', insert_dbase)
gm_worker.work()
