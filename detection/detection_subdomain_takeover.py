import re
from pathlib import Path


def detect_subdomain_takeover(log_file):
    text = Path(log_file).read_text().lower()

    has_cname = "record: cname" in text
    has_external_provider = "provider:" in text
    has_error = bool(
        re.search(
            r"status:\s*404|no such application|not found|unknown host|resource does not exist",
            text
        )
    )

    if has_cname and has_external_provider and has_error:
        print(f"🚨 ALERT: Possible Subdomain Takeover Exposure")
        print(f"   Log: {log_file}")
        return True

    print(f"✅ No alert: {log_file}")
    return False


if __name__ == "__main__":
    attack_log = "../logs/attack_sample.log"
    benign_log = "../logs/benign_sample.log"

    print("=== Subdomain Takeover Detection Test ===\n")

    detect_subdomain_takeover(attack_log)
    detect_subdomain_takeover(benign_log)