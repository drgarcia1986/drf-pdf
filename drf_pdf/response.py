# encoding: utf-8
import codecs
import os
from rest_framework.response import Response
from .exceptions import PDFFileNotFound


class PDFResponse(Response):

    """
    DRF Response to render data as a PDF File.

    kwargs:
        - pdf (byte array). The PDF file content.
        - file_name (string). The default downloaded file name.
    """

    def __init__(self, pdf, file_name, *args, **kwargs):
        headers = {
            'Content-Disposition': 'filename="{}.pdf"'.format(file_name),
            'Content-Length': len(pdf),
        }

        super(PDFResponse, self).__init__(
            pdf,
            content_type='application/pdf',
            headers=headers,
            *args,
            **kwargs
        )


class PDFFileResponse(PDFResponse):

    """
    DRF Response to render data as a PDF File
    from a PDF file from file system

    kwargs:
        - file_path (string). The PDF file path (to load file from file system)
    """

    def __init__(self, file_path, *args, **kwargs):
        pdf = self.__load_pdf(file_path)
        file_name = os.path.splitext(
            os.path.basename(file_path)
        )[0]
        super(PDFFileResponse, self).__init__(
            pdf=pdf,
            file_name=file_name,
            *args,
            **kwargs
        )

    def __load_pdf(self, file_path):
        if not os.path.isfile(file_path):
            raise PDFFileNotFound()
        with codecs.open(file_path, 'r', 'ISO-8859-2') as f:
            file_data = f.read()
        return file_data
