#!/usr/bin/env python3
"""
Synthetic Deterministic EPUB Library Generator for KOReader Benchmark
Generates valid EPUBs with deterministic metadata, covers, series, tags, and chapters.
Supports both FLAT and HIERARCHICAL layouts.
"""

import os
import sys
import zipfile
import hashlib
import random
import io
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# Deterministic seed
RANDOM_SEED = 42

AUTHORS = [
    "Arthur C. Clarke", "Isaac Asimov", "Philip K. Dick", "Ursula K. Le Guin",
    "Frank Herbert", "William Gibson", "Neal Stephenson", "Stanislaw Lem",
    "Ray Bradbury", "Robert A. Heinlein", "Dan Simmons", "Gene Wolfe",
    "Iain M. Banks", "Vernor Vinge", "Alastair Reynolds", "Peter F. Hamilton",
    "Cixin Liu", "Ted Chiang", "Greg Egan", "Octavia Butler",
    "Ada Lovelace", "Alan Turing", "Grace Hopper", "Claude Shannon",
    "Donald Knuth", "John von Neumann", "Norbert Wiener", "Leslie Lamport",
    "Barbara Liskov", "Edsger Dijkstra", "Dennis Ritchie", "Ken Thompson"
]

GENRES = [
    ("Fiction/SciFi", "Science Fiction"),
    ("Fiction/Cyberpunk", "Cyberpunk"),
    ("Fiction/SpaceOpera", "Space Opera"),
    ("Fiction/Classics", "Classics"),
    ("Nonfiction/ComputerScience", "Computer Science"),
    ("Nonfiction/Mathematics", "Mathematics"),
    ("Nonfiction/Philosophy", "Philosophy"),
    ("Nonfiction/History", "History"),
]

SERIES_LIST = [
    "Foundation Series", "Dune Chronicles", "Sprawl Trilogy", "Culture Series",
    "Hyperion Cantos", "Revelation Space", "Remembrance of Earth's Past", "The Expanse"
]

NOUNS = ["Star", "Galaxy", "Nebula", "Protocol", "Algorithm", "Silicon", "Empire", "Void",
         "Chronicles", "Matrix", "Cipher", "Dimension", "Horizon", "Singularity", "Vector",
         "Quantum", "Engine", "Network", "Cosmos", "Memory", "Shadow", "Light", "Circuit"]

ADJECTIVES = ["Ancient", "Silent", "Infinite", "Neural", "Digital", "Forgotten", "Synthetic",
              "Parallel", "Cybernetic", "Abstract", "Autonomous", "Luminous", "Dark", "Deep"]


def generate_cover_image(title: str, author: str, series: str = None, series_idx: int = None) -> bytes:
    """Generate a deterministic 600x800 grayscale JPEG cover image."""
    h = int(hashlib.md5(f"{title}:{author}".encode('utf-8')).hexdigest(), 16)
    bg_gray = 200 + (h % 45)  # 200 to 245 light gray

    img = Image.new('L', (600, 800), color=bg_gray)
    draw = ImageDraw.Draw(img)

    draw.rectangle([20, 20, 580, 780], outline=30, width=4)
    draw.rectangle([28, 28, 572, 772], outline=80, width=1)
    draw.rectangle([40, 50, 560, 90], fill=40)

    font_large = ImageFont.load_default()
    font_small = ImageFont.load_default()

    draw.text((60, 62), "KOReader Benchmark Corpus", fill=240, font=font_small)

    shape_type = h % 3
    if shape_type == 0:
        draw.ellipse([150, 160, 450, 460], outline=50, width=3)
        draw.ellipse([180, 190, 420, 430], outline=100, width=2)
    elif shape_type == 1:
        draw.rectangle([160, 160, 440, 440], outline=50, width=3)
        draw.rectangle([190, 190, 410, 410], outline=100, width=2)
    else:
        draw.polygon([(300, 150), (460, 450), (140, 450)], outline=50, width=3)

    draw.text((60, 500), f"Title: {title}", fill=20, font=font_large)
    draw.text((60, 550), f"Author: {author}", fill=40, font=font_large)

    if series:
        draw.text((60, 600), f"Series: {series} (#{series_idx})", fill=60, font=font_small)

    draw.text((60, 720), f"UUID: {h:016x}"[:30], fill=120, font=font_small)

    buf = io.BytesIO()
    img.save(buf, format='JPEG', quality=85)
    return buf.getvalue()


