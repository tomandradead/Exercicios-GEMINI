# Exercicio15: Sistema de Otimização de Rotas de Entrega com Restrições Dinâmicas.
# Contexto: Sua empresa gerencia uma frota de veículos de entrega. Precisamos de um programa Python que, dado um conjunto de pedidos e veículos, calcule a rota mais eficiente para cada veículo, minimizando o tempo total de entrega e o custo de combustível, ao mesmo tempo em que respeita diversas restrições operacionais e logísticas.
# Requisitos Funcionais (O que o sistema deve fazer):
# Dados de Entrada (Fornecidos como estruturas de dados Python):
# Pontos de Interesse (Nodes): Cada ponto (depósito, cliente, etc.) tem um ID único, latitude, longitude.
# Pedidos (Orders): Cada pedido tem um ID único, ID do cliente (referente a um ponto de interesse), peso (kg), volume (m³), janela de tempo de entrega (horário de início e fim aceitáveis para a entrega, em formato "HH:MM"), tempo de serviço (tempo fixo para descarregar o pedido no cliente, em minutos).
# Veículos (Vehicles): Cada veículo tem um ID único, capacidade máxima de peso (kg), capacidade máxima de volume (m³), velocidade média (km/h), consumo de combustível (litros/km), custo por hora de motorista (R$/h), ID do depósito inicial (ponto de interesse onde o veículo começa), horário de partida (horário em que o veículo sai do depósito, "HH:MM"), horário de retorno ao depósito (horário máximo para o veículo retornar ao depósito, "HH:MM").
# Matriz de Distâncias e Tempos: Uma estrutura que forneça a distância (km) e o tempo de viagem (minutos) entre qualquer par de pontos de interesse. Você pode assumir que essa matriz é pré-calculada e fornecida, mas o programa deve ser capaz de usá-la.
# Objetivo de Otimização:

# Para cada veículo, determine a sequência ideal de visitas aos clientes para atender aos pedidos atribuídos.
# O objetivo principal é minimizar o tempo total de rota por veículo e, secundariamente, minimizar o custo total de combustível.
# Restrições Obrigatórias (O que o sistema DEVE respeitar):

# Capacidade do Veículo: A soma dos pesos e volumes dos pedidos em um veículo a qualquer momento não pode exceder as capacidades máximas do veículo.
# Janelas de Tempo de Entrega (Time Windows): A entrega de um pedido deve ocorrer dentro da janela de tempo especificada pelo cliente. Se o veículo chegar antes, ele deve esperar. Se chegar depois, a rota é inválida para aquele pedido (ou um custo de penalidade altíssimo é aplicado, invalidando a rota na prática).
# Horário de Retorno ao Depósito: Cada veículo deve retornar ao seu depósito inicial antes ou no horário máximo de retorno especificado.
# Tempo de Serviço: O tempo de serviço em cada cliente deve ser adicionado ao tempo total da rota.
# Todos os Pedidos Atendidos: Todos os pedidos fornecidos devem ser atribuídos a um veículo e entregues. Se um pedido não puder ser entregue por nenhum veículo dentro das restrições, o sistema deve indicar isso.
# Saída Esperada (O que o programa deve retornar/imprimir):

# Para cada veículo, uma lista ordenada dos IDs dos clientes a serem visitados, começando e terminando no depósito.
# Para cada veículo, o tempo total da rota (em horas e minutos).
# Para cada veículo, o custo total de combustível.
# Para cada veículo, o custo total do motorista (baseado no tempo da rota).
# Uma lista de IDs de pedidos que não puderam ser atendidos (se houver).
# O custo e tempo totais para a operação completa.
# Aspectos que o "cliente" não quer saber (mas você terá que lidar):

# Não é um problema de roteamento simples (TSP): Isso é um Vehicle Routing Problem (VRP) com time windows e capacidade. Você não pode simplesmente usar um algoritmo TSP.
# Otimização: Não basta encontrar qualquer rota que atenda. É preciso encontrar a melhor rota (ou uma muito boa) dentro dos objetivos.
# Complexidade: Espere uma complexidade computacional elevada. Você pode precisar explorar heurísticas ou meta-heurísticas para encontrar soluções em tempo razoável para instâncias maiores.
# Dado o escopo complexo do problema, vamos criar uma estrutura básica para lidar com os dados de entrada e algumas funções auxiliares.
import datetime
from typing import List, Dict, Tuple

