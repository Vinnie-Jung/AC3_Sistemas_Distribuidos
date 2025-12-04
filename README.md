Foi utilizado o curl para testar cada rota.

Rotas:
- tasks/create_task
- tasks/delete_task
- task/get_task
- tasks/get_tasks_by_id
- tasks/list_tasks
- tasks/update_task

**URL:**
https://h3a9by6n0a.execute-api.us-east-1.amazonaws.com/tasks

**Manipulação de tarefa:**
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"title":"Teste","description":"Criado pelo curl","date":"2025-12-03"}' \
  https://h3a9by6n0a.execute-api.us-east-1.amazonaws.com/tasks

Obs: 
1) "\" é apenas uma quebra de linha no terminal (não é necessária)
2) -X é o parâmetro que determina o método HTTP (Ex: GET, POST, PUT, DELETE)
3) -H é o parâmetro de header, especificando o formato json
4) -d é o parâmetro do conteúdo que está sendo enviado

**Listar todas as tarefas:**
curl https://h3a9by6n0a.execute-api.us-east-1.amazonaws.com/tasks

**Filtrar por data:**
curl https://h3a9by6n0a.execute-api.us-east-1.amazonaws.com/tasks/date/2025-12-03

**GET por ID:**
curl https://h3a9by6n0a.execute-api.us-east-1.amazonaws.com/tasks/{ID_AQUI}

