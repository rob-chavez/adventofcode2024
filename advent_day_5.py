FILENAME = "/Users/blackbox/Desktop/advent5"

def load_data(FILENAME):
    with open(FILENAME) as f:
        lines = [line.rstrip() for line in f]

    rules, printjobs = {}, []
    for line in lines:
        if '|' in line:
            r1, r2 = map(int, line.split('|'))
            rules.setdefault(r2, []).append(r1)
        elif ',' in line:
            printjobs.append([int(page) for page in line.split(',')])
    
    return rules, printjobs
    
def mid(input_list):
    middle = float(len(input_list))/2
    if middle % 2 != 0:
        return input_list[int(middle - .5)]
    else:
        return (input_list[int(middle)], input_list[int(middle-1)])
    

def valid(printjobs, part1=True):
    validprintjob, notvalidprintjob = [], []
    for printjob in printjobs:
        for page_index, page in enumerate(printjob):
            if any(p in rules.get(page, []) for p in printjob[page_index:]):
                notvalidprintjob.append(printjob)
                break
        else:
            validprintjob.append(printjob)

    return (validprintjob, notvalidprintjob) if part1 else ((1, 0) if not notvalidprintjob else (0, page_index))


def highest_index(page, job):
    return next((i for i in range(len(job) - 1, -1, -1) if job[i] in rules[page]), 0)

def get_index(page, job):
    return job.index(page)

def iterfix(page, pagelist):
    pagelist.insert(highest_index(page, pagelist), pagelist.pop(get_index(page, pagelist)))
    return pagelist

def part1(printjobs):
    print(sum(mid(job) for job in valid(printjobs)[0]))
    return valid(printjobs)[1]
    
def part2(notvalidprintjob):
    corrected = []
    for nvpj in notvalidprintjob:
        pagelist = nvpj.copy()
        while not (val := valid([pagelist], False))[0]:
            pagelist = iterfix(pagelist[val[1]], pagelist)
        corrected.append(pagelist)

    print(sum(mid(job) for job in corrected))

    
rules, printjobs = load_data(FILENAME)    
part2(part1(printjobs))
