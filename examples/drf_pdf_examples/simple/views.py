# coding: utf-8
from cStringIO import StringIO

from rest_framework import status
from rest_framework.views import APIView

from drf_pdf.renderer import PDFRenderer
from drf_pdf.response import PDFResponse

from reportlab.pdfgen import canvas


class SimpleExample(APIView):

    renderer_classes = (PDFRenderer, )

    def get(self, request):
        pdf = StringIO()

        gen_pdf = canvas.Canvas(pdf)
        gen_pdf.drawString(100, 100, 'Simple example')
        gen_pdf.showPage()
        gen_pdf.save()

        return PDFResponse(
            pdf.getvalue(),
            file_name='example',
            status=status.HTTP_200_OK
        )
