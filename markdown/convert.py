filters_single_line = {
    '# ': ['<h1>', '</h1>'],
    '## ': ['<h2>', '</h2>'],
    '### ': ['<h3>', '</h3>'],
}
filters_inline = {
    '*': ['<strong>', '</strong>'],
    '`': ['<code>', '</code>'],
    '_': ['<em>', '</em>'],
}

file_lines = []
res_line_filter = []
def read_file():
    global file_lines
    fl = open('python.md', 'r')
    file_content = fl.read()
    file_lines = file_content.splitlines()

def filter_lines():
    count =0
    for l in file_lines:
        line = str(l)
        sfilters = filters_single_line.keys()
        for filter in sfilters:
            if line.startswith(filter):
                filter_tags = filters_single_line[filter]
                line = line.lstrip(filter)
                line = filter_tags[0] + line + filter_tags[1]
                file_lines[count] = line
        count += 1

def filter_inlines():
    for l in file_lines:
        line = str(l)
        ifilters = filters_inline.keys()
        for filter in ifilters:
            while line.__contains__(filter):
                index = line.find(filter)
                prev_not_safe = False
                if index != 0:
                    prev_not_safe = True if line[index-1] != '\\' else False
                if prev_not_safe: break
                else:
                    split = line.split(filter)
                    split.replace(filter, filters_inline[filter][0])
                    split.replace(filter, filters_inline[filter][1])



read_file()
filter_lines()
#filter_inlines()
print(file_lines)