def create_epub(dest_path: Path, title: str, author: str, series: str = None, series_idx: int = None, tags: list = None):
    """Create a strictly valid EPUB file with Dublin Core metadata and cover image."""
    dest_path.parent.mkdir(parents=True, exist_ok=True)

    book_id = f"urn:uuid:{hashlib.md5(f'{title}:{author}'.encode()).hexdigest()}"
    tags = tags or ["Benchmark", "Test"]

    container_xml = """<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>"""

    meta_series = ""
    if series and series_idx is not None:
        meta_series = f"""
    <meta name="calibre:series" content="{series}"/>
    <meta name="calibre:series_index" content="{series_idx}"/>"""

    meta_tags = "\n".join([f'    <dc:subject>{t}</dc:subject>' for t in tags])

    content_opf = f"""<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="BookID" version="2.0">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opf="http://www.idpf.org/2007/opf">
    <dc:title>{title}</dc:title>
    <dc:creator opf:role="aut">{author}</dc:creator>
    <dc:identifier id="BookID" opf:scheme="UUID">{book_id}</dc:identifier>
    <dc:language>en</dc:language>
    <dc:publisher>KOReader Benchmark Suite</dc:publisher>
{meta_tags}
    <meta name="cover" content="cover-image"/>{meta_series}
  </metadata>
  <manifest>
    <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
    <item id="cover-image" href="cover.jpg" media-type="image/jpeg"/>
    <item id="cover" href="cover.xhtml" media-type="application/xhtml+xml"/>
    <item id="chapter1" href="chapter1.xhtml" media-type="application/xhtml+xml"/>
    <item id="chapter2" href="chapter2.xhtml" media-type="application/xhtml+xml"/>
  </manifest>
  <spine toc="ncx">
    <itemref idref="cover" linear="no"/>
    <itemref idref="chapter1"/>
    <itemref idref="chapter2"/>
  </spine>
  <guide>
    <reference type="cover" title="Cover" href="cover.xhtml"/>
  </guide>
</package>"""

    toc_ncx = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE ncx PUBLIC "-//NISO//DTD ncx 2005-1//EN" "http://www.daisy.org/z3986/2005/ncx-2005-1.dtd">
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
  <head>
    <meta name="dtb:uid" content="{book_id}"/>
    <meta name="dtb:depth" content="1"/>
    <meta name="dtb:totalPageCount" content="0"/>
    <meta name="dtb:maxPageNumber" content="0"/>
  </head>
  <docTitle><text>{title}</text></docTitle>
  <navMap>
    <navPoint id="navpoint-1" playOrder="1">
      <navLabel><text>Chapter 1: The Journey Begins</text></navLabel>
      <content src="chapter1.xhtml"/>
    </navPoint>
    <navPoint id="navpoint-2" playOrder="2">
      <navLabel><text>Chapter 2: The Architecture of Speed</text></navLabel>
      <content src="chapter2.xhtml"/>
    </navPoint>
  </navMap>
</ncx>"""

    cover_data = generate_cover_image(title, author, series, series_idx)

    cover_xhtml = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>Cover</title>
  <style type="text/css">
    body {{ margin: 0; padding: 0; text-align: center; }}
    img {{ max-width: 100%; height: auto; }}
  </style>
</head>
<body>
  <div>
    <img src="cover.jpg" alt="Cover"/>
  </div>
</body>
</html>"""

    chapter1_xhtml = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>{title} - Chapter 1</title>
  <style type="text/css">
    body {{ font-family: sans-serif; line-height: 1.5; padding: 1em; }}
    h1 {{ text-align: center; margin-bottom: 1.5em; }}
    p {{ text-indent: 1.5em; margin: 0.5em 0; }}
  </style>
