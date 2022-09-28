def order_list(lista: list, ordem: str, text_field: str) -> list:
    nova_lista = []
    for item in lista:
        if text_field.lower() in str(item).lower():
            nova_lista.append(item)
    return sorted(nova_lista, key=lambda k: k[dicionario_orderby.get(ordem, 'name')])


def filters(lista: list, filter_list: list) -> list:
    tamanho = len(filter_list)

    try:
        if tamanho <= 0:
            return lista
        elif tamanho == 1:
            return list(filter(lambda k: k[filter_list[0]] == True, lista))
        elif tamanho == 2:
            return list(filter(lambda k: k[filter_list[0]] == True and k[filter_list[1]] == True, lista))
        else:
            return list(filter(lambda k: k[filter_list[0]] == True and k[filter_list[1]] == True and k[filter_list[2]] == True, lista))
    except:
        return lista

dicionario_orderby = {
    'nome': 'name',
    'name': 'name',
    'commit': 'updated_at',
    'update': 'updated_at',
    'updated_at': 'updated_at',
    'criacao': 'created_at',
    'created': 'created_at',
    'created_at': 'created_at',
    'id': 'id',
    'project_id': 'id',
    'privado': 'private',
    'private': 'private',
    'pushed': 'pushed_at',
    'pushed_at': 'pushed_at',
    'idioma': 'language',
    'language': 'language',
    'visibility': 'visibility',
    'visibilidade': 'visibility'
}
    

filters_accepted = ('archived', 'disabled', 'has_downloads',
                'has_projects', 'has_issues', 'private', 'fork')
