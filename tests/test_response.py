# -*- coding: utf-8 -*-
from drf_pdf import response


class TestResponse(object):
    """Test for DRF-PDF Response"""

    def test_response(self, pdf_file_sample):

        with open(pdf_file_sample, 'r') as f:
            file_data = f.read()
            ret = response.PDFResponse(
                file_data,
                'sample'
            )

        assert ret.content_type.lower() == 'application/pdf'
        assert ret['Content-Length'] == str(len(file_data))
        assert ret['Content-Disposition'].lower() == 'filename="sample.pdf"'
