# DRF-PDF-Renderer
A simple PDF renderer for Django Rest Framework

## Example

```python
# coding: utf - 8
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_pdf_renderer import CustomPDFRenderer
from my_pdf_package import PDFGenerator


class PDFHandler(APIView):

    renderer_classes = (CustomPDFRenderer, )

    def get(self, request):
        pdf = PDFGenerator('foo')
        headers = {
            'Content-Disposition': 'filename="foo.pdf"',
            'Content-Length': len(pdf),
        }

        return Response(
            pdf,
            headers=headers,
            status=status.HTTP_200_OK
        )
```
