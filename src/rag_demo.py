"""Small, dependency-light retrieval example for the RAG starter."""

from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class Document:
    title: str
    text: str


def retrieve(query: str, documents: list[Document], limit: int = 3) -> list[Document]:
    """Return documents ranked by the number of query terms they contain."""
    terms = set(re.findall(r"[a-z0-9]+", query.lower()))
    scored = []
    for document in documents:
        words = set(re.findall(r"[a-z0-9]+", document.text.lower()))
        scored.append((len(terms & words), document))
    return [document for score, document in sorted(scored, key=lambda item: item[0], reverse=True) if score][:limit]


def main() -> None:
    documents = [
        Document("RAG", "Retrieval augmented generation grounds answers in retrieved context."),
        Document("Evaluation", "Retrieval quality should be measured with representative questions."),
    ]
    query = input("Question: ").strip()
    for document in retrieve(query, documents):
        print(f"[{document.title}] {document.text}")


if __name__ == "__main__":
    main()
