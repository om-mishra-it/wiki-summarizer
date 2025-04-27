from tools.fetch_article_tool import fetch_wikipedia_article
from llm.router import build_graph


def main():
    url = input("Enter Wikipedia URL: ").strip()
    article_text = fetch_wikipedia_article(url)
    if not article_text:
        print("Failed to fetch article.")
        return

    graph = build_graph()
    output = graph.invoke({"article": article_text})

    print("\n=== Summary ===\n")
    print(output["summary"])


if __name__ == "__main__":
    main()