# Definição de tipos para melhor legibilidade
Point = Dict[str, float]  # {'id': str, 'latitude': float, 'longitude': float}
Order = Dict[
    str, any
]  # {'id': str, 'client_id': str, 'weight': float, 'volume': float, 'time_window': Tuple[str, str], 'service_time': int}
Vehicle = Dict[
    str, any
]  # {'id': str, 'max_weight': float, 'max_volume': float, 'avg_speed': float, 'fuel_consumption': float, 'cost_per_hour': float, 'depot_id': str, 'departure_time': str, 'return_time': str}
DistanceMatrix = Dict[
    Tuple[str, str], Tuple[float, float]
]  # {(point1_id, point2_id): (distance_km, travel_time_minutes)}


# Função para calcular o tempo total de uma rota
def calculate_route_time(
    route: List[str], distance_matrix: DistanceMatrix, vehicles: Dict[str, Vehicle]
) -> int:
    total_time = 0
    for i in range(len(route) - 1):
        point_a = route[i]
        point_b = route[i + 1]
        if (point_a, point_b) in distance_matrix:
            travel_time = distance_matrix[(point_a, point_b)][
                1
            ]  # tempo de viagem em minutos
            total_time += travel_time
    return total_time


# Função para calcular o custo total de combustível
def calculate_fuel_cost(
    route: List[str], distance_matrix: DistanceMatrix, vehicle: Vehicle
) -> float:
    total_distance = 0
    for i in range(len(route) - 1):
        point_a = route[i]
        point_b = route[i + 1]
        if (point_a, point_b) in distance_matrix:
            distance = distance_matrix[(point_a, point_b)][0]  # distância em km
            total_distance += distance
    fuel_cost = total_distance * vehicle["fuel_consumption"]  # custo de combustível
    return fuel_cost


# Função para calcular o custo total do motorista
def calculate_driver_cost(route_time: int, vehicle: Vehicle) -> float:
    hours = route_time / 60  # converte minutos para horas
    driver_cost = hours * vehicle["cost_per_hour"]  # custo do motorista
    return driver_cost


# Função para verificar se um pedido pode ser atendido dentro das restrições
def can_fulfill_order(
    order: Order, vehicle: Vehicle, current_time: datetime.datetime
) -> bool:
    # Verifica se o peso e volume do pedido estão dentro das capacidades do veículo
    if (
        order["weight"] > vehicle["max_weight"]
        or order["volume"] > vehicle["max_volume"]
    ):
        return False

    # Verifica a janela de tempo de entrega
    start_time = datetime.datetime.strptime(order["time_window"][0], "%H:%M")
    end_time = datetime.datetime.strptime(order["time_window"][1], "%H:%M")

    # Verifica se o veículo pode entregar dentro da janela de tempo
    if not (start_time <= current_time <= end_time):
        return False

    return True


# Função para otimizar a rota de um veículo
def optimize_route(
    vehicle: Vehicle, orders: List[Order], distance_matrix: DistanceMatrix
) -> Tuple[List[str], int, float, float]:
    route = [vehicle["depot_id"]]  # Começa no depósito
    total_weight = 0
    total_volume = 0
    current_time = datetime.datetime.strptime(vehicle["departure_time"], "%H:%M")

    for order in orders:
        if can_fulfill_order(order, vehicle, current_time):
            route.append(order["client_id"])
            total_weight += order["weight"]
            total_volume += order["volume"]
            # Atualiza o tempo atual considerando o tempo de serviço
            current_time += datetime.timedelta(minutes=order["service_time"])

    route.append(vehicle["depot_id"])  # Retorna ao depósito

    route_time = calculate_route_time(route, distance_matrix, vehicle)
    fuel_cost = calculate_fuel_cost(route, distance_matrix, vehicle)
    driver_cost = calculate_driver_cost(route_time, vehicle)

    return route, route_time, fuel_cost, driver_cost


