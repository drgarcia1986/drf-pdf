# encoding: utf-8
from rest_framework.response import Response


class PDFResponse(Response):
    """
    DRF Response to render data as a PDF File

    kwargs:
        - pdf (byte array). The PDF file content.
        - file_name (string). The default downloaded file name.
    """

    def __init__(self, pdf, file_name, *args, **kwargs):
        headers = headers = {
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
