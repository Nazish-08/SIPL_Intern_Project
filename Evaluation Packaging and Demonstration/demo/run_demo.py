from pathlib import Path
import json


BASE_DIR = Path(__file__).resolve().parent.parent
RESULTS_DIR = BASE_DIR / "results"


def load_json(filename):
    file_path = RESULTS_DIR / filename

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:
        return json.load(file)


def main():

    metrics = load_json(
        "capstone_metrics.json"
    )

    results = load_json(
        "capstone_results.json"
    )

    print("\n========================================")
    print("ANPR CAPSTONE DEMONSTRATION")
    print("========================================")

    print(
        "\nTotal Images       :",
        metrics["total_images"]
    )

    print(
        "Evaluated Images   :",
        metrics["evaluated_images"]
    )

    print(
        "Exact Matches      :",
        metrics["exact_matches"]
    )

    print(
        "Exact Match Rate   :",
        f'{metrics["exact_match_rate_percent"]}%'
    )

    print(
        "Average Time       :",
        f'{metrics["average_processing_time_seconds"]} seconds'
    )

    print(
        "Average FPS        :",
        metrics["average_fps"]
    )

    print("\n----------------------------------------")
    print("IMAGE RESULTS")
    print("----------------------------------------")

    for result in results:

        print(
            f'\nImage: {result["image"]}'
        )

        print(
            f'Ground Truth: {result["ground_truth"]}'
        )

        print(
            f'Prediction: {result["prediction"]}'
        )

        print(
            f'OCR Confidence: {result["ocr_confidence"]}'
        )

        print(
            f'Detections: {result["detections"]}'
        )

        print(
            f'Exact Match: {result["exact_match"]}'
        )

    print("\n========================================")
    print("DEMO COMPLETE")
    print("========================================")


if __name__ == "__main__":
    main()