def calcularNotaNecessaria(media):
    nota_necessaria = 10 - media
    return max(nota_necessaria, 0)

def dadosDosAlunos():
    all_values = sheet.get_all_values()
    NTotaldeLinhas = len(all_values) - 3
    linha = 4
    i = 0
    totalDeAulasDoSemestre = 60

    while i < NTotaldeLinhas:
        # Obter as pontuações para gerar uma média que posteriormente será utilizada para gerar a situação do aluno
        pontuacao1 = int(sheet.cell(linha, 4).value)
        pontuacao2 = int(sheet.cell(linha, 5).value)
        pontuacao3 = int(sheet.cell(linha, 6).value)
        MediaDasNotasDoAluno = (pontuacao1 + pontuacao2 + pontuacao3) / 3

        # Calcular Minimo de Presença nas aulas e porcentagem necessária para a Não-Reprovação
        porcentagemDePresencaMinima = (25 / 100) * totalDeAulasDoSemestre
        faltasDoAluno = int(sheet.cell(linha, 3).value)

        # Calculo da Nota Final
        notaNecessariaCalculada = calcularNotaNecessaria(MediaDasNotasDoAluno)
        print(notaNecessariaCalculada)

        # Condicionais visando atualização pelo sheet.cell().value da situação do aluno e de sua nota para aprovação final
        if faltasDoAluno < porcentagemDePresencaMinima:
            sheet.cell(linha, 7).value = "Reprovado por Falta"
            sheet.cell(linha, 8).value = "0"
        elif MediaDasNotasDoAluno < 50 and faltasDoAluno >= porcentagemDePresencaMinima:
            sheet.cell(linha, 7).value = "Reprovado por Nota"
            sheet.cell(linha, 8).value = "0"
        elif 50 <= MediaDasNotasDoAluno < 70 and faltasDoAluno >= porcentagemDePresencaMinima:
            sheet.cell(linha, 7).value = "Exame Final"
            sheet.cell(linha, 8).value = "0"
        elif MediaDasNotasDoAluno >= 70 and faltasDoAluno >= porcentagemDePresencaMinima:
            sheet.cell(linha, 7).value = "Aprovado"
            sheet.cell(linha, 8).value = "0"

        # Contadores
        linha += 1
        i += 1

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

spreadsheet_name = "Engenharia de Software – Desafio Gabriel Augusto Diniz Barbosa"

try:
    sheet = client.open(spreadsheet_name).sheet1
    dadosDosAlunos()

except gspread.exceptions.SpreadsheetNotFound:
    print(f"Erro: Planilha '{spreadsheet_name}' não encontrada.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")





