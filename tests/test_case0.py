import pyHTMLProofer


def test_no_options_links():
    """Tests the check links function."""

    links = ["https://example.com", "https://cloudbytes.dev"]

    failures = pyHTMLProofer.links(links).check()

    assert len(failures) == 0


def test_no_options_file():
    files = "tests/cases/1/file1.html"
    failures = pyHTMLProofer.file(files).check()
    assert len(failures) == 0


def test_no_options_directory():
    """Tests the check links function."""
    directory_paths = ["tests/cases/1/"]
    failures = pyHTMLProofer.directories(directory_paths).check()

    assert len(failures) == 0
