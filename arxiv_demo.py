import feedparser

# 设置搜索条件
query = "IoT%20Security%20LLM"  # 搜索关键词
max_results = 10          # 最大返回结果数

# 构造 API 请求 URL
url = f"http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results={max_results}"

# 发送请求并解析返回的数据
feed = feedparser.parse(url)

# 打印返回结果的信息
print(f"共找到 {feed.feed.opensearch_totalresults} 篇相关论文")

for entry in feed.entries:
    # 打印论文标题
    print(f"标题: {entry.title}")

    # 打印作者信息
    authors = ", ".join([author.name for author in entry.authors])
    print(f"作者: {authors}")

    # 打印摘要
    print(f"摘要: {entry.summary}")

    # 打印论文链接
    print(f"链接: {entry.link}")

    print("-" * 20)