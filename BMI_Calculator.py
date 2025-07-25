import customtkinter as ctk 

#Configuração da aparência
ctk.set_appearance_mode('dark')

#Criação das funções de funcionalidades
def calcular_imc():
    peso = float(campo_peso.get())
    altura = float(campo_altura.get())
    
    imc = peso / (altura**2)
    imc = round (imc,2)
    

    resultado_imc.configure(text=imc)
    #resultado_texto = ''
    
    if imc < 18.5:
        #resultado_texto = ('Abaixo do peso')
        classificacao_imc.configure(text='Abaixo do peso', 
                                    text_color=("#C2B00F", '#F0EC02'))
    elif imc < 25:
        #resultado_texto = ('Peso normal')
        classificacao_imc.configure(text='Peso normal',
                                    text_color=("#078007", "#3CE625"))
    elif imc < 30:
        #resultado_texto = ('Sobrepeso')
        classificacao_imc.configure(text='Sobrepeso ',
                                    text_color=("#C2B00F", "#F0EC02"))
    elif imc < 35:
        #resultado_texto = ('Obesidade 1')
        classificacao_imc.configure(text='Obesidade 1',
                                    text_color='orange')
    elif imc < 40:
        #resultado_texto = ('Obesidade 2')
        classificacao_imc.configure(text='Obesidade 2',
                                    text_color='orange')
    else:
        #resultado_texto = ('Obesidade mórbida')
        classificacao_imc.configure(text='Obesidade mórbida',
                                    text_color='red')
    
    #classificacao_imc.configure(text=resultado_texto)


#Criação da janela principal
app = ctk.CTk()
app.title('Calculadora de IMC')
app.geometry('350x375')

#Criação dos campos
#label
label_peso = ctk.CTkLabel(app,text='Peso em quilogramas', font=('Arial', 18))
label_peso.pack(pady=5)
#entry 
campo_peso = ctk.CTkEntry(app,placeholder_text='Digite seu peso')
campo_peso.pack(pady=5)
#label
label_altura = ctk.CTkLabel(app,text='Altura em metros', font=('Arial', 18))
label_altura.pack(pady=5)
#entry 
campo_altura = ctk.CTkEntry(app,placeholder_text='Digite sua altura')
campo_altura.pack(pady=5)

#button
button_calcular = ctk.CTkButton(app,text='Calcular',command=calcular_imc)
button_calcular.pack(pady=10)

#campo resultado 
resultado_imc = ctk.CTkLabel(app,text='', font=('Arial', 24))
resultado_imc.pack(pady=5)
classificacao_imc = ctk.CTkLabel(app,text='', font=('Arial', 20))
classificacao_imc.pack(pady=15)


#button dark-light mode
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
