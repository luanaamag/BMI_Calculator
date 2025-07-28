import customtkinter as ctk 

# Appearance configuration
ctk.set_appearance_mode('dark')

# Functionality functions
def calculate_bmi():
    try:
        
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        
        if height <= 0:
            bmi_result.configure(text="Erro")
            bmi_classification.configure(text='Altura inválida!', text_color='red')
            return
        
        bmi = weight / (height**2)
        bmi = round(bmi, 2)
        
        bmi_result.configure(text=bmi)
    
        if bmi < 18.5:
            bmi_classification.configure(text='Abaixo do peso', 
                                    text_color=("#C2B00F", '#F0EC02'))
        elif bmi < 25:
            bmi_classification.configure(text='Peso normal',
                                    text_color=("#078007", "#3CE625"))
        elif bmi < 30:
            bmi_classification.configure(text='Sobrepeso',
                                    text_color=("#C2B00F", "#F0EC02"))
        elif bmi < 35:
            bmi_classification.configure(text='Obesidade 1',
                                    text_color='orange')
        elif bmi < 40:
            bmi_classification.configure(text='Obesidade 2',
                                    text_color='orange')
        else:
            bmi_classification.configure(text='Obesidade mórbida',
                                    text_color='red')
    except ValueError:
        bmi_result.configure(text="Erro")
        bmi_classification.configure(text='Entrada inválida! Use números.', text_color='red')
        
    except Exception as e:
        bmi_result.configure(text="Erro")
        bmi_classification.configure(text=f'Ocorreu um erro: {e}', text_color='red')

# Main window creation
app = ctk.CTk()
app.title('Calculadora de IMC')
app.geometry('350x375')
app.resizable(0,0)

# Fields creation
# label
weight_label = ctk.CTkLabel(app, text='PESO (Kg)', font=('Arial', 16))
weight_label.pack(pady=5)
# entry 
weight_entry = ctk.CTkEntry(app, placeholder_text='Digite seu peso')
weight_entry.pack(pady=5)
# label
height_label = ctk.CTkLabel(app, text='ALTURA (m)', font=('Arial', 16))
height_label.pack(pady=5)
# entry 
height_entry = ctk.CTkEntry(app, placeholder_text='Digite sua altura')
height_entry.pack(pady=5)

# button
calculate_button = ctk.CTkButton(app, text='CALCULAR', command=calculate_bmi)
calculate_button.pack(pady=10)

# result field 
bmi_result = ctk.CTkLabel(app, text='', font=('Arial', 24))
bmi_result.pack(pady=5)
bmi_classification = ctk.CTkLabel(app, text='', font=('Arial', 20))
bmi_classification.pack(pady=15)


# dark-light mode button
def switch_event():
    print("switch toggled, current value:", switch_var.get())
    if switch_var.get() == "on":
        ctk.set_appearance_mode('Dark')
    else:
        ctk.set_appearance_mode('Light')

switch_var = ctk.StringVar(value="on")
switch = ctk.CTkSwitch(app, text="Dark mode", command=switch_event,
                       variable=switch_var, onvalue="on", offvalue="off")
switch.pack(pady=5)
app.mainloop()