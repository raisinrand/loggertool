from utils import cmdline
from . import template
import os

def execute(f):
    tp = template.get_template(os.getcwd())
    group_prompts(f, tp.daily_metrics, 0)


# produce all prompts for a habit group
def group_prompts(out, group, indent_level):
    indent = cmdline.indent(indent_level)
    # adapt this to scan entire tree to see if it's empty
    if not is_not_empty(group):
        return
    if isinstance(group,template.Skill):
        used = cmdline.prompt("did you {} today? (yes/no)".format(group.verb))
        if used.lower() != "yes":
            return
        out.write(indent + "{}:".format(group.name) + cmdline.paragraph)
    for h in group.metrics:  
        ans = cmdline.prompt(h.prompt)
        out.write(indent + "    {}: {}".format(h.name,ans) + cmdline.paragraph)
    for c in group.children.values():
        group_prompts(out, c, indent_level + 1)

def is_not_empty(skill : template.MetricGroup) -> bool:
    not_empty = len(skill.metrics) > 0
    for c in skill.children.values():
        not_empty = not_empty or is_not_empty(c)
    return not_empty