</head>
<body>
  <h1>{title}</h1>
  <h3>by {author}</h3>
  <hr/>
  <h2>Chapter 1: The Journey Begins</h2>
  <p>The dawn broke across the silicon expanse of the horizon. {author}'s tale began not with a whisper, but with the steady hum of machines cycling through their initialization sequences.</p>
  <p>Every parameter was strictly deterministic, every memory address mapped out in advance. In the vast architecture of the digital library, each book stood as a beacon of organized knowledge.</p>
  <p>As the reader turned the page, the ink refreshed smoothly across the electronic canvas, leaving no ghosting behind.</p>
</body>
</html>"""

    chapter2_xhtml = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>{title} - Chapter 2</title>
  <style type="text/css">
    body {{ font-family: sans-serif; line-height: 1.5; padding: 1em; }}
    h2 {{ text-align: center; margin-bottom: 1.2em; }}
    p {{ text-indent: 1.5em; margin: 0.5em 0; }}
  </style>
</head>
<body>
  <h2>Chapter 2: The Architecture of Speed</h2>
  <p>Beneath the surface of the user interface, thousands of layout calculations occurred in fractions of a millisecond. Dirty rectangles merged, partial refreshes pulsed, and the page turned with relentless consistency.</p>
  <p>The benchmark continued onward, recording every byte of memory allocated, every garbage collection cycle, and every frame painted.</p>
</body>
</html>"""

    with zipfile.ZipFile(dest_path, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        z.writestr('mimetype', 'application/epub+zip', compress_type=zipfile.ZIP_STORED)
        z.writestr('META-INF/container.xml', container_xml)
        z.writestr('OEBPS/content.opf', content_opf)
        z.writestr('OEBPS/toc.ncx', toc_ncx)
        z.writestr('OEBPS/cover.xhtml', cover_xhtml)
        z.writestr('OEBPS/cover.jpg', cover_data)
        z.writestr('OEBPS/chapter1.xhtml', chapter1_xhtml)
        z.writestr('OEBPS/chapter2.xhtml', chapter2_xhtml)


def generate_library(base_dir: Path, count: int, mode: str = "hierarchical"):
    """Generate a deterministic library of `count` books in flat or hierarchical mode."""
    base_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(RANDOM_SEED + count)

    print(f"Generating deterministic {mode} library of {count} books at {base_dir}...")
    series_tracker = {s: 1 for s in SERIES_LIST}

    for i in range(count):
        author = rng.choice(AUTHORS)
        adj = rng.choice(ADJECTIVES)
        noun = rng.choice(NOUNS)
        title = f"{adj} {noun} {i+1:04d}"

        is_series = (rng.random() < 0.40)
        series_name = None
        series_idx = None

        if is_series:
            series_name = rng.choice(SERIES_LIST)
            series_idx = series_tracker[series_name]
            series_tracker[series_name] += 1
            folder_rel = f"Series/{series_name}" if mode == "hierarchical" else ""
            tags = ["Series", series_name.split()[0], "Sci-Fi"]
        else:
            folder_genre, genre_name = rng.choice(GENRES)
            folder_rel = folder_genre if mode == "hierarchical" else ""
            tags = [genre_name, "Fiction" if "Fiction" in folder_genre else "Nonfiction"]

        filename = f"{author} - {title}.epub".replace("/", "-")
        book_path = (base_dir / folder_rel / filename) if folder_rel else (base_dir / filename)
        create_epub(book_path, title, author, series_name, series_idx, tags)

    print(f"Successfully generated {count} books in {base_dir}")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: generate_library.py <output_directory> <mode: flat|hierarchical|both> <count_1> [count_2 ...]")
        sys.exit(1)

    out_root = Path(sys.argv[1])
    mode = sys.argv[2].lower()
    counts = [int(c) for c in sys.argv[3:]]

    for c in counts:
        if mode in ("flat", "both"):
            generate_library(out_root / "flat" / f"books_{c}", c, mode="flat")
        if mode in ("hierarchical", "both"):
            generate_library(out_root / "hierarchical" / f"books_{c}", c, mode="hierarchical")
