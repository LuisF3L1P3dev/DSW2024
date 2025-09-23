Você foi contratado para desenvolver a interface de uma pequena loja virtual. Sua primeira tarefa é criar a página principal que exibe os produtos disponíveis e permite que o cliente filtre os produtos por nome em tempo real.

 

Estrutura de Dados Inicial:

const produtos = [
{ id: 1, nome: 'Notebook Gamer', categoria: 'Eletrônicos', preco: 4500 },
{ id: 2, nome: 'Cadeira de Escritório', categoria: 'Móveis', preco: 1200 },
{ id: 3, nome: 'Mouse sem fio', categoria: 'Eletrônicos', preco: 150 },
{ id: 4, nome: 'Mesa de Jantar', categoria: 'Móveis', preco: 2500 },
{ id: 5, nome: 'Teclado Mecânico', categoria: 'Eletrônicos', preco: 450 }
];

  

Estrutura HTML Inicial


<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF--8">
    <title>Vitrine da Loja</title>
</head>
<body>
    <h1>Nossa Vitrine</h1>
    <form id="form-busca">
        <label for="campo-busca">Buscar Produto:</label>
        <input type="text" id="campo-busca" placeholder="Digite o nome do produto...">
        <button type="submit">Buscar</button>
    </form>
    <hr>
    <div id="container-produtos">
        </div>
    <script src="script.js"></script>
</body>
</html>

1. Crie uma função renderizarProdutos(produtosParaRenderizar):
Esta função deve receber um array de objetos de produto como argumento.
Dentro da função, use o método .map() para transformar cada objeto do array em uma string HTML. A string deve criar um <div> com as informações do produto (nome, categoria e preço).
Ao final, junte todas as strings HTML geradas e insira o resultado no container-produtos.

2. Renderização Inicial 
Ao carregar a página, chame a função renderizarProdutos pela primeira vez, passando o array completo de produtos para exibir todos os itens na vitrine.

3. Implemente a Lógica de Filtro
Adicione um addEventListener ao formulário (<form>) para "escutar" o evento submit.
Dentro da função do evento, trate-a para que o formulário seja enviado, mas a página não seja recarregada.
Obtenha o texto digitado pelo usuário no campo de busca. A busca não deve diferenciar maiúsculas de minúsculas.
Use o método .filter() no array original de produtos para criar um novo array contendo apenas os produtos cujo nome inclua o texto da busca.
Chame a função renderizarProdutos novamente, desta vez passando o novo array filtrado.