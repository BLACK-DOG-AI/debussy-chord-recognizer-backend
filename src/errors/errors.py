from http import HTTPStatus

class ApiError(Exception):
    code = HTTPStatus.UNPROCESSABLE_ENTITY
    description = "Default message"

class BadRequest(ApiError):
    code = HTTPStatus.BAD_REQUEST

class Unauthorized(ApiError):
    code = HTTPStatus.UNAUTHORIZED

class Forbidden(ApiError):
    code = HTTPStatus.FORBIDDEN

class NotFound(ApiError):
    code = HTTPStatus.NOT_FOUND

class PreconditionFailed(ApiError):
    code = HTTPStatus.PRECONDITION_FAILED
