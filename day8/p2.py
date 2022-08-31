def sort_str(input_string: str) -> str:
    return "".join(sorted(input_string))


def parse_file():
    with open("input.txt", "r", encoding="utf-8") as file:
        for line in file:
            inp, out = line.strip().split(" | ")
            yield (map(sort_str, inp.split(" ")), map(sort_str, out.split(" ")))


for inp, out in parse_file():
    inp = list(inp)
    out = list(out)

    arrSegments = []
    
    dic = { 


        }

    for index in range(len(out)):
        out[index] = dic[out[index]]