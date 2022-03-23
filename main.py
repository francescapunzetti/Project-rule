import numpy as np

rule30 = {"000": '.',
          "00.": '.',
          "0.0": '.',
          "...": '.',
          "0..": '0',
          ".00": '0',
          ".0.": '0',
          "..0": '0',
         }

def generate_state():
    return ".....0....."

def evolve(stato):
    new_state = '.' + stato + '.'
    #final_state = np.array(len(stato))
    for i in range(1, len(stato)-1):
        for chiave in rule30.keys():
            if new_state[ i-1 : i+2 ] == chiave:
                #final_state[i] = rule30[chiave] 
                #print(rule30[chiave])
                #print(i)
                #print(final_state[i])
                print(new_state[ i-1 : i+2 ])
    return stato

#def evolve(stato):
#    new_state = '.' + stato + '.'
#    final_state = "."
#    for i in range(1, len(stato)+1):
#        for chiave in rule30.keys():
#            if new_state[ i-1 : i+2 ] == chiave:
#                final_state += rule30[chiave] 
#    final_state += "."
#    print(new_state.center(50))
#   return final_state



def simulation(nsteps):
    initial_state = generate_state()
    states_seq = [initial_state]
    for i in range(nsteps):
        old_state = states_seq[-1]
        new_state = evolve(old_state)
        states_seq.append(new_state)
    return states_seq

print(simulation(2))


########################################################

def test_generation_valid_state():
    state = generate_state()
    assert set(state) == {'.', '0'}
    

def test_generation_single_alive():
    state = generate_state()
    num_of_0 = sum(1 for i in state if i=='0')
    assert num_of_0 == 1
