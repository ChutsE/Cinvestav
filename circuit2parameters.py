import numpy as np

component_value = {
    "R1": 100,
    "L1": .01,
    "R2": 1000,
    "C1": 0.00001
}
#nodes = np.array([["R1","C1","In"],["R2","C1","L1"],["R1","R2","Out"]])
nodes = np.array([["C1","In"],["R2","C1","L1"],["R2","Out"]])

def get_circuit_matrix(component_value : dict, nodes : np.array) -> np.array:
    """This function calculate the circuit matriz based of nodes
    
    Args:
        component_value (dict): It's a dict with the component values
        nodes (np.array): It's a matrix where "y" elements are the nodes and 
                          each node contain the components into there.

    Returns:
        np.array: Returns the characteristic matrix of the circuit
    """

    circuit_matrix_len = nodes.shape[0]
    circuit_matrix = np.zeros((circuit_matrix_len, circuit_matrix_len), dtype=complex)
    
    #This section fills the diagonal of circuit matrix 
    for j in range(circuit_matrix_len):
        for i in range(circuit_matrix_len):
            if i == j:
                acc = complex(0,0)
                for comp in nodes[j]:
                    if not ((comp == "In") or (comp == "Out")):
                        acc += 1/component_impedance(comp, component_value[comp])
                circuit_matrix[j,i] = acc
    
    #This section search the component pair in other nodes 
    #and if it find it in n node, n will be the position where will be filled in circuit matrix.
    for j, node in enumerate(nodes):
        for component_name in node:

            if component_name == "In":
                Node_In = j
                continue
            elif component_name == "Out":
                Node_Out = j
                continue

            node_num = finder(j, nodes, component_name)

            if node_num > -1:
                circuit_matrix[j, node_num] = -1/component_impedance(component_name, component_value[component_name])
            
    return circuit_matrix

def finder(row : int, nodes : np.array,  component_name : str) -> int:
    """This function find the component pair and returns the node number where it was allocated.

    Args:
        row (int): Current row of circuit matrix .
        nodes (np.array): nodes matrix.
        component_name (str): component name want to find it.

    Returns:
        int: Node number where component pair was found, -1 if didn't find it.
    """
    for i, node in enumerate(nodes):
        if (i != row) and (component_name in node):
            return i
    return -1

F = 10000
W = 2*np.pi*F
def component_impedance(component_name : str, component_value: float) -> complex:
    if component_name[0] == "R":
        return component_value
    elif component_name[0] == "C":
        return complex(0,-1/(W*component_value))
    elif component_name[0] == "L":
        return complex(0,W*component_value)
    
print(get_circuit_matrix(component_value, nodes))