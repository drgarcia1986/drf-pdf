# DRF-PDF
[![Build Status](https://travis-ci.org/drgarcia1986/drf-pdf.svg?branch=master)](https://travis-ci.org/drgarcia1986/drf-pdf)
[![Coverage Status](https://coveralls.io/repos/drgarcia1986/drf-pdf/badge.svg)](https://coveralls.io/r/drgarcia1986/drf-pdf)

A simple PDF utils for Django Rest Framework

## Example

```python
# coding: utf - 8
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_pdf.renderer import PDFRenderer

from my_pdf_package import PDFGenerator


class PDFHandler(APIView):

    renderer_classes = (PDFRenderer, )

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

### With two or more renderer_classes


```python
# coding: utf - 8
from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView

from drf_pdf.response import PDFResponse
from drf_pdf.renderer import PDFRenderer

from my_pdf_package import get_pdf


class PDFHandler(APIView):

    renderer_classes = (PDFRenderer, JSONRenderer)

    def get(self, request, pdf_id):
        pdf = get_pdf(pdf_id)
		if not pdf:
			return Response(
				{'error': 'Not found'},
				status=status.HTTP_404_NOT_FOUND
			)

        return PDFResponse(
            pdf=pdf,
			file_name=pdf_id
            status=status.HTTP_200_OK
        )
```
