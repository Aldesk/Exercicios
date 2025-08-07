import pandas as p

df = p.read_csv('D:/Andre/workspace/Exercícios intermediários/Pandas/Notas alunos com pandas/notas_alunos.csv')
df = df.fillna(0)

# se quisesse alterar só as colunas de nota, poderia fazer assim: 
# df[['Nota1', 'Nota2', 'Nota3']] = df[['Nota1', 'Nota2', 'Nota3']].fillna(0)

df['Media'] = df[['Nota1', 'Nota2', 'Nota3']].mean(axis=1) #fazer .mean das linhas: axis=1 , colunas axis=0
df['Situacao'] = df['Media'].apply(lambda x: "aprovado" if x > 7 else "reprovado")
df.to_csv('D:/Andre/workspace/Exercícios intermediários/Pandas/Notas alunos com pandas/relatorio_final.csv', index=False)