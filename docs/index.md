Welcome to DRF PDF
==================

DRF PDF is a set of simple PDF utils for [Django Rest Framework](http://www.django-rest-framework.org/)


Requirements
------------

* Python (2.7, 3.4)
* Django (1.5, 1.6, 1.7, 1.8)


Installation
------------

Install using `pip`

```
pip install drf-pdf
```

Add `drf_pdf` to your `INSTALLED_APPS` setting.

```python
INSTALLED_APPS = (
    ...
    'drf_pdf',
)
```

Example
-------

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

With two or more `renderer_classes`

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
            file_name=pdf_id,
            status=status.HTTP_200_OK
        )
```

API Guide
---------

* [Renderers](api-guide/renderers.md)
* [Response](api-guide/responses.md)
