from fpdf import FPDF
#region "Variáveis"
projeto = input('Digite a descrição do projeto \n')
horas_estimadas = input('Qual o total de horas que você irá trabalhar por dia no projeto? \n')
valor_hora = input('Qual o valor da sua hora? \n')
prazo_conclusao = input('Qual será o prazo total para conclusão do projeto? \n')
#endregion

valor_total = int(horas_estimadas) * int(valor_hora)

#region "Criando PDF"
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial")
pdf.image(r'img\template.png', x=0, y=0)

pdf.text(115, 145, projeto)
pdf.text(115, 160, horas_estimadas)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, prazo_conclusao)
pdf.text(115, 205, str(valor_total))
pdf.output('orçamento.pdf')
print('Orçamento gerado com sucesso!')
#endregion