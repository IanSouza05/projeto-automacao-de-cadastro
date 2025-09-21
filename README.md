Projeto para automação de Cadastro de Produtos

Este projeto em Python usa a biblioteca PyAutoGUI para automatizar o cadastro de produtos em um sistema web, e Pandas para leitura de dados a partir de um arquivo CSV.

🚀 Funcionalidades

- Faz login automático no sistema.
- Lê dados de produtos de um arquivo produtos.csv.
- Preenche os campos do formulário (código, marca, tipo, categoria, preço, custo e observação).
- Envia o cadastro automaticamente.
- Ignora campos de observação vazios para evitar escrever "NaN".

🛠️ Tecnologias utilizadas

- Python
- PyAutoGUI
- Pandas

📂 Estrutura do CSV

O arquivo produtos.csv contem as seguintes colunas:

codigo, marca, tipo, categoria, preco_unitario, custo, obs

▶️ Como executar

- Clone este repositório
- Instale as dependências: pip install pyautogui - pip install pandas
- Ajuste no código as coordenadas de clique (x, y) conforme a sua tela. (Isso varia de tela para tela)
- Execute (⚠️Durante a execução, não mexa no mouse e teclado, pois o PyAutoGUI vai controlar sua máquina.)
