import pandas as pd
import os

#caminho_arquivo = r"#:\#\#\#\Back log 2024-2025.xlsx"
caminho_arquivo = "Back log 2024-2025.xlsx"
def verificar_e_converter_arquivo(caminho):
    extensao = os.path.splitext(caminho)[1]

    if extensao == '.csv':
        df = pd.read_csv(caminho)
        novo_caminho = caminho.replace('.csv', '.xlsx')
        df.to_excel(novo_caminho, index=False)
        return novo_caminho
    elif extensao == '.xlsx':
        return caminho
    else:
        raise ValueError("Formato de arquivo não suportado. Por favor, forneça um arquivo .csv ou .xlsx")

caminho_convertido = verificar_e_converter_arquivo(caminho_arquivo)

# Read Excel'Plan2', skipping t-1°s lines tht are not headers
plan2 = pd.read_excel(caminho_convertido, sheet_name='Plan2', skiprows=2)

print("Dados iniciais da Plan2:")
print(plan2.head())

# Convert colunmn"Soma de Valor Contrato"t/n°(if hasn't been)
plan2['Soma de Valor Contrato'] = pd.to_numeric(plan2['Soma de Valor Contrato'], errors='coerce')

# Convert t/MoneyType->real (R$)
plan2['Soma de Valor Contrato'] = plan2['Soma de Valor Contrato'].apply(lambda x: f'R${x:,.2f}')

# Organize data->From Highest Value t/t-Lowest
plan2.sort_values(by='Soma de Valor Contrato', ascending=False, inplace=True)

print("Dados organizados da Plan2:")
print(plan2.head())

# Save-organizedData in a new ExcelFile
#caminho_saida = r"#:\#\#\#\Plan2_Organizada.xlsx"
caminho_saida = "Plan2_Organizada.xlsx"
plan2.to_excel(caminho_saida, index=False)

print(f"Dados organizados foram salvos em: {caminho_saida}")
