# -*- coding: utf-8 -*-
from drf_pdf import response
import codecs


class TestResponse(object):
    """Test for DRF-PDF Response"""

    def test_response(self, pdf_file_sample):

        with codecs.open(pdf_file_sample, 'r', 'ISO-8859-2') as f:
            file_data = f.read()
            ret = response.PDFResponse(
                file_data,
                'sample'
            )

        assert ret.content_type.lower() == 'application/pdf'
        assert ret['Content-Length'] == str(len(file_data))
        assert ret['Content-Disposition'].lower() == 'filename="sample.pdf"'
