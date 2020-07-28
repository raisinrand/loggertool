import os.path

# a group of metric. either daily_metrics or a skill.
class MetricGroup(object):
    
    def __init__(self, name, metrics, children):
        self.name = name
        self.metrics = metrics
        self.children = children

# a skill to track in log. contains metrics associated with the skill.
class Skill(MetricGroup):

    def __init__(self, name, verb, metrics, children):
        super().__init__(name,metrics,children)
        self.verb = verb

# a metric to track in log
class Metric(object):

    def __init__(self, name, prompt):
        self.name = name
        self.prompt = prompt
        self.type = type

# a log template containing skills and daily metric
class LogTemplate(object):
    def __init__(self, daily_metrics):
        self.daily_metrics = daily_metrics

TEMPLATE_EXTENSION = ".metrics"

# get filename of a path without extension
def filename(path):
    return os.path.splitext(os.path.basename(path))[0]

# attempts to find a skill with the given name in the descendants of skill. if one is found, return it, otherwise return None.
def find_skill(group, name):
    if name in group.children:
        return group.children[name]
    else:
        for child in group.children.values():
            search = find_skill(child, name)
            if search:
                return search
    return None


# read group data and metric from specified file
def parse_group_metric(template, path, is_skill):
    name = filename(path)
    parent = template.daily_metrics
    if find_skill(parent,name):
        return
    with open(path) as file:
        verb = name
        metrics = []
        for line in file.readlines():
            s = line.split(":")
            if len(s) != 2:
                continue
            l = s[0].strip()
            r = s[1].strip()
            if l == "parent":
                parent_name = filename(r)
                search = find_skill(parent,parent_name)
                if search:
                    parent = search
                else:                
                    rel_path = os.path.join(os.path.dirname(path),r)
                    parent = parse_group_metric(template,rel_path,True)
            elif l == "verb":
                verb = r
            else:
                metrics.append(Metric(l,r))
        if is_skill:
            s = Skill(name,verb,metrics,{})
            parent.children[name] = s
            return s
        else:
            parent.metrics.extend(metrics)

def __recurse_build_template(template, path, skill_dir):
    with os.scandir(path) as it:
        for entry in it:
            if entry.name.startswith('.'):
                continue
            if entry.is_file() and entry.name.endswith(TEMPLATE_EXTENSION):
                parse_group_metric(template, entry.path, skill_dir)
            if entry.is_dir():
                entry_skill_dir = skill_dir or (entry.name == "skills")
                __recurse_build_template(template, entry.path, entry_skill_dir)

# construct a template from habit files in the specified directory
def get_template(path):
    template = LogTemplate(MetricGroup("dailies",[],{}))
    __recurse_build_template(template, path, False)
    return template

a = get_template(os.getcwd())
