from logs.models import Log
def getLogs():
    queryset = Log.objects.all().order_by('created')
    return (queryset)

def createLog(formLog):
    log = formLog.save()
    log.save()

def createLogObject(level, message, created):
    log = Log()
    log.level = level
    log.message = message
    log.created = created
    log.save()