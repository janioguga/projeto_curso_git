# usar a funçao datetime
from datetime import date, time, datetime, timedelta
def trabalhando_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%D/%M/%Y - %H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.year)
    print(data_atual.day)
    print(data_atual.date())
    print(data_atual.weekday())
    print(data_atual.astimezone())
    tupla = ('segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo')
    print('O dia de hoje é:', tupla[data_atual.weekday()])
    tupla_mes = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
    print('O mês atual é:', tupla_mes[data_atual.month])
    data_criada = datetime(2018,6,20, 15,30,20)
    print(data_criada.strftime('%c'))
    data_string = '10/11/1981 12:20:15'
    data_convertida = datetime.strptime(data_string,'%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    print(type(data_convertida))
    nova_data = data_convertida + timedelta(days=365, hours=2, minutes=20)
    print(nova_data)

def trabalhando_date():
    data_atual = date.today()
    print(type(data_atual))
    data_atual = data_atual.strftime('%A/%B/%Y')
    print(data_atual)
    print(type(data_atual))

def trabalhando_time():
    horario = time(hour=18, minute= 25, second= 45)
    horario_str = horario.strftime('%H:%M-%S')
    print(horario)
    print(horario_str)

def exercicio():
    data_exercicio = datetime(1815, 12, 10, 00, 00, 00).strftime('%d/%m/%Y')
    hora_exercicio = time(hour=13, minute=14, second=00)
    print('{} às {}'.format(data_exercicio, hora_exercicio))
    data_atual = datetime.now()
    resultado = data_atual.strftime('%d/%m/%Y %H:%M:%S')
    print(resultado)
    data_viagem = datetime.now() - timedelta(days=1)
    print(datetime.now().weekday())  # retornou 0
    print(data_viagem)


if __name__ == '__main__':
    trabalhando_date()
    trabalhando_time()
    trabalhando_datetime()
    exercicio()
    print('veja como resolver:', datetime.now())
#projeto trabalha com o datetime()
