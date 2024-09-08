from pycallgraph2 import PyCallGraph
from pycallgraph2.output import GraphvizOutput
from main import main_process


# 生成一个函数调用图
def graph():
    # 使用 GraphvizOutput 类生成 Graphviz 输出对象
    graphviz = GraphvizOutput()
    # 将输出文件设置为 main_call_graph.png
    graphviz.output_file = 'main_call_graph.png'
    # 使用 PyCallGraph 库生成函数调用图，并将输出设置为 graphviz 对象
    with PyCallGraph(output=graphviz):
        # p1 和 p2 分别表示两个输入文件路径
        p1 = r'D:\我的文档\Desktop\学校\软件工程\作业\2\test\demo_orig.txt'
        p2 = r'D:\我的文档\Desktop\学校\软件工程\作业\2\test\demo_orig_0.8.txt'
        # 调用 main_process 函数，并将输入文件路径作为参数
        main_process(p1, p2)

if __name__ == '__main__':
    graph()