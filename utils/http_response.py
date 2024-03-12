class HttpResponse:
    OK = 200
    ERROR = 500
    NOTFOUND = 404
    BAD_REQUEST = 400
    NOT_AUTHORIZED = 401

    def __init__(cls, code, data={}, message='') -> None:
        cls.code = code 
        message = message
        data = data

    @classmethod
    def Success(cls, data={}, message=''):
        return {
            'code': cls.OK,
            'status': True,
            'message': message or 'OK',
            'data': data
        }
    
    @classmethod
    def NotFound(cls, data={}, message=''):
        return {
            'code': cls.NOTFOUND,
            'message': message or 'Not found in system',
            'data': data
        }
    
    @classmethod
    def BadRequest(cls, data={}, message=''):
        return {
            'code': cls.BAD_REQUEST,
            'message': message or 'Bad Request',
            'data': data
        }
        
    @classmethod
    def NotAuthorized(cls, data={}, message=''):
        return {
            'code': cls.NOT_AUTHORIZED,
            'message': message or 'Not Authorized',
            'data': data
        }