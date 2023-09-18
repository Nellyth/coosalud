import csv, io


def read_csv_of_request(file_uploaded):
    csv_list = []
    archivo_texto = io.TextIOWrapper(file_uploaded, encoding='utf-8')
    csv_reader = csv.reader(archivo_texto)
    for fila in csv_reader:
        if fila[0]:
            csv_list.append(fila)

    return csv_list
