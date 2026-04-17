def unbleach(n):
    return n.replace(' ', 's').replace('\t', 't').replace('\n', 'n')

def whitespace(code, inp=''):
    clean_code = [c for c in code if c in ' \t\n']
    iterator = iter(clean_code)

    def get_char():
        try:
            return next(iterator)
        except StopIteration:
            raise Exception("Fin de archivo inesperado (EOF)")

    def read_number():
        sign = get_char()
        if sign == '\n':
            raise Exception("Formato de número inválido: Solo terminal")
        num_str = ''
        while True:
            c = get_char()
            if c == '\n': 
                break
            num_str += '0' if c == ' ' else '1'
        val = int(num_str, 2) if num_str else 0
        return val if sign == ' ' else -val

    def read_label():
        label = ''
        while True:
            c = get_char()
            if c == '\n': 
                break
            label += c
        return label

    instructions = []
    labels = {}

    try:
        while True:
            imp = get_char()
            if imp == ' ': 
                cmd = get_char()
                if cmd == ' ': instructions.append(('push', read_number()))
                elif cmd == '\n':
                    subcmd = get_char()
                    if subcmd == ' ': instructions.append(('dup', None))
                    elif subcmd == '\t': instructions.append(('swap', None))
                    elif subcmd == '\n': instructions.append(('discard', None))
                elif cmd == '\t':
                    subcmd = get_char()
                    if subcmd == ' ': instructions.append(('copy_nth', read_number()))
                    elif subcmd == '\n': instructions.append(('slide', read_number()))
            
            elif imp == '\t':
                imp2 = get_char()
                if imp2 == ' ': 
                    op = get_char() + get_char()
                    if op == '  ': instructions.append(('add', None))
                    elif op == ' \t': instructions.append(('sub', None))
                    elif op == ' \n': instructions.append(('mul', None))
                    elif op == '\t ': instructions.append(('div', None))
                    elif op == '\t\t': instructions.append(('mod', None))
                    else: raise Exception("Comando aritmético desconocido")
                
                elif imp2 == '\t': 
                    cmd = get_char()
                    if cmd == ' ': instructions.append(('store', None))
                    elif cmd == '\t': instructions.append(('retrieve', None))
                    else: raise Exception("Comando de montículo desconocido")
                
                elif imp2 == '\n': 
                    op = get_char() + get_char()
                    if op == '  ': instructions.append(('out_char', None))
                    elif op == ' \t': instructions.append(('out_num', None))
                    elif op == '\t ': instructions.append(('in_char', None))
                    elif op == '\t\t': instructions.append(('in_num', None))
                    else: raise Exception("Comando I/O desconocido")
            
            elif imp == '\n':
                op = get_char() + get_char()
                if op == '  ':
                    label = read_label()
                    if label in labels: raise Exception("Etiqueta duplicada")
                    labels[label] = len(instructions)
                elif op == ' \t': instructions.append(('call', read_label()))
                elif op == ' \n': instructions.append(('jmp', read_label()))
                elif op == '\t ': instructions.append(('jz', read_label()))
                elif op == '\t\t': instructions.append(('jn', read_label()))
                elif op == '\t\n': instructions.append(('ret', None))
                elif op == '\n\n': instructions.append(('exit', None))
                else: raise Exception("Comando de control de flujo desconocido")
    except Exception as e:
        if str(e) != "Fin de archivo inesperado (EOF)":
            raise e

    output = ''
    stack = []
    heap = {}
    ip = 0
    call_stack = []
    inp_pos = 0

    while ip < len(instructions):
        cmd, arg = instructions[ip]

        if cmd == 'push':
            stack.append(arg)
        elif cmd == 'dup':
            if not stack: raise Exception("Pila vacía")
            stack.append(stack[-1])
        elif cmd == 'swap':
            if len(stack) < 2: raise Exception("Pila muy pequeña para Swap")
            stack[-1], stack[-2] = stack[-2], stack[-1]
        elif cmd == 'discard':
            if not stack: raise Exception("Pila vacía")
            stack.pop()
        elif cmd == 'copy_nth':
            if arg < 0 or arg >= len(stack): raise Exception("Índice de copy_nth inválido")
            stack.append(stack[-(arg + 1)])
        elif cmd == 'slide':
            if not stack: raise Exception("Pila vacía")
            top = stack.pop()
            if arg < 0 or arg >= len(stack):
                stack = []
            elif arg > 0:
                stack = stack[:-arg]
            stack.append(top)
        
        elif cmd in ('add', 'sub', 'mul', 'div', 'mod'):
            if len(stack) < 2: raise Exception("Pila muy pequeña para operación aritmética")
            a = stack.pop()
            b = stack.pop()
            if cmd == 'add': stack.append(b + a)
            elif cmd == 'sub': stack.append(b - a)
            elif cmd == 'mul': stack.append(b * a)
            elif cmd == 'div':
                if a == 0: raise Exception("División por cero")
                stack.append(b // a)  
            elif cmd == 'mod':
                if a == 0: raise Exception("Módulo por cero")
                stack.append(b % a)   
        
        elif cmd == 'store':
            if len(stack) < 2: raise Exception("Pila muy pequeña para store")
            val = stack.pop()
            addr = stack.pop()
            heap[addr] = val
        elif cmd == 'retrieve':
            if not stack: raise Exception("Pila vacía")
            addr = stack.pop()
            if addr not in heap: raise Exception("Dirección de montículo no inicializada")
            stack.append(heap[addr])
        
        elif cmd == 'out_char':
            if not stack: raise Exception("Pila vacía")
            output += chr(stack.pop())
        elif cmd == 'out_num':
            if not stack: raise Exception("Pila vacía")
            output += str(stack.pop())
        elif cmd == 'in_char':
            if not stack: raise Exception("Pila vacía")
            addr = stack.pop()
            if inp_pos >= len(inp): raise Exception("No queda input")
            heap[addr] = ord(inp[inp_pos])
            inp_pos += 1
        elif cmd == 'in_num':
            if not stack: raise Exception("Pila vacía")
            addr = stack.pop()
            nl_idx = inp.find('\n', inp_pos)
            if nl_idx == -1: raise Exception("Número en input no termina en salto de línea")
            val_str = inp[inp_pos:nl_idx]
            inp_pos = nl_idx + 1
            heap[addr] = int(val_str)

        elif cmd == 'call':
            if arg not in labels: raise Exception("Etiqueta no encontrada")
            call_stack.append(ip)
            ip = labels[arg]
            continue
            
        elif cmd == 'jmp':
            if arg not in labels: raise Exception("Etiqueta no encontrada")
            ip = labels[arg]
            continue  
            
        elif cmd == 'jz':
            if not stack: raise Exception("Pila vacía")
            if stack.pop() == 0:
                if arg not in labels: raise Exception("Etiqueta no encontrada")
                ip = labels[arg]
                continue  
                
        elif cmd == 'jn':
            if not stack: raise Exception("Pila vacía")
            if stack.pop() < 0:
                if arg not in labels: raise Exception("Etiqueta no encontrada")
                ip = labels[arg]
                continue  
                
        elif cmd == 'ret':
            if not call_stack: raise Exception("Pila de llamadas vacía")
            ip = call_stack.pop() + 1
            continue  
            
        elif cmd == 'exit':
            return output

        ip += 1

    raise Exception("Terminación sucia (Unclean termination)")

# originaal kata: https://www.codewars.com/kata/52dc4688eca89d0f820004c6
# my solution: https://www.codewars.com/kata/reviews/55d7da1ba7692a4d7f00002a/groups/69e1dd324e63d0c41fb6dabb
