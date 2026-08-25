import json
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(BASE_DIR))

from evaluate_capstone import normalize_text


RESULTS_DIR = BASE_DIR / "results"


def test_normalize_text():
    assert normalize_text("MH 20 DV 2366") == "MH20DV2366"
    assert normalize_text("abc-123 xyz") == "ABC123XYZ"


def test_results_file_exists():
    result_file = RESULTS_DIR / "capstone_results.json"
    assert result_file.exists()


def test_metrics_file_exists():
    metrics_file = RESULTS_DIR / "capstone_metrics.json"
    assert metrics_file.exists()


def test_results_structure():
    result_file = RESULTS_DIR / "capstone_results.json"

    with open(result_file, "r", encoding="utf-8") as file:
        results = json.load(file)

    assert isinstance(results, list)
    assert len(results) == 15


def test_metrics_structure():
    metrics_file = RESULTS_DIR / "capstone_metrics.json"

    with open(metrics_file, "r", encoding="utf-8") as file:
        metrics = json.load(file)

    assert "total_images" in metrics
    assert "evaluated_images" in metrics
    assert "exact_matches" in metrics
    assert "exact_match_rate_percent" in metrics
    assert "average_processing_time_seconds" in metrics
    assert "average_fps" in metrics


def test_total_images():
    metrics_file = RESULTS_DIR / "capstone_metrics.json"

    with open(metrics_file, "r", encoding="utf-8") as file:
        metrics = json.load(file)

    assert metrics["total_images"] == 15


def test_metric_ranges():
    metrics_file = RESULTS_DIR / "capstone_metrics.json"

    with open(metrics_file, "r", encoding="utf-8") as file:
        metrics = json.load(file)

    assert 0 <= metrics["exact_match_rate_percent"] <= 100
    assert metrics["average_processing_time_seconds"] >= 0
    assert metrics["average_fps"] >= 0