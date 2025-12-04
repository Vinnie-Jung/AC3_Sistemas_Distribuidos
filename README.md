# M3 - CRUD AWS

## 1. AWS Lambda

**O que é?**
É um serviço de computação serverless. Ele permite executar códigos sem precisar provisionar e gerenciar servidores (como instâncias EC2). O usuário paga apenas pelo tempo de computação que consome (medido em milissegundos).

**Como funciona?**
O Lambda é orientado a eventos. Ele fica "dormindo" até que algo o acorde.

Um evento ocorre (ex: uma chamada no API Gateway, um arquivo salvo no S3, ou um cronograma). \
v \
O Lambda sobe um ambiente isolado (container) instantaneamente. \
v \
Ele executa o seu código (chamado de "Função"). \
v \
Retorna o resultado e desliga o ambiente. 

**Como utilizar?**
Acessar o console do AWS Lambda.
Clicar em "Create function".
Escolher a linguagem (Python 3.14 foi escolhido).
Escrever o código no editor.
Definir um "gatilho" (Trigger), que no caso seria o API Gateway.

## 2. Amazon DynamoDB

**O que é?** 
É um banco de dados NoSQL de chave-valor e documentos. É totalmente gerenciado, o que significa que ele escala automaticamente para suportar desde 10 até milhões de requisições por segundo.

**Como funciona?** 
Diferente de bancos relacionais (SQL) com tabelas rígidas, o DynamoDB é flexível.

* Os dados são armazenados em tabelas.
* Cada item precisa apenas de uma Chave Primária (Primary Key) para ser identificado unicamente.
* Os outros atributos podem variar de item para item.
* Ele oferece latência de milissegundos (muito rápido).

**Como utilizar?**
Acessar o console do DynamoDB.

No console do DynamoDB, clicar em "Create table". \
v \
Definir o nome da tabela e a Chave de Partição (ex: Tasks). \
v \
Nas configurações, é possível deixar no modo "On-demand" (paga por leitura/escrita) ou "Provisioned" (capacidade fixa). \
v \
Para inserir ou ler dados, geralmente usa o AWS SDK dentro da função Lambda (ex: usando Python boto3 para fazer um put_item).

## 3. Amazon API Gateway

**O que é?**
É o "porteiro" da aplicação. Ele é um serviço gerenciado para criar, publicar e segurar APIs (REST, HTTP ou WebSocket). Ele atua como a "porta da frente" para que aplicações externas (Postman, Frontend, Apps Mobile) acessem seus dados ou lógicas.

**Como funciona?**

* Ele recebe a requisição HTTP (GET, POST, PUT, DELETE) do cliente.
* Ele pode validar a autorização do usuário.
* Ele encaminha a requisição para o serviço de backend (neste caso, o AWS Lambda).
* Ele pega a resposta do Lambda e devolve para o cliente.

**Como utilizar?**
No console do API Gateway, escolha criar uma "REST API" ou "HTTP API".

Criar um Recurso (o caminho da URL, ex: /usuarios). \
v \
Criar um Método (ex: POST). \
v \
Configurar a "Integração" apontando para a Função Lambda. \
v \
Clicar em "Deploy" para gerar uma URL pública que pode ser testada no Postman, Curl, VSCode Thunder Client, etc.

## 4. AWS IAM (Identity and Access Management)

**O que é?** 
É o serviço de segurança e controle de acesso da AWS. Ele define "quem" (autenticação) pode fazer "o quê" (autorização).

**Como funciona?** 
Ele utiliza políticas (documentos JSON) para dar permissões.
Para funcionar, o Lambda precisa de permissão para escrever no DynamoDB. Não é necessária senha no código; apenas se atribui uma Role ao Lambda que diz: "Esta função tem permissão para usar o PutItem na tabela X".

**Como utilizar?**
No console do IAM, ir em "Roles" e criar uma nova. \
v \
Selecionar "AWS Service" e escolher "Lambda" (pois é o Lambda que vai assumir essa identidade). \
v \
Anexar políticas de permissão (AmazonDynamoDBFullAccess foi utilizada). \
v \
Ao criar a função Lambda, associar essa Role a ela. 

## Execução

Foi utilizado o curl para testar cada rota.

Rotas:
- tasks/create_task
- tasks/delete_task
- tasks/get_task
- tasks/get_tasks_by_id
- tasks/list_tasks
- tasks/update_task

**URL:**
https://h3a9by6n0a.execute-api.us-east-1.amazonaws.com/tasks

**Manipulação de tarefa:**

```
curl -X POST -H "Content-Type: application/json" -d '{"title":"Teste","description":"Criado pelo curl","date":"2025-12-03"}' https://h3a9by6n0a.execute-api.us-east-1.amazonaws.com/tasks
```

Obs: 
1) "title":"Teste","description":"Criado pelo curl","date":"2025-12-03" representa o conteúdo passado
2) -X é o parâmetro que determina o método HTTP (Ex: GET, POST, PUT, DELETE)
3) -H é o parâmetro de header, especificando o formato json
4) -d é o parâmetro do conteúdo que está sendo enviado

**Listar todas as tarefas:**
```
curl https://h3a9by6n0a.execute-api.us-east-1.amazonaws.com/tasks
```

**Filtrar por data:**
```
curl https://h3a9by6n0a.execute-api.us-east-1.amazonaws.com/tasks/date/2025-12-03
```

**GET por ID:**
```
curl https://h3a9by6n0a.execute-api.us-east-1.amazonaws.com/tasks/{ID_AQUI}
```
