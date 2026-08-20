from pathlib import Path
import json

from text_cleaning import clean_ocr_text


# ============================================================
# 1. FILES
# ============================================================

comparison_file = Path("comparison_report.json")
ground_truth_file = Path("ground_truth.json")

output_file = Path("final_ocr_evaluation.json")


# ============================================================
# 2. LOAD FILES
# ============================================================

with open(comparison_file, "r", encoding="utf-8") as file:
    comparison_results = json.load(file)

with open(ground_truth_file, "r", encoding="utf-8") as file:
    ground_truth = json.load(file)


# ============================================================
# 3. PREPROCESSING METHODS
# ============================================================

methods = [
    "original",
    "grayscale",
    "clahe",
    "threshold"
]

method_stats = {
    method: {
        "valid_samples": 0,
        "exact_matches": 0,
        "exact_match_rate": 0.0
    }
    for method in methods
}


# ============================================================
# 4. COMPARE OCR WITH GROUND TRUTH
# ============================================================

details = []


for image_result in comparison_results:

    image_name = image_result["image"]

    expected = ground_truth.get(
        image_name,
        ""
    )

    expected = clean_ocr_text(expected)

    # No ground truth means it cannot be evaluated
    if not expected:
        continue


    image_detail = {
        "image": image_name,
        "ground_truth": expected,
        "methods": {}
    }


    for method in methods:

        detections = image_result[
            "methods"
        ].get(method, [])


        predictions = []

        for detection in detections:

            text = clean_ocr_text(
                detection["text"]
            )

            confidence = float(
                detection["confidence"]
            )

            predictions.append({
                "text": text,
                "confidence": confidence
            })


        best_match = False
        best_prediction = ""


        # Check every OCR detection
        for prediction in predictions:

            if prediction["text"] == expected:

                best_match = True
                best_prediction = prediction["text"]
                break


        # If no exact match, keep highest confidence
        if not best_prediction and predictions:

            best_prediction = max(
                predictions,
                key=lambda x: x["confidence"]
            )["text"]


        method_stats[method][
            "valid_samples"
        ] += 1


        if best_match:

            method_stats[method][
                "exact_matches"
            ] += 1


        image_detail["methods"][method] = {
            "prediction": best_prediction,
            "exact_match": best_match
        }


    details.append(image_detail)


# ============================================================
# 5. CALCULATE EXACT MATCH RATE
# ============================================================

for method in methods:

    valid_samples = method_stats[
        method
    ]["valid_samples"]

    exact_matches = method_stats[
        method
    ]["exact_matches"]


    if valid_samples > 0:

        method_stats[method][
            "exact_match_rate"
        ] = round(
            exact_matches /
            valid_samples *
            100,
            2
        )


# ============================================================
# 6. SAVE FINAL REPORT
# ============================================================

final_report = {
    "confidence_threshold": 0.50,
    "method_statistics": method_stats,
    "details": details
}


with open(
    output_file,
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        final_report,
        file,
        indent=4,
        ensure_ascii=False
    )


# ============================================================
# 7. PRINT SUMMARY
# ============================================================

print("\n========================================")
print("FINAL OCR EVALUATION")
print("========================================")

print(
    "Evaluated images:",
    len(details)
)

print("\nExact Match Rates:")

for method in methods:

    rate = method_stats[
        method
    ]["exact_match_rate"]

    matches = method_stats[
        method
    ]["exact_matches"]

    samples = method_stats[
        method
    ]["valid_samples"]

    print(
        f"{method:12} : "
        f"{matches}/{samples} "
        f"({rate}%)"
    )


print("\n========================================")
print("REPORT SAVED")
print("========================================")

print(
    "File:",
    output_file
)