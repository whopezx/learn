class BrowserHistory:

    def __init__(self, homepage: str):
        self.index = 0
        self.blist = [homepage]

    def visit(self, url: str) -> None:
        # 这里题目中说
        # void visit(string url) 从当前页跳转访问 url 对应的页面  。执行此操作会把浏览历史前进的记录全部删除。
        # 但是我这里相当于把后退的记录也删除了（下面测试），看来是题目中的表达有问题
        self.blist = self.blist[:self.index+1]
        self.index += 1
        self.blist.append(url)
        return None

    def back(self, steps: int) -> str:
        self.index = max(0, self.index-steps)
        return self.blist[self.index]

    def forward(self, steps: int) -> str:
        self.index = min(len(self.blist)-1, self.index+steps)
        return self.blist[self.index]

# Your BrowserHistory object will be instantiated and called as such:
obj = BrowserHistory('homepage')
obj.visit("url1")
obj.visit("url2")
obj.visit("url3")
param_2 = obj.back(1)
param_2 = obj.back(1)
param_3 = obj.back(1)
obj.visit("url4")  # 这里visit完，前面三次back的历史都没了
param_3 = obj.back(2)
# param_2 = obj.back(2)
# param_2 = obj.back(7)