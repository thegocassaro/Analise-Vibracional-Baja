with open("path", 'r') as file:
    for line in file:
        
        line = line.strip()  # Remove leading/trailing whitespace
        parts = line.split(';')  # Split line at the semicolon
        
        if len(parts) == 2:
            time = parts[0]
            variables = parts[1].split('=')  # Split the second part at spaces

            # Extract the numbers and values
  
            x = variables[1]
            y = variables[2]
            z = variables[3]

            
            # Process the extracted values
            print("Time:", time)
            print("X:", x)
            print("Y:", y)
            print("Z:", z)
            
        else:
            print("Invalid line format:", line)