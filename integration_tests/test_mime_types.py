import os
import pathlib
import pytest
import magic

from helpers.http_methods_helpers import get


@pytest.mark.benchmark
@pytest.mark.parametrize("function_type", ["sync", "async"])
def test_text_type(function_type: str, session):
    r = get(f"/{function_type}/file/download")
    assert r.headers["Content-Type"] == "text/plain"


@pytest.mark.benchmark
@pytest.mark.parametrize("function_type", ["sync", "async"])
def test_pdf_type(function_type: str, session):
    r = get(f"/{function_type}/file/download_pdf")
    assert r.headers["Content-Type"] == "application/pdf"


@pytest.mark.benchmark
@pytest.mark.parametrize("function_type", ["sync", "async"])
def test_image_type(function_type: str, session):
    r = get(f"/{function_type}/file/download_image")
    assert r.headers["Content-Type"] == "image/tiff"


@pytest.mark.benchmark
@pytest.mark.parametrize("function_type", ["sync", "async"])
def test_docx_type(function_type: str, session):
    r = get(f"/{function_type}/file/download_docx")
    assert (
        r.headers["Content-Type"]
        == "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )


@pytest.mark.benchmark
@pytest.mark.parametrize("function_type", ["sync", "async"])
def test_mislabeled_type(function_type: str, session):
    r = get(f"/{function_type}/file/download_mislabeled")
    assert r.headers["Content-Type"] == "image/tiff"


@pytest.mark.benchmark
@pytest.mark.parametrize("function_type", ["sync", "async"])
def test_unknown_type(function_type: str, session):
    r = get(f"/{function_type}/file/download_unknown")
    assert r.headers["Content-Type"] == magic.from_file(
        os.path.join(
            pathlib.Path(__file__).parent.resolve(), "downloads", "test_unknown.strings"
        ),
        mime=True,
    )
