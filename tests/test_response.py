# -*- coding: utf-8 -*-
import codecs
import os
import pytest
from drf_pdf import response, exceptions


class TestResponse(object):
    """Test for DRF-PDF Response"""

    def test_response(self, pdf_file_sample):
        with codecs.open(pdf_file_sample, 'rb', 'ISO-8859-2') as f:
            file_data = f.read()
            ret = response.PDFResponse(
                file_data,
                'sample'
            )

        assert ret.content_type.lower() == 'application/pdf'
        assert ret['Content-Length'] == str(len(file_data))
        assert ret['Content-Disposition'].lower() == 'filename="sample.pdf"'


class TestFileResponse(object):
    """Test for DRF-PDF File Response"""

    def test_response_by_file_name(self, pdf_file_sample):
        ret = response.PDFFileResponse(file_path=pdf_file_sample)

        assert ret.content_type.lower() == 'application/pdf'
        assert ret['Content-Disposition'].lower() == \
            'filename="{}"'.format(os.path.basename(pdf_file_sample))

    def test_response_file_not_found(self, pdf_file_sample):
        with pytest.raises(exceptions.PDFFileNotFound):
            response.PDFFileResponse(file_path='foo.bar')
