Responses
=========

You can use a [Regular REST Framework's Response](http://www.django-rest-framework.org/api-guide/responses/) to create a PDF file response, but _DRF PDF_ includes `PDFResponse` as a nice way to do it and it also includes some PDF file metadata.

Example:
```python
from rest_framework import status
from drf_pdf.response import PDFResponse

response = PDFResponse(
    pdf=pdf,
    file_name=pdf_id,
    status=status.HTTP_200_OK
)
```

Arguments:

* `pdf`: A byte array with the PDF file content.

* `file_name`: The default downloaded file name

Another option is _DRF PDF_ `PDFFileResponse`.
Different from `PDFResponse`, `PDFFileResponse` accepts the path of a pdf file and loads the pdf content from file system.

Example:
```python
from rest_framework import status
from drf_pdf.response import PDFFileResponse

response = PDFFileResponse(
	file_path='/path/to/file.pdf',
	status=status.HTTP_200_OK
)
```

Arguments:

* `file_path`: The PDF file path (to load file from file system).

You can also include _REST Framework's_ [Response arguments](http://www.django-rest-framework.org/api-guide/responses/#response) on both responses.
