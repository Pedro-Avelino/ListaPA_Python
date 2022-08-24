def delete(list):
    id = []
    for aux in list:
        if aux not in id:
            id.append(aux)
    tuple(id)
    print(id)
    print(min(id))
    print(max(id))