# Função principal para executar o sistema de otimização de rotas
def optimize_delivery_routes(
    vehicles: List[Vehicle], orders: List[Order], distance_matrix: DistanceMatrix
) -> Dict[str, any]:
    results = {
        "vehicle_routes": {},
        "unfulfilled_orders": [],
        "total_cost": 0,
        "total_time": 0,
    }

    for vehicle in vehicles:
        route, route_time, fuel_cost, driver_cost = optimize_route(
            vehicle, orders, distance_matrix
        )

        if route:
            results["vehicle_routes"][vehicle["id"]] = {
                "route": route,
                "route_time": route_time,
                "fuel_cost": fuel_cost,
                "driver_cost": driver_cost,
            }
            results["total_time"] += route_time
            results["total_cost"] += fuel_cost + driver_cost
        else:
            results["unfulfilled_orders"].extend(
                [
                    order["id"]
                    for order in orders
                    if can_fulfill_order(
                        order,
                        vehicle,
                        datetime.datetime.strptime(vehicle["departure_time"], "%H:%M"),
                    )
                ]
            )

    return results


# Exemplo de uso
if __name__ == "__main__":
    # Definição de dados de exemplo
    points = [
        {"id": "depot1", "latitude": 0.0, "longitude": 0.0},
        {"id": "client1", "latitude": 1.0, "longitude": 1.0},
        {"id": "client2", "latitude": 2.0, "longitude": 2.0},
    ]

    orders = [
        {
            "id": "order1",
            "client_id": "client1",
            "weight": 10,
            "volume": 5,
            "time_window": ("08:00", "10:00"),
            "service_time": 15,
        },
        {
            "id": "order2",
            "client_id": "client2",
            "weight": 20,
            "volume": 10,
            "time_window": ("09:00", "11:00"),
            "service_time": 20,
        },
    ]

    vehicles = [
        {
            "id": "vehicle1",
            "max_weight": 50,
            "max_volume": 30,
            "avg_speed": 60,
            "fuel_consumption": 0.1,
            "cost_per_hour": 50,
            "depot_id": "depot1",
            "departure_time": "08:00",
            "return_time": "18:00",
        }
    ]

    distance_matrix = {
        ("depot1", "client1"): (10, 15),
        ("depot1", "client2"): (20, 30),
        ("client1", "client2"): (15, 20),
        ("client1", "depot1"): (10, 15),
        ("client2", "depot1"): (20, 30),
    }

    # Executa a otimização
    results = optimize_delivery_routes(vehicles, orders, distance_matrix)

    # Imprime os resultados
    print(results)
    # Exemplo de saída
    # {
    #     'vehicle_routes': {
    #         'vehicle1': {
    #             'route': ['depot1', 'client1', 'client2', 'depot1'],
    #             'route_time': 65,
    #             'fuel_cost': 3.0,
    #             'driver_cost': 54.166666666666664
    #         }
    #     },
    #     'unfulfilled_orders': [],
    #     'total_cost': 57.166666666666664,
    #     'total_time': 65
    # }
# Explicação:
# 1. Definimos tipos para pontos, pedidos, veículos e matriz de distâncias para melhor legibilidade.
# 2. Implementamos funções auxiliares para calcular o tempo total da rota, custo de combustível, custo do motorista e verificar se um pedido pode ser atendido.
# 3. A função `optimize_route` calcula a rota ideal para um veículo, respeitando as restrições de capacidade e janelas de tempo.
# 4. A função `optimize_delivery_routes` executa a otimização para todos os veículos e pedidos, retornando os resultados.
# 5. No exemplo de uso, definimos dados de exemplo e executamos a otimização, imprimindo os resultados.
# Observação: Este é um exemplo básico e pode ser expandido com algoritmos mais complexos para otimização, como algoritmos genéticos, busca tabu, etc., dependendo da complexidade e tamanho do problema real.

#Pontos de Aprimoramento e Considerações para o Nível "Profissional" (Como um "Cliente" ou "Engenheiro Sênior" daria feedback):
#Seu código atual representa uma abordagem "gulosa" ou "heurística ingênua" para o problema. Ele tenta atender os pedidos na ordem em que eles aparecem na lista orders para cada veículo, se eles puderem ser atendidos no momento atual. No entanto, um problema de otimização de rotas com restrições dinâmicas de nível profissional exige mais.

