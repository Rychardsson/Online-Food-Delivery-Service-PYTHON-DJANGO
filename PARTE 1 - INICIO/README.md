# Online-Food-Delivery-Service-PYTHON-DJANGO
Online Food Delivery Service

1 - Restaurant Profile Management:

Este projeto consiste em um script em Python que oferece funcionalidades para gerenciar um restaurante, seu menu e preços, utilizando um banco de dados SQLite para armazenamento eficiente de dados.

Funcionalidades Principais:

Configuração automática do banco de dados SQLite para armazenar informações sobre restaurantes, itens de menu e preços.

Classes organizadas para representar Restaurantes, Menus, Itens de Menu e Preços, proporcionando uma estrutura clara e modular.

Interface interativa com o usuário para adicionar itens de menu e definir preços, utilizando loops intuitivos.

Estrutura do Projeto:

restaurant_management.py: Script principal contendo as classes e funcionalidades.

database: Pasta contendo o arquivo do banco de dados SQLite.

Instruções de Uso:

Execute o script restaurant_management.py.

Siga as instruções para configurar o restaurante, adicionar itens de menu e definir preços.

O script interage com o banco de dados automaticamente.

Classes Principais:

Restaurant

Representa um restaurante e gerencia perfil, menu e preços.

Métodos: save_to_db, update_db_profile, display_profile, create_tables.

Menu

Representa um menu e gerencia a adição de itens e exibição do menu.

Métodos: add_item, display_menu.

MenuItem

Representa um item de menu com nome, descrição e preço.

Métodos: save_to_db, get_restaurant_id.

Prices

Gerencia preços para itens de menu.

Métodos: set_price, display_prices, save_price_to_db.

2 - Order Placement and Management:

Este é um simples sistema de pedidos em Python que utiliza o SQLite para armazenar informações sobre usuários e seus pedidos.

Funcionalidades Principais:

Classe User

Representa um usuário com um identificador único, nome de usuário e uma lista de pedidos.

Métodos: place_order, track_orders.

Classe Order

Representa um pedido com um identificador único, uma lista de itens e um status inicial de "Pendente".

Métodos: update_status, save_to_db.


Estrutura do Projeto:
order_system.py: Script principal contendo as classes User e Order e funcionalidades principais.

restaurant_data.db: Banco de dados SQLite para armazenar informações sobre pedidos.


3 - Delivery Tracking:

Este script em Python implementa um sistema de rastreamento de entregas, simulando o status de entregas em diferentes etapas. O sistema utiliza um banco de dados SQLite para armazenar informações sobre as entregas.


Funcionalidades Principais:


Classe Delivery

Representa uma entrega com um identificador único e um status padrão de "Pending" (Pendente).

Método: update_status para atualizar o status da entrega.

Classe DeliveryTracker

Gerencia o rastreamento de múltiplas entregas.

Métodos: add_delivery, update_delivery_status, get_delivery_status, save_delivery_to_db, update_delivery_in_db.

Função simulate_delivery_tracking

Simula o rastreamento de entrega, atualizando os status para "Em Andamento" e "Entregue" em intervalos de tempo.


Instruções de Uso

Execute o script delivery_tracking.py.

O sistema consulta o banco de dados para obter os IDs dos pedidos existentes.

Cria uma entrega para cada pedido e adiciona ao rastreador.

Simula o rastreamento de entrega, atualizando os status em intervalos de tempo.

Exibe os status finais de cada entrega.


4 - Payment Processing:

Este script em Python implementa um sistema de pagamentos que aceita diferentes métodos de pagamento, como cartão de crédito, PayPal e Bitcoin. Os pagamentos são processados e registrados em um banco de dados SQLite.

Funcionalidades Principais:

Classe Payment

Representa um pagamento com um valor e ID do pedido associado.

Método: process_payment é uma função abstrata que deve ser implementada pelas subclasses.

Método: save_payment_to_db salva informações do pagamento no banco de dados.

Classe CreditCardPayment (Subclasse de Payment)

Representa um pagamento com cartão de crédito, incluindo número do cartão, data de validade e CVV.

Método process_payment: Imprime a mensagem de processamento e salva o pagamento no banco de dados.

Classe PayPalPayment (Subclasse de Payment)

Representa um pagamento usando o serviço PayPal, incluindo o endereço de e-mail associado.

Método process_payment: Imprime a mensagem de processamento e salva o pagamento no banco de dados.

Classe BitcoinPayment (Subclasse de Payment)

Representa um pagamento usando Bitcoin, incluindo o endereço Bitcoin.

Método process_payment: Imprime a mensagem de processamento e salva o pagamento no banco de dados.


Instruções de Uso

Execute o script payment_system.py.

Insira o ID do pedido e o valor do pagamento quando solicitado.

O sistema cria instâncias de CreditCardPayment, PayPalPayment e BitcoinPayment com informações fictícias.

Os pagamentos são processados e registrados no banco de dados.


5 - Customer Reviews and Ratings:

Este script em Python simula um sistema de avaliações de pratos em restaurantes, permitindo que os clientes adicionem avaliações aos pratos. As informações são armazenadas em um banco de dados SQLite.

Funcionalidades Principais:

Classe Review

Representa uma avaliação de um cliente para um prato específico.

Método: save_review_to_db salva a avaliação no banco de dados.

Classe Dish

Representa um prato com nome, descrição e uma lista de avaliações associadas.

Métodos: add_review para adicionar uma avaliação ao prato, average_rating para calcular a avaliação média.

Classe Restaurant

Representa um restaurante com nome, culinária e uma lista de pratos associados.

Métodos: add_dish para adicionar um prato ao restaurante, get_dish_by_name para encontrar um prato pelo nome.


Instruções de Uso

