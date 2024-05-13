import streamlit as st
st.title(':red[Calculadora básica]')
st.write(' ')
st.write(' ')
st.write('Feita por :violet[Thiago] e :green[Vinícius]!!!')
st.write(' ')
st.write(' ')

num1 = st.number_input("Insira o primeiro número: ", value= None, placeholder='Insira aqui...')
num2 = st.number_input("Insira o segundo número: ", value= None, placeholder='Insira aqui...')
result = 0
def soma(num1, num2):
     return num1 + num2
def subtracao(num1, num2):
    return num1 - num2
def multiplicacao(num1, num2):
    return num1 * num2
def divisao(num1, num2):
    return num1 / num2
def pot(num1, num2):
    return num1 ** num2
def mod(num1, num2):
    return num1 % num2

op = st.selectbox(
    "Escolha uma operação",
    ("Soma", "Subtração", "Multiplicação", "Divisão", 'Potenciação', 'Módulo'),
    index = None,
     placeholder= 'Selecione aqui...')

result = st.button(":red[Calcular]")
if result:
    if op == "Soma":
        result = soma(num1, num2)
    elif op == "Subtração":
        result = subtracao(num1, num2)
    elif op == "Multiplicação":
        result = multiplicacao(num1, num2)
    elif op == "Divisão":
        result = divisao(num1, num2)
    elif op == 'Potenciação':
        result = pot(num1, num2)
    elif op == 'Módulo':
        result = mod(num1, num2)
    else:
        st.write("Escolha uma operação antes de calcular!")


    st.write('Resultado:', result)