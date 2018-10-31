from rest_framework.exceptions import APIException


class DealAlreadyPicked(APIException):
    status_code = 409
    default_detail = "The deal is already picked by another rider"
    default_code = "deal_picked"


class DealNotYours(APIException):
    status_code = 403
    default_detail = "The deal is owned by another rider"
    default_code = "deal_owned_another"
