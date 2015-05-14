# encoding: utf-8
from rest_framework import status
from rest_framework.views import APIView

from drf_pdf.renderer import PDFRenderer
from drf_pdf.response import PDFTemplateResponse


class FromTemplate(APIView):
    renderer_classes = (PDFRenderer, )

    def get(self, request):

        return PDFTemplateResponse(
            file_name='example',
            template_name='my_template.html',
            context={'text': 'foo'},
            status=status.HTTP_200_OK
        )
