import streamlit as st
from contract import Sales
from datetime import datetime, time
from pydantic import ValidationError

def main():
  st.title("Sistema de CRM e Vendas da ZapFlow - Frontend Simples")
  email = st.text_input("Campo de texto para inserção do email do vendedor")
  date = st.date_input("Data da compra", datetime.now())
  hour = st.time_input("Hora da compra", value=time(9, 0))  # Valor padrão: 09:00
  value = st.number_input("Valor da venda", min_value=0.0, format="%.2f")
  quantity = st.number_input("Quantidade de produtos", min_value=1, step=1)
  product = st.selectbox("Produto", options=["ZapFlow com Gemini", "ZapFlow com chatGPT", "ZapFlow com Llama3.0"])

  if st.button("Salvar"):
        try:
            date_time = datetime.combine(date, hour)
            
            Sales = Sales(
                email = email,
                date = date_time,
                value = value,
                quantity = quantity,
                product = product
            )
            st.write(Sales)
            # salvar_no_postgres(venda)
        except ValidationError as e:
            st.error(f"Erro: {e}")

if __name__ == "__main__":
  main()