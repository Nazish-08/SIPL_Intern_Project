import re


# ============================================================
# 1. CLEAN OCR TEXT
# ============================================================

def clean_ocr_text(text: str) -> str:
    """
    Normalize OCR text by:
    removing extra spaces,
    converting to uppercase,
    removing unwanted characters.
    """

    text = text.upper()

    # Replace multiple spaces with one
    text = re.sub(r"\s+", " ", text)

    # Remove spaces around text
    text = text.strip()

    # Keep only letters, numbers and spaces
    text = re.sub(
        r"[^A-Z0-9 ]",
        "",
        text
    )

    # Remove spaces completely for plate matching
    text = text.replace(" ", "")

    return text


# ============================================================
# 2. INDIAN LICENSE PLATE PATTERN
# ============================================================

INDIAN_PLATE_PATTERN = re.compile(
    r"^[A-Z]{2}[0-9]{1,2}[A-Z]{1,3}[0-9]{4}$"
)


# ============================================================
# 3. VALIDATE INDIAN PLATE
# ============================================================

def is_valid_indian_plate(text: str) -> bool:
    """
    Check whether OCR text follows
    a common Indian vehicle registration pattern.
    """

    cleaned_text = clean_ocr_text(text)

    return bool(
        INDIAN_PLATE_PATTERN.fullmatch(
            cleaned_text
        )
    )


# ============================================================
# 4. TEST EXAMPLES
# ============================================================

if __name__ == "__main__":

    test_values = [
        "MH12AB1234",
        "MH 12 AB 1234",
        "DL8CAF1234",
        "ABC123",
        "MOTE BEAM"
    ]

    print("========== TEXT CLEANING TEST ==========")

    for value in test_values:

        cleaned = clean_ocr_text(value)
        valid = is_valid_indian_plate(value)

        print(
            f"Original: {value} | "
            f"Cleaned: {cleaned} | "
            f"Valid Plate: {valid}"
        )