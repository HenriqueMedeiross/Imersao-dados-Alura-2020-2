dfteste = pd.read_excel('D:/Data/Anexo_II_final-2019.xlsx')
dropados = np.arange(7)
dfteste = dfteste.drop(labels = dropados,axis = 0)
dropados = ['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 12', 'Unnamed: 13']
dfteste = dfteste.drop(labels = dropados,axis = 1)
dfteste = dfteste.reset_index()
dfteste = dfteste.drop(labels = 'index',axis = 1)
colunas = ['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 10', 'Unnamed: 11']
dfteste = dfteste.rename(columns={colunas[1]: 'Municipio',
                        colunas[2]: 'Parcial',
                        colunas[3]: 'Integral'})
dfteste = dfteste.drop(labels = 'Unnamed: 0',axis=1)
dfteste = dfteste.drop(labels = [0,1,2], axis=0)
dfteste = dfteste.reset_index(drop = True)
tamanho_dfteste = np.arange(0,len(dfteste)-3,6)
lista_cidades = []
for i in tamanho_dfteste:
    lista_cidades.append(dfteste.iloc[i][0])
segundo_index_level = []
for i in np.arange(0,len(dfteste)-3,6):
    aux = []
    for a in range(1,6):
        aux.append(dfteste.iloc[i+a][0])
    segundo_index_level.append(aux)
iterables = [lista_cidades,segundo_index_level[1]]
index = pd.MultiIndex.from_product(iterables,names=['Localidade','Tipo_escola'])
valores = []
for i in np.arange(0,len(dfteste)-3,6):
    for a in range(1,6):
        valores.append([dfteste.iloc[i+a][1],dfteste.iloc[i+a][2]])
dftestes = pd.DataFrame(valores,index=index)
dftestes = dftestes.reset_index()
df_escolas = dftestes.query('Localidade != "BRASIL"').reset_index(drop = True)

states = ['Acre', 'Alagoas', 'Amapa', 'Amazonas', 'Bahia', 'Ceara', 'Distrito Federal', 'Espírito Santo', 'Goias', 'Maranhao', 'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais', 'Para', 'Paraiba', 'Parana', 'Pernambuco', 'Piaui', 'Rio de Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul','Rondonia','Roraima','Santa Catarina','Sao Paulo','Sergipe','Tocantins']
states_sem_cidades = ['Acre', 'Alagoas', 'Amazonas', 'Bahia', 'Ceara', 'Distrito Federal', 'Espírito Santo', 'Maranhao', 'Mato Grosso do Sul', 'Minas Gerais', 'Para', 'Paraiba', 'Pernambuco', 'Piaui', 'Rio Grande do Norte', 'Rio Grande do Sul','Rondonia','Roraima','Santa Catarina','Sergipe']
for i in states:
    states[states.index(i)] = states[states.index(i)].upper()
for i in states_sem_cidades:
    states_sem_cidades[states_sem_cidades.index(i)] = states_sem_cidades[states_sem_cidades.index(i)].upper()