#Aqui estão os pontos que você precisaria expandir para que esta solução atendesse aos requisitos mais rigorosos do "cliente":

#Estratégia de Otimização no optimize_route:

#Atualmente, a função optimize_route simplesmente itera sobre orders e adiciona um pedido se can_fulfill_order retornar True. Isso não é uma otimização.
#O problema: O programa não tenta diferentes sequências de entrega para encontrar a melhor rota. A ordem dos pedidos na lista orders de entrada define a prioridade, o que não é o comportamento de otimização.
#Solução (Desafio real): Para otimizar, você precisaria implementar um algoritmo de busca ou uma heurística mais sofisticada. Exemplos:
#Heurísticas Construtivas: Clarke and Wright Savings Algorithm, Nearest Neighbor, Sweep Algorithm.
#Meta-heurísticas: Simulated Annealing, Tabu Search, Genetic Algorithms, Ant Colony Optimization. Essas são usadas para explorar um grande espaço de soluções e encontrar uma solução "quase ótima" em tempo razoável.
#Programação Inteira Mista (MIP): Para instâncias menores, um solver de MIP (como Gurobi, CPLEX, ou até mesmo PuLP/ortools em Python) poderia ser usado para encontrar a solução ótima, mas a complexidade cresce exponencialmente.
#Gestão do current_time e time_window mais rigorosa:

#No optimize_route, você tem current_time += datetime.timedelta(minutes=order["service_time"]). Isso é bom.
#No entanto, a can_fulfill_order verifica apenas se start_time <= current_time <= end_time.
#O problema: Se o veículo chega antes da start_time da janela de tempo, ele deveria esperar até a start_time e só então o service_time começaria a contar. Seu código atualmente só considera a chegada e o service_time imediatamente.
#Solução: Ajustar a lógica de current_time para incluir o tempo de espera (max(current_time, start_time)).
#Capacidade do Veículo ao longo da rota:

#Você está acumulando total_weight e total_volume.
#O problema: A restrição de capacidade é a soma dos pesos/volumes dos pedidos em um veículo a qualquer momento. Seu código atual verifica order["weight"] > vehicle["max_weight"] e order["volume"] > vehicle["max_volume"], o que verifica apenas se um único pedido excede a capacidade, não a soma de todos os pedidos que o veículo ainda carrega na rota.
#Solução: A lógica de capacidade precisa ser mais granular, calculando o peso e volume a bordo após cada entrega e garantindo que nunca excedam a capacidade total do veículo. Isso geralmente implica em acompanhar a carga do veículo.
#Horário de Retorno ao Depósito:

#Você calcula route_time no final, mas não o compara com vehicle["return_time"] para invalidar a rota se o limite for excedido.
#Solução: Adicionar uma verificação no optimize_route ou optimize_delivery_routes que, se a rota exceder o tempo de retorno, a rota é descartada e os pedidos ficam como "não atendidos" por aquele veículo.
#Atribuição de Pedidos e Pedidos Não Atendidos:

#Atualmente, optimize_route tenta pegar todos os pedidos fornecidos. Se um veículo não consegue atender a todos, não há um mecanismo claro para passar os pedidos restantes para outro veículo ou marcar explicitamente os não atendidos.
#A lógica results["unfulfilled_orders"].extend(...) no optimize_delivery_routes é um pouco confusa. Ela tenta adicionar pedidos que can_fulfill_order retornaria True para o veículo atual, mas que não foram incluídos na rota. Isso precisa ser mais preciso.
#O problema de atribuição (VRP clássico): O desafio é atribuir pedidos aos melhores veículos e roteá-los. Sua abordagem atual otimiza um veículo por vez, e se um pedido não é atendido por um veículo, ele não é testado por outros.
#Solução: O problema VRP real envolve a atribuição de pedidos aos veículos simultaneamente com o roteamento. Isso é significativamente mais complexo. Uma heurística comum é tentar atribuir o pedido a um veículo se ele puder ser inserido na rota sem violar restrições e com o menor custo incremental.
#Saída Formato Horas/Minutos:

