from src.rag_demo import Document, retrieve


def test_retrieve_ranks_matching_document() -> None:
    docs = [
        Document("python", "Python is useful for data work."),
        Document("rag", "RAG retrieves context for grounded answers."),
    ]
    assert retrieve("grounded RAG answers", docs)[0].title == "rag"
