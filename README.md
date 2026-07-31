# Bible Text Dataset

17 Bible translations (9 English + 8 Portuguese) in structured JSON format, organized for NLP, information retrieval, and computational theology research.

Part of the [NEUU](https://github.com/neuu-org) biblical scholarship ecosystem.

## Prerequisites: Git LFS

The files under `data/` are stored in **Git LFS**, not in the regular Git
history. Install `git-lfs` *before* cloning, or you will not get the actual
data.

```bash
# Install Git LFS (one-time, per machine)
git lfs install

# Then clone as usual — LFS content downloads automatically
git clone https://github.com/neuu-org/bible-text-dataset.git
```

**Already cloned without Git LFS?** Run this from inside the repo to pull the
real files:

```bash
git lfs install
git lfs pull
```

**How to tell you got pointer files instead of data**: if a JSON file under
`data/` is only ~130 bytes and starts with a line like
`version https://git-lfs.github.com/spec/v1`, Git LFS was not installed when
you cloned — it downloaded a pointer, not the Bible text. Run the recovery
commands above to fix it.

## Overview

| Metric | Value |
|--------|-------|
| Total translations | 17 |
| English versions | 9 |
| Portuguese versions | 8 |
| Embeddings available | 1,057,990 (dual small+large) |
| Format | JSON (book > chapter > verse) |
| Total size | ~98 MB |

## Translations

### English (9)

| Version | Abbreviation | Size |
|---------|:---:|---:|
| King James Version | KJV | 8.2 MB |
| American King James Version | AKJV | 8.2 MB |
| American Standard Version | ASV | 8.2 MB |
| Berean Standard Bible | BSB | 8.0 MB |
| Darby English Bible | Darby | 4.3 MB |
| Douay-Rheims-Challoner | DRC | 9.5 MB |
| Geneva Bible (1599) | Geneva1599 | 4.4 MB |
| Webster's Revision | Webster | 4.4 MB |
| Young's Literal Translation | YLT | 4.3 MB |

### Portuguese (8)

| Version | Abbreviation | Size |
|---------|:---:|---:|
| Almeida Corrigida e Fiel | ACF | 4.1 MB |
| Almeida Revista e Atualizada | ARA | 4.1 MB |
| Almeida Revista e Corrigida | ARC | 3.9 MB |
| Almeida Seculo 21 | AS21 | 3.8 MB |
| Nova Almeida Atualizada | NAA | 4.5 MB |
| Nova Traducao na Linguagem de Hoje | NTLH | 5.1 MB |
| Nova Versao Internacional | NVI | 4.4 MB |
| Nova Vida Nova Traducao | NVT | 4.5 MB |

## Pipeline

```
00_raw  --[normalize.py]-->  01_structured
```

## Structure

```
bible-text-dataset/
├── data/
│   ├── 00_raw/                      # Original files (mixed schemas)
│   │   ├── english/
│   │   └── portuguese/
│   └── 01_structured/               # Normalized to unified schema
│       ├── english/
│       └── portuguese/
├── scripts/
│   └── normalize.py                 # 00_raw -> 01_structured
└── README.md, CHANGELOG.md, LICENSE
```

## Schema

Each JSON file contains a full Bible translation:

```json
{
  "translation": "King James Version (KJV) ...",
  "books": [
    {
      "name": "Genesis",
      "chapters": [
        {
          "chapter": 1,
          "verses": [
            {"verse": 1, "text": "In the beginning God created the heaven and the earth."},
            {"verse": 2, "text": "And the earth was without form, and void..."}
          ]
        }
      ]
    }
  ]
}
```

## License

This dataset is released under **CC BY 4.0**. See [`LICENSE`](LICENSE) for the
full legal text, [`NOTICE`](NOTICE) for the attribution string and
translation provenance notes, and [`CITATION.cff`](CITATION.cff) for citation
metadata.

## Citation

```bibtex
@misc{neuu_bible_text_2026,
  title={Bible Text Dataset: Multilingual Bible Translations in JSON},
  author={NEUU},
  year={2026},
  publisher={GitHub},
  url={https://github.com/neuu-org/bible-text-dataset}
}
```

## Related Datasets (NEUU Ecosystem)

- [bible-commentaries-dataset](https://github.com/neuu-org/bible-commentaries-dataset) — 31,218 patristic commentaries
- [bible-crossrefs-dataset](https://github.com/neuu-org/bible-crossrefs-dataset) — 1.1M+ cross-references
- [bible-topics-dataset](https://github.com/neuu-org/bible-topics-dataset) — 7,873 unified topics
- [bible-hybrid-search](https://github.com/neuu-org/bible-hybrid-search) — Hybrid retrieval research
