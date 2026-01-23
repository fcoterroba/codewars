def strip_comments(strng, markers):
    def process_line(line):
        min_pos = len(line)
        for marker in markers:
            pos = line.find(marker)
            if pos != -1:
                min_pos = min(min_pos, pos)
        return line[:min_pos].rstrip()
    
    return '\n'.join(process_line(line) for line in strng.split('\n'))

# original kata: https://www.codewars.com/kata/51c8e37cee245da6b40000bd
# my solution: https://www.codewars.com/kata/reviews/553a85a21e0399bb92000153/groups/697328fdaecd33273304f6d3