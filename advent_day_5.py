FILENAME = "/Users/blackbox/Desktop/advent5"
f = open(FILENAME)
strings = []
for line in f:
    strings.append(line.rstrip())
f.close()

rules = {}
printjobs = []


for line in strings:
    if '|' in line:
        r1, r2 = line.split('|')
        if int(r2) in rules:
            update = rules[int(r2)]
            update.append(int(r1))
        else:
            rules[int(r2)] = [int(r1)]
    elif "," in line:
        printjob = line.split(',')
        printjobs.append([int(page) for page in printjob])
    else:
        pass
    
def mid(input_list):
    middle = float(len(input_list))/2
    if middle % 2 != 0:
        return input_list[int(middle - .5)]
    else:
        return (input_list[int(middle)], input_list[int(middle-1)])
    

def valid(printjobs, part1=True):
    validprintjob = []
    notvalidprintjob = []

    for printjob in printjobs:
        #print(printjob)
        for page_index, page_to_be_printed in enumerate(printjob):
            rule_broken = 0
            try:
                rules_for_page_to_be_printed = rules[page_to_be_printed]
                pages_still_to_be_printed = printjob[page_index:]

                for page_still_to_be_printed in pages_still_to_be_printed:
                    if page_still_to_be_printed in rules_for_page_to_be_printed:
                        rule_broken = 1
                        break

                if rule_broken == 1:
                    break
            except:
                continue

        if rule_broken == 1:
            notvalidprintjob.append(printjob)
        else:
            validprintjob.append(printjob)
    
    if part1:
        return(validprintjob, notvalidprintjob)
    else:
        if len(notvalidprintjob) == 0:
            return (1,0)
        else:
            return (0, page_index)


def highest_index(page, job):
    highest_index = 0
    for index, pg in enumerate(job):
        if pg in rules[page]:
            highest_index = index
    return highest_index

def get_index(page, job):
    return job.index(page)

def iterfix(page, pagelist):
    
    hi = highest_index(page, pagelist)
    page_index = get_index(page, pagelist)
    pagelist.pop(page_index)
    pagelist.insert(hi, page)
    
    return pagelist

corrected = []

def part1(printjobs):
    (validprintjob, notvalidprintjob) = valid(printjobs)
    value = 0
    for validjob in validprintjob:
        value+=mid(validjob)
    print(value)
    return notvalidprintjob

    

    
def part2(notvalidprintjob):
    index=0
    for nvpj in notvalidprintjob:

        pagelist = nvpj.copy()
        page = pagelist[index]
        val,error = valid([pagelist], False)

        while not val:
            pagelist = iterfix(page, pagelist)
            val,error = valid([pagelist], False)
            page = pagelist[error]

        corrected.append(pagelist.copy())

    value = 0
    for validjob in corrected:
        value+=mid(validjob)
    print(value)

    
notvalidprintjob = part1(printjobs)
part2(notvalidprintjob)