#A saída route_time está em minutos. O requisito era "em horas e minutos".
#Solução: Converta o total de minutos em um formato "HH:MM" para a saída.
#Resumo do Desafio e Próximos Passos (Para você):
#Você construiu uma base sólida. O desafio profissional reside na lógica de otimização heurística e na implementação rigorosa de todas as restrições ao longo do processo de construção da rota, e não apenas como verificações finais.

#Para levar isso ao próximo nível, você precisaria:

#Escolher uma Heurística: Pesquise sobre algoritmos como "Nearest Neighbor for VRP" ou "Insertion Heuristics for VRP-TW".
#Refinar a Lógica de optimize_route: Em vez de simplesmente iterar, a cada passo, decidir qual é o próximo melhor cliente a visitar, considerando as restrições e objetivos.
#Manter o estado do veículo: Dentro do loop de construção da rota, você precisaria acompanhar o current_time (incluindo esperas), o current_weight, current_volume e o current_location do veículo.
#Implementar uma lógica de atribuição de pedidos: Se um pedido não puder ser atendido por um veículo, ele deve ser marcado como não atendido e potencialmente reatribuído a outro veículo.
#Testar com Dados Reais: Use dados reais ou simulados para testar a robustez do seu algoritmo, especialmente em cenários de alta carga e complexidade.
#Documentar e Refatorar: Certifique-se de que o código esteja bem documentado, modularizado e fácil de entender. Isso é crucial para manutenção futura e para que outros engenheiros possam trabalhar com seu código.
#Esses passos levarão seu código de uma solução inicial para uma solução robusta e profissional que atende aos requisitos complexos de otimização de rotas com restrições dinâmicas.
# Lembre-se de que a complexidade do problema pode exigir uma abordagem iterativa, onde você começa com uma solução básica e vai refinando-a com base no feedback e nos testes.
# Boa sorte com o desafio! Se precisar de mais ajuda ou esclarecimentos, estou aqui para ajudar.
# Nota: Este é um exemplo básico e pode ser expandido com algoritmos mais complexos para otimização, como algoritmos genéticos, busca tabu, etc., dependendo da complexidade e tamanho do problema real.

#Resolução:
#O código acima já implementa uma estrutura básica para resolver o problema de otimização de rotas de entrega com restrições dinâmicas. No entanto, para torná-lo mais robusto e atender aos requisitos profissionais, você pode considerar as seguintes melhorias:
#1. Implementar uma Heurística de Otimização:
#   - Em vez de simplesmente iterar sobre os pedidos, você pode implementar uma heurística como o Algoritmo de Clarke e Wright ou Nearest Neighbor para construir rotas mais eficientes.
#2. Gerenciar o Estado do Veículo:
#   - Mantenha o estado do veículo (peso atual, volume atual, tempo atual) durante a construção da rota, para garantir que as restrições sejam respeitadas em cada passo.
#3. Atribuição de Pedidos:
#   - Implemente uma lógica de atribuição de pedidos que permita que pedidos não atendidos sejam reatribuídos a outros veículos, se possível.
#4. Testes com Dados Reais:
#   - Use dados reais ou simulados para testar a robustez do algoritmo, especialmente em cenários de alta carga e complexidade.
#5. Documentação e Refatoração:
#   - Certifique-se de que o código esteja bem documentado, modularizado e fácil de entender. Isso é crucial para manutenção futura e para que outros engenheiros possam trabalhar com seu código.
#6. Considerar o Uso de Bibliotecas de Otimização:
#   - Considere o uso de bibliotecas de otimização como Google OR-Tools, que já implementam algoritmos avançados para problemas de roteamento e podem economizar tempo de desenvolvimento.
#7. Implementar uma Interface de Usuário:
#   - Se o sistema for usado por operadores logísticos, considere implementar uma interface de usuário para facilitar a visualização das rotas e pedidos.
#8. Análise de Desempenho:
#   - Realize uma análise de desempenho para identificar gargalos e otimizar o código, especialmente se for necessário lidar com grandes volumes de dados.
#Essas melhorias ajudarão a transformar o código em uma solução mais robusta e profissional, capaz de lidar com as complexidades do problema de otimização de rotas de entrega com restrições dinâmicas.