SCOPES = [
    'https://www.googleapis.com/auth/documents',
    'https://www.googleapis.com/auth/drive'
]
DOCUMENT_ID_1 = '1krXSZdL_c6tnCDMLYJ2C6xngsDoHuJ9WGXTe5STwggE'
DOCUMENT_ID_2 = '1rzfkk4Va7_jEWuFGt05WKdbmqB5K7m-3U64wE3NOI3c'
CRED_FILE = "creds.json"


def writeDoc(text, typ, service):
    if typ == 1:
        document = service.documents().get(documentId=DOCUMENT_ID_1).execute()
        content = document['body']['content'][2]
        try:
            if content['paragraph']['paragraphStyle']['indentFirstLine']['magnitude'] == 54 and content['paragraph']['paragraphStyle']['indentStart']['magnitude'] == 72:
                requests = [
                    {
                        "insertText": {
                            "text": text[6:] + "\n",
                            "location": {
                                "index": 12
                            }
                        }
                    }
                ]
                result = service.documents().batchUpdate(documentId=DOCUMENT_ID_1, body={'requests': requests}).execute()
            else:
                requests = [
                    {
                        'insertText': {
                            'location': {
                                'index': 12
                            },
                            'text': '\t' + text[6:] + '\n',
                        }
                    }
                ]
                result = service.documents().batchUpdate(documentId=DOCUMENT_ID_1, body={'requests': requests}).execute()
                requests = [
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
                                'endIndex':  14
                            },
                            'bulletPreset': 'NUMBERED_DECIMAL_ALPHA_ROMAN',
                        }
                    }
                ]
                result = service.documents().batchUpdate(documentId=DOCUMENT_ID_1, body={'requests': requests}).execute()
        except :
            requests = [
                {
                    'insertText': {
                        'location': {
                            'index': 12
                        },
                        'text': '\t' + text[6:] + '\n',
                    }
                }
            ]
            result = service.documents().batchUpdate(documentId=DOCUMENT_ID_1, body={'requests': requests}).execute()
            requests = [
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
                            'endIndex':  14
                        },
                        'bulletPreset': 'NUMBERED_DECIMAL_ALPHA_ROMAN',
                    }
                }
            ]
            result = service.documents().batchUpdate(documentId=DOCUMENT_ID_1, body={'requests': requests}).execute()
    elif typ == 2:
        document = service.documents().get(documentId=DOCUMENT_ID_2).execute()
        content = document['body']['content'][2]
        try:
            if content['paragraph']['paragraphStyle']['indentFirstLine']['magnitude'] == 54 and content['paragraph']['paragraphStyle']['indentStart']['magnitude'] == 72:
                requests = [
                    {
                        "insertText": {
                            "text": text + "\n",
                            "location": {
                                "index": 12
                            }
                        }
                    }
                ]
                result = service.documents().batchUpdate(documentId=DOCUMENT_ID_2, body={'requests': requests}).execute()
            else:
                requests = [
                    {
                        'insertText': {
                            'location': {
                                'index': 12
                            },
                            'text': '\t' + text + '\n',
                        }
                    }
                ]
                result = service.documents().batchUpdate(documentId=DOCUMENT_ID_2, body={'requests': requests}).execute()
                requests = [
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
                                'endIndex':  14
                            },
                            'bulletPreset': 'NUMBERED_DECIMAL_ALPHA_ROMAN',
                        }
                    }
                ]
                result = service.documents().batchUpdate(documentId=DOCUMENT_ID_2, body={'requests': requests}).execute()
        except:
            requests = [
                {
                    'insertText': {
                        'location': {
                            'index': 12
                        },
                        'text': '\t' + text + '\n',
                    }
                }
            ]
            result = service.documents().batchUpdate(documentId=DOCUMENT_ID_2, body={'requests': requests}).execute()
            requests = [
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
                            'endIndex':  14
                        },
                        'bulletPreset': 'NUMBERED_DECIMAL_ALPHA_ROMAN',
                    }
                }
            ]
            result = service.documents().batchUpdate(documentId=DOCUMENT_ID_2, body={'requests': requests}).execute()
    