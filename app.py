import streamlit as st

st.set_page_config(
    page_title='Meu primeiro site!',
    page_icon='⛬',
    layout='centered'
)
st.title('Meu primeiro site!')

st.header('Meu cabeçalho!')

st.subheader('Meu primeiro subtítulo!')

st.write('Este é um texto teste.')

mostrar_mensagem = st.checkbox('Mostrar mensagem de boas-vindas')

if mostrar_mensagem:
    st.success('Boas-Vindas!')
else:
    st.error('Mensagem de boas-vindas ocultada.')

opcao = st.radio(
    'Qual área você esta aprendendo?',
    ['Programação','Dados','Automação','Outros']
)

if opcao == 'Outros':
    x = st.text_area('Informe quais:')
    if x:
        st.write(x)

nivel = st.selectbox(
    'Qual seu nível?',
    ['Inexperiente','Intermediário','Avançado']
)

horas_de_estudo = st.slider(
    'Quantas horas por semana você estuda?',
     min_value = 0,
     max_value = 40,
     value = 0

)

st.text(f'Você estuda {horas_de_estudo} horas por dia')

if st.button('Enviar respostas',key = '1'):
    st.balloons(),
    st.success('Respostas enviadas com sucesso.')

st.title('Este é outro teste.')

