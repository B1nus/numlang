def tokenize(source_code):
    source_lines = [line.strip().split() for line in source_code.split("\n")]

    return list(filter(lambda l: len(l) > 0, source_lines))

def parse(tokens):
    statements = []
    labels = {}
    for token_id, token in enumerate(tokens):
        opcode = token[0]

        if opcode.endswith(":"):
            label = opcode[:-1]
            labels[label] = len(statements)
            statements.append(("LABEL", label))
            continue

        match opcode:
            case "PUSH":
                number = int(token[1])
                statements.append((opcode, number))
            case "PRINT":
                statements.append((opcode, ' '.join(token[1:])))
            case "JUMP.EQ.0":
                statements.append((opcode, token[1]))
            case "JUMP.GT.0":
                statements.append((opcode, token[1]))
            case _:
                statements.append((opcode,))

    return statements, labels
