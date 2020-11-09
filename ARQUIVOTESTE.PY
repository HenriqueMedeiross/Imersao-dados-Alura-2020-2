enem_uberlandia_presentes = enem_uberlandia.query('FALTOU_ALGUM_DIA == 0')['Presenca_automovel'].value_counts(normalize =True)
enem_uberlandia_faltantes = enem_uberlandia.query('FALTOU_ALGUM_DIA == 1')['Presenca_automovel'].value_counts(normalize =True)

faltantes_vs_automoveis_uberlandia = pd.DataFrame({'Faltou algum dia': enem_uberlandia_faltantes,
                                        'Nao faltou': enem_uberlandia_presentes})