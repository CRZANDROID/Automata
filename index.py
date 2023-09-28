import tkinter as tk

def validar_automata(input_string, states):
    if len(input_string) != 8:
        return {'success': False, 'message': f'Error: la cadena ingresada debe tener exactamente 8 caracteres.', 'sequence': []}

    current_state = "q0"
    state_sequence = [current_state]

    for char in input_string:
        if char in states[current_state]:
            current_state = states[current_state][char]
            state_sequence.append(current_state)
        else:
            return {'success': False, 'message': f'Autómata no válido, error en el estado {current_state}', 'sequence': state_sequence}

    return {'success': True, 'message': 'Autómata válido', 'sequence': state_sequence}


def validar():
    
    resultado_label.config(text="")
    state_sequence_label.config(text="")

    input_text = entrada.get()
    resultado = validar_automata(input_text, STATES)
    resultado_label.config(text=f"Resultado: {resultado['message']}")
    state_sequence_label.config(text=f"Secuencia de estados: {' -> '.join(resultado['sequence'])}")

def create_gui():
    ventana = tk.Tk()
    ventana.title("Validador de Autómata")
    ventana.geometry("500x500")

    tk.Label(ventana, text="Ingresa el autómata:").pack()
    global entrada
    entrada = tk.Entry(ventana)
    entrada.pack()

    tk.Button(ventana, text="Validar", command=validar).pack()

    global resultado_label
    resultado_label = tk.Label(ventana, text="")
    resultado_label.pack()
    
    global state_sequence_label
    state_sequence_label = tk.Label(ventana, text="")
    state_sequence_label.pack()

    ventana.mainloop()

STATES = {
    'q0': {"5": 'q10', "4": 'q1'},
    'q1': {'-':'q2'},
    'q2': {'B':'q3'},
    'q3': {'U':'q4', 'V':'q4', 'W':'q4','X':'q4','Y':'q4','Z':'q4'},
    'q4':{'-':'q5'},
    'q5':{'0':'q6','1':'q9','2':'q9','3':'q9','4':'q9','5':'q9','6':'q9','7':'q9','8':'q9','9':'q9'},
    'q6':{'1':'q7','2':'q7','3':'q7','4':'q7','5':'q7','6':'q7','7':'q7','8':'q7','9':'q7',},
    'q7':{'F':'q8','G':'q8','H':'q8','I':'q8','J':'q8','K':'q8','L':'q8','M':'q8','N':'q8','O':'q8','P':'q8','Q':'q8','R':'q8',
          'S':'q8','T':'q8','U':'q8','V':'q8','W':'q8','X':'q8','Y':'q8','Z':'q8'},
    'q8':{},
    'q9':{'1':'q7','2':'q7','3':'q7','4':'q7','5':'q7','6':'q7','7':'q7','8':'q7','9':'q7'},
    'q10':{'-':'q11'},
    'q11':{'B':'q12'},
    'q12':{'A':'q13','B':'q13','C':'q13','D':'q13','E':'q13','F':'q13','G':'q13','H':'q13','I':'q13','J':'q13','K':'q13','L':'q13',
           'M':'q13','N':'q13','O':'q13','P':'q13','Q':'q13','R':'q13','S':'q13','T':'q13','U':'q13','V':'q13','W':'q13',
            'X':'q13', 'Y':'q13','Z':'q13'},
    'q13':{'-':'q14'},
    'q14':{'0':'q15','1':'q18','2':'q18','3':'q18','4':'q18','5':'q18','6':'q18','7':'q18','8':'q18','9':'q18'},
    'q15':{'1':'q16','2':'q16','3':'q16','4':'q16','5':'q16','6':'q16','7':'q16','8':'q16','9':'q16'},
    'q16':{'A':'q17','B':'q17','C':'q17','D':'q17','E':'q17','F':'q17','G':'q17','H':'q17','I':'q17','J':'q17','K':'q17','L':'q17',
           'M':'q17','N':'q17','O':'q17','P':'q17','Q':'q17','R':'q17','S':'q17','T':'q17','U':'q17','V':'q17','W':'q17',
            'X':'q17', 'Y':'q17','Z':'q17'},
    'q17':{},
    'q18':{'0':'q16','1':'q16','2':'q16','3':'q16','4':'q16','5':'q16','6':'q16','7':'q16','8':'q16','9':'q16'}
}

if __name__ == "__main__":
    create_gui()
