#!/usr/bin/env python3
"""Verify the real landing-page destination, not only its HTTP 200 wrapper."""
import argparse
import hashlib
from html.parser import HTMLParser
from pathlib import Path
import sys
from urllib.parse import urljoin
from urllib.request import urlopen

CATALOG = "catalog_retail_2024_02.pdf"


class Landing(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refresh = []
        self.links = []

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if tag == "meta" and attrs.get("http-equiv", "").lower() == "refresh":
            target = attrs.get("content", "").partition(";")[2].partition("=")[2]
            self.refresh.append(target.strip().strip("\"'"))
        if tag == "a":
            self.links.append(attrs.get("href"))


def landing(document):
    page = Landing()
    page.feed(document.decode("utf-8"))
    if page.refresh != [CATALOG] or CATALOG not in page.links:
        raise ValueError("The automatic redirect and fallback link must point to the tracked catalogue")


def fetch(url, mime):
    with urlopen(url, timeout=20) as response:
        if response.status != 200 or response.headers.get_content_type() != mime:
            raise ValueError("Unexpected status or content type: " + url)
        return response.read()


def check(root, url=None):
    landing((root / "index.html").read_bytes())
    expected = (root / CATALOG).read_bytes()
    if not expected.startswith(b"%PDF-") or b"%%EOF" not in expected[-1024:]:
        raise ValueError("The release catalogue is missing or is not a complete PDF")
    digest = hashlib.sha256(expected).hexdigest()
    if url:
        landing(fetch(url, "text/html"))
        actual = fetch(urljoin(url, CATALOG), "application/pdf")
        if hashlib.sha256(actual).hexdigest() != digest:
            raise ValueError("Published catalogue differs from the release")
    print(f"Catalogue verified: {len(expected)} bytes, SHA-256 {digest}" + (f", {url}" if url else ""))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--url", help="Verify the actual public hostname and complete PDF response")
    args = parser.parse_args()
    try:
        check(args.root, args.url)
    except (OSError, ValueError) as error:
        print("Catalogue verification failed: " + str(error), file=sys.stderr)
        sys.exit(1)
