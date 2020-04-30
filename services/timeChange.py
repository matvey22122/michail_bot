import datetime

def changeInfo(service, doc_id):
    revisions = service.revisions().list(fileId=doc_id).execute()
    items = revisions['items']
    timeNow = datetime.datetime.now()

    timeLast = datetime.datetime.strptime("2020-03-24T20:53:36.620Z", "%Y-%m-%dT%H:%M:%S.%f%z")
    timeLast = timeLast.replace(tzinfo=None)
    items.reverse()
    for change in items:
        timeCh = datetime.datetime.strptime(change['modifiedDate'], "%Y-%m-%dT%H:%M:%S.%f%z")
        timeCh = timeCh.replace(tzinfo=None)
        if change['lastModifyingUserName'] == "Ashurova Alina" and  timeCh > timeLast:
            timeLast = timeCh
            break
    return (timeNow - (timeLast + datetime.timedelta(hours=5)))