Execute o script restaurant_reviews.py.

Insira o nome e a culinária do restaurante.

Calcule e exiba a avaliação média de um prato específico.


6 - Promotion and Discount Management:

Este script em Python implementa um sistema de gerenciamento de promoções e descontos em restaurantes, utilizando um banco de dados SQLite para armazenar informações. Abaixo estão as funcionalidades principais do sistema:

Funcionalidades Principais:

Classe Promotion

Representa uma promoção com nome, descrição, data de início, data de término e ID do restaurante associado.

Método: save_to_db salva a promoção no banco de dados.

Método: is_valid verifica se a promoção é válida em uma determinada data.

Classe Discount

Representa um desconto com nome, valor, tipo de desconto ('percentage' ou 'fixed') e ID do restaurante associado.

Método: save_to_db salva o desconto no banco de dados.

Método: apply_discount aplica o desconto ao preço original.

Classe Restaurant

Representa um restaurante com nome, contendo listas de promoções e descontos associados.

Métodos: add_promotion e add_discount para adicionar promoções e descontos, respectivamente.

Método: get_valid_promotions retorna promoções válidas em uma determinada data.

Método: apply_discount aplica um desconto específico ao preço original.


Instruções de Uso:

Execute o script restaurant_promotions.py.

Adicione promoções e descontos ao restaurante.

Informe a data desejada para verificar as promoções válidas.

Aplique um desconto específico ao preço original.


7 - Order History:

Este script em Python implementa um sistema simples de pedidos e histórico de usuários utilizando um banco de dados SQLite. Abaixo estão as funcionalidades principais do sistema:

Funcionalidades Principais:

Classe Order

Representa um pedido com um ID único, ID do usuário, itens do pedido e preço total.

Método: display_order exibe as informações do pedido.

Método: save_to_db salva o pedido e seus itens associados no banco de dados.

Método de classe: load_from_db carrega um pedido existente a partir do banco de dados.

Classe User

Representa um usuário com ID único, nome e uma lista de pedidos.

Métodos: place_order para fazer um novo pedido, view_order_history para visualizar o histórico de pedidos e reorder_favorite para reordenar um pedido anterior.

Método de classe: load_orders_by_user_id carrega todos os pedidos associados a um ID de usuário existente no banco de dados.


Instruções de Uso

Execute o script order_system.py.

Insira um ID de usuário e o nome do usuário.

Faça pedidos usando o método place_order.

Visualize o histórico de pedidos com view_order_history.

Reordene um pedido anterior com reorder_favorite.


8 - Customizable Delivery Options:

Este script em Python implementa um sistema de opções de entrega para pedidos, permitindo que os usuários especifiquem detalhes como o horário de entrega e instruções especiais. Abaixo estão as funcionalidades principais do sistema:

Funcionalidades Principais:

Classe DeliveryOptions

Representa as opções de entrega para um pedido, como horário de entrega e instruções especiais.

Métodos: set_delivery_time e set_special_instructions para definir o horário de entrega e instruções especiais, respectivamente.

Métodos: get_delivery_time e get_special_instructions para obter o horário de entrega e instruções especiais, respectivamente.

Métodos: save_to_db para salvar as opções de entrega no banco de dados associado a um pedido.

Método de classe: load_from_db para carregar as opções de entrega de um pedido existente a partir do banco de dados.


Instruções de Uso

Execute o script delivery_options.py.

Insira um ID de pedido.

Defina as opções de entrega, como horário de entrega e instruções especiais.

Salve as opções de entrega no banco de dados.

Carregue as opções de entrega do banco de dados e exiba-as.


9 - Customer Support Interface:

Este script em Python implementa um sistema simples de pedidos e clientes que utiliza um banco de dados SQLite para armazenar informações. Aqui estão as principais funcionalidades do sistema:

Funcionalidades Principais:

Classe Order

Representa um pedido com um número de pedido e uma lista de produtos.

Método **str** para fornecer uma representação de string legível para o pedido.

Método save_to_db para salvar o pedido no banco de dados associado a um cliente.

Método de classe load_from_db para carregar os pedidos de um cliente existente a partir do banco de dados.

Classe Customer

Representa um cliente com informações como nome, e-mail e número de telefone.

Método place_order para permitir que o cliente faça um pedido e o salve no banco de dados.

Método save_to_db para salvar as informações do cliente no banco de dados.

Método get_customer_id para obter o ID do cliente a partir do banco de dados.

Método de classe load_from_db para carregar informações do cliente existente a partir do banco de dados.


Instruções de Uso

Execute o script order_customer_system.py.

Insira as informações do cliente, como nome, e-mail e número de telefone.

Faça pedidos para o cliente.

Salve as informações do cliente e dos pedidos no banco de dados.

Procure e exiba informações do cliente e seus pedidos.


10 - Analytics for Restaurants:

Este script em Python implementa um sistema simples de analytics para um restaurante que utiliza um banco de dados SQLite para armazenar informações sobre pedidos e clientes. Aqui estão as principais funcionalidades do sistema:

Funcionalidades Principais:

Classe Analytics

Inicializa uma conexão com o banco de dados SQLite.

Método get_total_orders para obter o número total de pedidos.

Método get_total_customers para obter o número total de clientes.

Método get_popular_dishes para obter os pratos mais populares com base no número de pedidos.

Método close_connection para fechar a conexão com o banco de dados.


Instruções de Uso

Execute o script analytics_system.py.

Obtenha o total de pedidos, o total de clientes e os pratos mais populares.

Os resultados serão exibidos no console.


SQLITE:
![Alt text](https://github.com/Rychardsson/Online-Food-Delivery-Service-PYTHON-DJANGO/blob/main/imagem/Captura%20de%20tela%202023-12-12%20220849.png?raw=true)
