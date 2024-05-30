from logs.models import Log

def getLogs():
    return Log.objects.all().order_by('created')

def createLogObject(uid, level, message, user, time):
    log = Log()
    log.uid = uid
    log.level = level
    log.message = message
    log.user = user
    log.time = time
    log.save()

def getLogsByDocumento(document):
    try:
        logs = Log.objects.filter(user=document)
        return logs
    except Exception as e:
        return None