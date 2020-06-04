
import sys
import os
import jinja2
import tempfile
import subprocess
import json

from io import BytesIO
import base64

from typing import Tuple,Dict,List,Union

import re

from collections import defaultdict

import pandas as pd  # type: ignore
from matplotlib import pyplot as plt # type: ignore
import markdown # type: ignore
import fire # type: ignore

from dataclasses import dataclass

@dataclass
class State:
    ELS: Dict[str,List[str]]
    BID: Union[str,None]

STATE = State({},None)

env = jinja2.Environment(
    loader = jinja2.PackageLoader("hyperpub")
)

def rndrplot()-> None:
    global STATE
    b = BytesIO() 
    plt.savefig(b,format="png")
    b.seek(0)
    b64pic = base64.b64encode(b.read()).decode()
    el = f'<img src="data:image/png;base64,{b64pic}"></a>\n\n'
    if STATE.BID:
        STATE.ELS[STATE.BID].append(el)
    else:
        raise ValueError("Tried to add element without BID")
            
    return 

def rndrtable(df: pd.DataFrame)->None:
    global STATE
    html = df.to_html()
    html = '<div class="table-container">'+html+'</div>'
    if STATE.BID:
        STATE.ELS[STATE.BID].append(html)
    else:
        raise ValueError("Tried to add element without BID")
    return 

def codeblocks(rawMarkdown: str) -> str:
    global STATE
    """
    Reserved globals:
        STATE
    """
    codeblocks = re.findall("^```(?:\{[^\}]+\})$[^```]+^```$",rawMarkdown,re.MULTILINE)
    markdown = re.sub("```(\{[^\}]+\})[^```]+```","\g<1>",rawMarkdown,re.MULTILINE)

    def parseBlock(block):
        lead,*code = block.split("\n")[:-1]
        name = re.search("\{[^\}]+\}",lead)[0]
        return name,"\n".join(code)

    namedCodeBlocks = {name:code for name,code in [parseBlock(block) for block in codeblocks]}

    code = [] 

    for name,codeblock in namedCodeBlocks.items():
        STATE.ELS[name] = []
        code += [f"STATE.BID='{name}'"]
        code += [f"print('Running {name}')"]
        code += codeblock.split("\n")

    exec("\n".join(code),{"STATE":STATE,"rndrplot":rndrplot,"rndrtable":rndrtable})
    
    for bid,els in STATE.ELS.items():
        els = ['<div class="result">'+e+'</div>' for e in els]
        markdown = re.sub(bid,"\n".join(els),markdown)
    
    return markdown

def render(filename,out):
    with open(filename) as f:
        md = f.read()
        md = codeblocks(md)
        md = markdown.markdown(md)
        tmpl = env.get_template("doc.html")
        rnd = tmpl.render(text=md)
        with open(out,"w") as f:
            f.write(rnd)

if __name__ == "__main__":
    fire.Fire(render)
