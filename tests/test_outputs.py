import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")

# Expected values, computed by hand from environment/access.log: 6 request
# lines, 3 distinct client IPs (192.168.0.1, 192.168.0.2, 10.0.0.5), and
# /index.html requested 3 times vs. 2 for /about.html and 1 for /api/login.
EXPECTED_TOTAL_REQUESTS = 6
EXPECTED_UNIQUE_IPS = 3
EXPECTED_TOP_PATH = "/index.html"


def _load_report():
    assert REPORT_PATH.exists(), "criterion 1: /app/report.json was not produced"
    with open(REPORT_PATH) as f:
        return json.load(f)


def test_report_is_valid_json_object():
    """Criterion 1: /app/report.json exists and contains a valid JSON object."""
    report = _load_report()
    assert isinstance(report, dict)


def test_total_requests():
    """Criterion 2: total_requests matches the actual number of request lines."""
    report = _load_report()
    assert report.get("total_requests") == EXPECTED_TOTAL_REQUESTS


def test_unique_ips():
    """Criterion 3: unique_ips matches the actual number of distinct client IPs."""
    report = _load_report()
    assert report.get("unique_ips") == EXPECTED_UNIQUE_IPS


def test_top_path():
    """Criterion 4: top_path matches the actual most-requested path."""
    report = _load_report()
    assert report.get("top_path") == EXPECTED_TOP_PATH
