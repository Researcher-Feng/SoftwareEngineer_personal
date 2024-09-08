from pycallgraph2 import PyCallGraph
from pycallgraph2.output import GraphvizOutput
from main import main_process


def graph():
    graphviz = GraphvizOutput()
    graphviz.output_file = 'main_call_graph.png'
    with PyCallGraph(output=graphviz):
        p1 = r'D:\我的文档\Desktop\学校\软件工程\作业\2\test\demo_orig.txt'
        p2 = r'D:\我的文档\Desktop\学校\软件工程\作业\2\test\demo_orig_0.8.txt'
        main_process(p1, p2)

if __name__ == '__main__':
    graph()