from pathlib import Path
import re

README = Path("README.md")
SCREENSHOTS = Path("screenshots")

START = "<!-- SCREENSHOTS:START -->"
END = "<!-- SCREENSHOTS:END -->"

EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".webp"}

def image_grid():
    images = sorted(
        p for p in SCREENSHOTS.iterdir()
        if p.is_file() and p.suffix.lower() in EXTENSIONS
    )

    rows = []

    for i in range(0, len(images), 4):
        row = images[i:i + 4]

        cells = []
        for image in row:
            name = image.stem.replace("_", " ").replace("-", " ")
            cells.append(
                f'''    <td align="center" valign="top">
      <img src="screenshots/{image.name}" width="100%" alt="{name}">
    </td>'''
            )

        while len(cells) < 4:
            cells.append("    <td></td>")

        rows.append(
            "  <tr>\n" +
            "\n".join(cells) +
            "\n  </tr>"
        )

    return (
        f"{START}\n"
        "<table>\n"
        + "\n".join(rows) +
        "\n</table>\n"
        f"{END}"
    )

def main():
    if not README.exists():
        raise SystemExit("README.md not found")

    if not SCREENSHOTS.exists():
        raise SystemExit("screenshots/ directory not found")

    content = README.read_text(encoding="utf-8")

    new_section = image_grid()

    pattern = re.compile(
        re.escape(START) + r".*?" + re.escape(END),
        re.DOTALL
    )

    if pattern.search(content):
        content = pattern.sub(new_section, content)
    else:
        if not content.endswith("\n"):
            content += "\n"

        content += "\n" + new_section + "\n"

    README.write_text(content, encoding="utf-8")

if __name__ == "__main__":
    main()