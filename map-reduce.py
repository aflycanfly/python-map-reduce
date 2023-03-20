import multiprocessing as mp

# get the lines from the file
def get_lines():
    # open the file 
    with open('Train_Data.csv', 'r') as f:
        lines = f.readlines()

    # split the lines into a list of lists
    lines = [line.strip().split(',') for line in lines]
    # delete the header
    del lines[0]
    # save line  index 3 to 5 and 17 to 20
    lines = [line[3:5] + line[17:20] for line in lines]
    return lines

# map function get the line and return a dictionary
def mapper(line):
    line_dict = {}
    line_dict['residence_space'] = line[0]
    line_dict['building_space'] = line[1]
    line_dict['exchange_rate'] = line[2]
    line_dict['unit_price_of_residence_space'] = line[3]
    line_dict['unit_price_of_building_space'] = line[4]
    return line_dict
  
# reduce function get the dictionary and return the total cost
def reducer(line_dict):
    # (The unit price of residence space * Residence space + Unit price of building space * Building space) * Exchange rate = Total cost. 
    residence_space=float(line_dict['residence_space'])
    unit_price_of_residence_space=float(line_dict['unit_price_of_residence_space'])
    building_space=float(line_dict['building_space'])
    unit_price_of_building_space=float(line_dict['unit_price_of_building_space'])
    exchange_rate=float(line_dict['exchange_rate'])
    return (unit_price_of_residence_space * residence_space + unit_price_of_building_space * building_space) * exchange_rate

# save the total cost to the file
def save_to_file(all_total_cost):
    with open('Train_Data.csv', 'r') as f:
        lines = f.readlines()
        lines = [line.strip().split(',') for line in lines]   

    for i in range(1,len(lines)):
        lines[i][20]=str(all_total_cost[i-1])

    with open('Done_Data.csv', 'w') as f:
        for line in lines:
            f.write(','.join(line))
            f.write('\n')
    
if  __name__ == '__main__' :
    # get the lines from the file
    lines = get_lines()

    # Open 5 threads to call mapper1
    with mp.Pool(5) as pool:
        line_dict = pool.map(mapper, lines)
    
    
    # open 2 threads to call reducer
    with mp.Pool(2) as pool:
        all_total_cost = pool.map(reducer, line_dict)

    # save the total cost to the a new file
    save_to_file(all_total_cost)

