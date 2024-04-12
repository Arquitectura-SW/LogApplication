from logs.models import Log
def getLogs():
    return Log.objects.all().order_by('created')

def createLogObject(id, level, message, created, user, time):
    log = Log()
    log.id = id
    log.level = level
    log.message = message
    log.created = created
    log.user = user
    log.time = time
    log.save()

def getLogsByDocumento(document):
    try:
        logs = Log.objects.filter(user=document)
        return logs
    except Exception as e:
        return None