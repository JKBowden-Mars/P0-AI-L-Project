# src/run_local.py

from src.lib.llm_client import analyze_ops_request
from src.lib.validate import validate_output


TEST_INPUTS = [
    "How do I get into that folder leadership told you all to give me access to yesterday? Someone needs to come give me access right now!",
    "Product says the release went out last night, but support is still seeing old behavior. Not sure which one's right.",
    "Not sure if this is an issue yet, but the night shift hasn't posted anything since Monday. No one's complained so far."
]


def main() -> None:
    for i, text in enumerate(TEST_INPUTS, start=1):
        raw = analyze_ops_request(text)
        validated = validate_output(dict(raw))  # ensure plain dict
        print(f"\n--- Result {i} ---")
        for k, v in validated.items():
            print(f"{k}: {v}")


if __name__ == "__main__":
    main()
