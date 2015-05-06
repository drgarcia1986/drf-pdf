# encoding: utf-8
from rest_framework import status
from rest_framework.exceptions import APIException


class PDFFileNotFound(APIException):
    status_code = status.HTTP_404_NOT_FOUND
