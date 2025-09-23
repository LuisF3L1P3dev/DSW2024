const produtos = [
  { id: 1, nome: 'Notebook Gamer', categoria: 'Eletrônicos', preco: 4500 },
  { id: 2, nome: 'Cadeira de Escritório', categoria: 'Móveis', preco: 1200 },
  { id: 3, nome: 'Mouse sem fio', categoria: 'Eletrônicos', preco: 150 },
  { id: 4, nome: 'Mesa de Jantar', categoria: 'Móveis', preco: 2500 },
  { id: 5, nome: 'Teclado Mecânico', categoria: 'Eletrônicos', preco: 450 }
];


const containerProdutos = document.querySelector('#container-produtos');

const renderizarProdutos = produtos.map((produto) => {
  return `
    <div class = "produto">
      <h2>${produto.nome}</h2>
      <p>Categoria: ${produto.categoria}</p>
      <p>Preço: R$ ${produto.preco.toFixed(2)}</p>
    </div>
  `;
});

containerProdutos.innerHTML = renderizarProdutos.join('');
console.log(containerProdutos);

// Formulario

const meuForm = document.querySelector('#form-busca');

meuForm.addEventListener('submit', (event) => {
  event.preventDefault();
  console.log('Formulário enviado!');
  const campoBusca = document.querySelector('#campo-busca')
  const elementoBuscado = campoBusca.value.toLowerCase();
  console.log('Elemento buscado:', elementoBuscado);
})
