import streamlit as st

def calcular_digito(cpf, peso):
    soma = 0
    for i in range(len(cpf)):
        soma += int(cpf[i]) * peso
        peso -= 1
    resto = soma % 11
    if resto < 2:
        return 0
    else:
        return 11 - resto

def obter_estado_por_oitavo_digito(nono_digito):
    regioes = {
        0: ['RS'],
        1: ['DF', 'GO', 'MT', 'MS', 'TO'],
        2: ['PA', 'AM', 'AC', 'AP', 'RO', 'RR'],
        3: ['CE', 'MA', 'PI'],
        4: ['PE', 'RN', 'PB', 'AL'],
        5: ['BA', 'SE'],
        6: ['MG'],
        7: ['RJ', 'ES'],
        8: ['SP'],
        9: ['PR', 'SC']
    }
    return regioes.get(nono_digito, ['Região desconhecida'])

LOGO_URL_LARGE = "https://streamlit.io/images/brand/streamlit-mark-color.png" 

with st.sidebar:
    st.logo(
        LOGO_URL_LARGE,
        link="https://adolfohugosilvaportifolio.streamlit.app",
        icon_image=LOGO_URL_LARGE,
    )
    st.markdown("""
    📧 Email: adolfohugosilva@gmail.com
                  
     📞 WhatsApp: (82) 99683-8463  
                
     🔗 [LinkedIn](https://www.linkedin.com/in/adolfo-hugo-silva-a298751aa)
                  
     📂 [GitHub](https://github.com/adolfohugosilva)
                
     📄 [Baixar Currículo em PDF](https://drive.google.com/file/d/1Rodf_389YdafdWk6KtJKLjirmitxsa81/view?usp=sharing)
    """)


st.title('Sistema de Validação de CPF')
st.write('Informe os dados solicitados para validar seu CPF.')

nascidos_2011 = st.radio('Seu CPF foi emitido depois de 2011?', ('Sim', 'Não'))

cpf_09 = st.text_input('Digite os 9 primeiros dígitos do seu CPF (somente números):', type = 'password')

if cpf_09:
    cpf_tratado = cpf_09.strip()
    if not cpf_tratado.isdigit() or len(cpf_tratado) != 9:
        st.error('Digite exatamente 9 números.')
    else:           
        if nascidos_2011 == 'Não':
            nono_digito = int(cpf_tratado[8]) 
            estados = obter_estado_por_oitavo_digito(nono_digito)
            digito1 = calcular_digito(cpf_tratado, 10)
            digito2 = calcular_digito(cpf_tratado + str(digito1), 11)

            
            
            st.success(f'Baseado nos dados, seu CPF pode pertencer a um destes estados: {", ".join(estados)}')
            final_cpf_completo = str(digito1) + str(digito2)
            st.success(f'O final do  CPF é: **{final_cpf_completo}**')
            
        else:

            digito1 = calcular_digito(cpf_tratado, 10)
            digito2 = calcular_digito(cpf_tratado + str(digito1), 11)

            final_cpf_completo = str(digito1) + str(digito2)
            
            
        
            st.success(f'O final do  CPF é: **{final_cpf_completo}**')
            
    st.write('Explicação: ')
    st.write('O CPF tem a configuração XXX.XXX.XXX-XX, onde os primeiros oito dígitos são o número-base,' \
    ' o nono define a Região Fiscal (até 2011), o décimo é o "Digito Verificador" (DV) módulo 11 dos nove dígitos anteriores e' \
    ' o último dígito é o DV módulo 11 dos dez dígitos anteriores.')
    st.write('Fonte: http://clubes.obmep.org.br/blog/a-matematica-nos-documentos-a-matematica-dos-cpfs/')

st.markdown("---")
st.markdown("<p style='text-align: right; font-size: 14px;'>© 2025 Adolfo Hugo Silva </p>", unsafe_allow_html=True)
