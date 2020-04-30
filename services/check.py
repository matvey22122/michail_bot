def check(service, DOCUMENT_ID_1, text):
    if text[:5] == "Алин,":
        text = text[:5]
    document = service.documents().get(documentId=DOCUMENT_ID_1).execute()
    content = document['body']['content'][1]
    if content.get('paragraph'):
        if content['paragraph']['elements'][0]['textRun']['content'] != 'Разобрать:\n':
            requests = [
                {
                    'insertText': {
                        'location': {
                            'index': 1
                        },
                        'text': 'Разобрать:\n',
                    }
                }
            ]
            result = service.documents().batchUpdate(
                documentId=DOCUMENT_ID_1, body={'requests': requests}).execute()
            requests = [
                {
                    'insertText': {
                        'location': {
                            'index': 12
                        },
                        'text': '\t' + text + '\n',
                    }
                },
                {
                    'deleteParagraphBullets': {
                        'range': {
                            'startIndex': 1,
                            'endIndex':  14
                        },
                    }
                },
                {
                    'createParagraphBullets': {
                        'range': {
                            'startIndex': 1,
                            'endIndex':  13
                        },
                        'bulletPreset': 'NUMBERED_DECIMAL_ALPHA_ROMAN',
                    }
                }
            ]
            result = service.documents().batchUpdate(documentId=DOCUMENT_ID_1, body={'requests': requests}).execute()
            return False
        else:
             return True
    else:
        requests = [
            {
                'insertText': {
                    'location': {
                        'index': 1
                    },
                    'text': 'Разобрать:\n',
                }
            }
        ]
        result = service.documents().batchUpdate(
            documentId=DOCUMENT_ID_1, body={'requests': requests}).execute()
        requests = [
            {
                'insertText': {
                    'location': {
                        'index': 12
                    },
                    'text': '\t' + text + '\n',
                }
            },
            {
                'deleteParagraphBullets': {
                    'range': {
                        'startIndex': 1,
                        'endIndex':  14
                    },
                }
            },
            {
                'createParagraphBullets': {
                    'range': {
                        'startIndex': 1,
                        'endIndex':  13
                    },
                    'bulletPreset': 'BULLET_ARROW_DIAMOND_DISC',
                }
            }
        ]
        result = service.documents().batchUpdate(documentId=DOCUMENT_ID_1, body={'requests': requests}).execute()
        return False