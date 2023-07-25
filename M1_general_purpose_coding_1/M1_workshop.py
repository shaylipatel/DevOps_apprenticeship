def calculator(operator, int1 , int2):
    try: 
        if operator == '+':
            return int1 + int2
        elif operator == '-':
            return int1 - int2
        elif operator == 'x':
            return int1 * int2
        elif operator == '/':
            return int1 // int2
        else:
            return "Error: Operator not found"
    except Exception as e:
        return f'Error: {e}'
    
def evaluate_goto(line):
    statement = line.split()
    if statement[1] == 'calc':
        return calculator(statement[2], int(statement[3]) , int(statement[3]))
    else:
        return int(statement[1]) - 1
# Step 2 
# with open('M1_calc_step2.txt', 'r+') as calc_input:
#     lines = calc_input.readlines()
#     total = 0 
#     for statement in lines:
#         total += calculator(statement)
    
#     print('Total: {:.2f}'.format(total))

# Step 3
with open('M1_calc_step3.txt', 'r+') as calc_input:
    lines = calc_input.readlines()

    read_lines = []
    line_number = 0
    while True:
        current_line = lines[line_number]
        print(current_line)
        if current_line in read_lines:
            print(f"Line number {line_number + 1}: {current_line}")
            break
        line_number = evaluate_goto(current_line)
        read_lines.append(current_line)
    


