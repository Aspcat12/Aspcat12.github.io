from pathlib import Path
import json
import re


# ============================================================
# CONFIG
# ============================================================

# โฟลเดอร์ที่เก็บไฟล์ .md
INPUT_DIR = Path(".")

# ไฟล์ catalog ที่จะสร้าง
OUTPUT_FILE = INPUT_DIR / "catalog.json"


# ============================================================
# HELPERS
# ============================================================

def clean_markdown(text: str) -> str:
    """ลบ Markdown พื้นฐานเพื่อใช้เป็น title / description"""
    text = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r"\1", text)          # image
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)           # link
    text = re.sub(r"[*_`~]+", "", text)                            # bold, italic, code
    text = re.sub(r"<[^>]+>", "", text)                            # HTML tag
    text = re.sub(r"\s+", " ", text).strip()

    return text


def get_title(markdown: str, fallback: str) -> str:
    """
    ใช้หัวข้อ Markdown ระดับ 1 ตัวแรก:
    # ชื่อเอกสาร

    ถ้าไม่พบ ใช้ชื่อไฟล์แทน
    """
    match = re.search(r"(?m)^\s*#\s+(.+?)\s*#*\s*$", markdown)

    if match:
        return clean_markdown(match.group(1))

    return fallback


def get_description(markdown: str, title: str) -> str:
    """
    ใช้ย่อหน้าแรกที่ไม่ใช่หัวข้อ, ตาราง, เส้นคั่น, code block
    จำกัดความยาว 160 ตัวอักษร
    """
    lines = markdown.splitlines()
    in_code_block = False

    for raw_line in lines:
        line = raw_line.strip()

        if line.startswith("```"):
            in_code_block = not in_code_block
            continue

        if in_code_block or not line:
            continue

        # ข้ามองค์ประกอบ Markdown ที่ไม่เหมาะใช้เป็นคำอธิบาย
        if line.startswith("#"):
            continue

        if line.startswith(("---", "***", "___", "|", "```")):
            continue

        if re.fullmatch(r"[-*+]\s*", line):
            continue

        cleaned = clean_markdown(line)

        if cleaned and cleaned != title:
            if len(cleaned) > 160:
                return cleaned[:157].rstrip() + "..."

            return cleaned

    return ""


def detect_language(markdown: str) -> str:
    """
    ตรวจแบบคร่าว ๆ ว่ามีไทย/อังกฤษหรือไม่
    """
    thai_chars = len(re.findall(r"[\u0E00-\u0E7F]", markdown))
    english_chars = len(re.findall(r"[A-Za-z]", markdown))

    if thai_chars > 0 and english_chars > 0:
        return "English / ไทย"

    if thai_chars > 0:
        return "ไทย"

    if english_chars > 0:
        return "English"

    return ""


def make_id(filename: str, used_ids: set[str]) -> str:
    """
    แปลงชื่อไฟล์เป็น ID เช่น:
    My Paper Notes.md -> my-paper-notes
    """
    base_id = filename.lower()
    base_id = re.sub(r"\.(md|markdown)$", "", base_id)
    base_id = re.sub(r"[^a-z0-9ก-๙]+", "-", base_id)
    base_id = base_id.strip("-")

    if not base_id:
        base_id = "document"

    result = base_id
    counter = 2

    while result in used_ids:
        result = f"{base_id}-{counter}"
        counter += 1

    used_ids.add(result)

    return result


# ============================================================
# MAIN
# ============================================================

def main():
    md_files = sorted(
        [
            path
            for path in INPUT_DIR.iterdir()
            if path.is_file()
            and path.suffix.lower() in {".md", ".markdown"}
            and path.name != OUTPUT_FILE.name
        ],
        key=lambda path: path.name.lower()
    )

    if not md_files:
        print("ไม่พบไฟล์ .md หรือ .markdown ในโฟลเดอร์นี้")
        return

    catalog = []
    used_ids = set()

    for file_path in md_files:
        try:
            markdown = file_path.read_text(encoding="utf-8-sig")

            fallback_title = file_path.stem.replace("_", " ").replace("-", " ")
            title = get_title(markdown, fallback_title)
            description = get_description(markdown, title)
            language = detect_language(markdown)
            document_id = make_id(file_path.name, used_ids)

            item = {
                "id": document_id,
                "title": title,
                "language": language,
                "description": description,
                "files": [
                    file_path.name
                ]
            }

            catalog.append(item)

            print(f"✓ {file_path.name}")
            print(f"  ID: {document_id}")
            print(f"  Title: {title}")
            print(f"  Language: {language or '-'}")

        except Exception as error:
            print(f"✗ {file_path.name} → ERROR: {error}")

    OUTPUT_FILE.write_text(
        json.dumps(catalog, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    print("\n" + "=" * 60)
    print(f"สร้าง {OUTPUT_FILE.name} สำเร็จ: {len(catalog)} รายการ")
    print("=" * 60)


if __name__ == "__main__":
    main()