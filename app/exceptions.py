from fastapi import HTTPException, status


class StandardException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class IncorrectCityNameException(StandardException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "Check the city name"
