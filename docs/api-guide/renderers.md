Renderers
=========

In order to support a new `media_type` in _REST Framework_, it is needed to add a [renderer](http://www.django-rest-framework.org/api-guide/renderers/) to `renderer_classes`. So DRF PDF includes `PDFRenderer`.

API Reference
-------------

### PDFRenderer

Render PDF binary content.

**.media_type**: `application/pdf`

**.format**: `pdf`

**.render_style**: `bynary`
