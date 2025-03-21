def replaceSeperater():
    with open("dataK21.csv", "r", encoding='utf-8') as f:
        content = f.read()
    content = content.replace('|', ',')
    with open("K21data.csv", 'w', encoding='utf-8') as f:
        f.write(content)

def swapEmailName():
    with open("K21data.csv", "r", encoding = "utf-8") as f:
        lines = f.readlines()
        
    new_lines = []
    for i, line in enumerate(lines):
        fields = line.strip().split(',')
        
        if i == 0:
            fields[1], fields[2] = fields[2], fields[1]
        else:
            fields[1], fields[2] = fields[2], fields[1]
            
        new_lines.append(','.join(fields))
    
    with open("k21Data.csv", "w", encoding = "utf-8") as f:
        f.write('\n'.join(new_lines))
        
swapEmailName()