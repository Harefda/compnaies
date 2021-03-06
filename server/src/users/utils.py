import enum


class UserErrorMessages(enum.Enum):
    TOO_LONG_EMAIL_ERROR = "TOO_LONG_EMAIL_ERROR"
    NON_UNIQUE_EMAIL_ERROR = "NON_UNIQUE_EMAIL_ERROR"
    INCORRECT_PASSWORD_SCHEME_ERROR = "INCORRECT_PASSWORD_SCHEME_ERROR"

    DISABLED_USER_ERROR = "DISABLED_USER_ERROR"
    CREDENTIALS_ERROR = "CREDENTIALS_ERROR"
    REQUEST_FIELDS_ERROR = "REQUEST_FIELDS_ERROR"

    USER_IS_NOT_AUTHENTICATED_ERROR = "USER_IS_NOT_AUTHENTICATED_ERROR"

    WRONG_USER_ID_ERROR = "WRONG_USER_ID_ERROR"
    USER_DOES_NOT_EXIST_ERROR = "USER_DOES_NOT_EXIST_ERROR"