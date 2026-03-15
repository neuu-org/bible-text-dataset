# Bible Text Dataset

20 Bible translations (7 English + 13 Portuguese) in structured JSON format, organized for NLP, information retrieval, and computational theology research.

Part of the [NEUU](https://github.com/neuu-org) biblical scholarship ecosystem.

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

### English (7)

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

### Portuguese (13)

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

## Structure

```
bible-text-dataset/
├── data/
│   ├── english/           # 7 translations
│   │   ├── KJV.json
│   │   ├── ASV.json
│   │   └── ...
│   └── portuguese/        # 13 translations
│       ├── NVI.json
│       ├── ARA.json
│       └── ...
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

All included Bible translations are in the **public domain** or distributed under open licenses. The structured dataset is released under **CC BY 4.0**.

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
