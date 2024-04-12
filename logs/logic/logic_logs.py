from logs.models import Log
from clientes.models import Cliente
def getLogs():
    queryset = Log.objects.all().order_by('created')
    return (queryset)

def createLog(formLog):
    log = formLog.save()
    log.save()

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
        userSelect = None
        logs = None
        try:
            userSelect = Cliente.objects.get(document=document)
            if userSelect != None:
                 logs = Log.objects.filter(user=document)
        except:
            logs
        return logs