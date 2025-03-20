import arxiv

# 搜索包含 "machine learning" 的论文，最多返回 5 个结果
search = arxiv.Search(query="machine learning", max_results=5)

# 获取搜索结果
results = search.results()

# 打印结果的标题
for result in results:
    print(result.title)