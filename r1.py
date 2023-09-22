def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip()) # 去掉空白和換行功能
    return lines

def convert(lines):
    new = []
    person = None # 先宣告成 None(無)，防程式當掉(未宣告變數的錯誤)
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        # print(line)
        if person: # 如果 person 有值才會執行
            new.append(person + ': ' + line)
    # print(new)
    return new

def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    lines = read_file('input.txt')
    # 顯示出 \ufeff 有編碼符號問題的話，在 encoding 加上 utf-8-sig 去掉符號
    # print(lines)
    lines = convert(lines)
    write_file('output.txt', lines)

main()