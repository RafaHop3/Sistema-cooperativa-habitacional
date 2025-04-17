<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cooperativa Habitacional</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f9f9f9;
    }
    header {
      background-color: #003366;
      color: white;
      padding: 20px;
      text-align: center;
      font-size: 24px;
      font-weight: bold;
    }
    nav {
      display: flex;
      justify-content: space-around;
      background-color: #e0e0e0;
      padding: 10px 0;
    }
    .nav-item {
      text-align: center;
    }
    .sub-tasks {
      display: none;
      flex-direction: column;
      margin-top: 5px;
    }
    .nav-item:hover .sub-tasks {
      display: flex;
    }
    .container {
      padding: 20px;
    }
    .form-section {
      background: white;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
      max-width: 800px;
      margin: auto;
    }
    .form-group {
      margin-bottom: 15px;
    }
    .form-group label {
      display: block;
      font-weight: bold;
    }
    .form-group input, .form-group select {
      width: 100%;
      padding: 8px;
      margin-top: 5px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
    .dependents-container {
      margin-top: 10px;
    }
    .dependent-input {
      margin-bottom: 10px;
    }
  </style>
</head>
<body>
  <header>
    COOPERATIVA HABITACIONAL DOS EMPREGADOS DA EMPRESA BRASILEIRA DE CORREIOS E TELÉGRAFOS
  </header>

  <nav>
    <div class="nav-item">
      Cadastro
      <div class="sub-tasks">
        <a href="#cadastro">Novo Cadastro</a>
        <a href="#alterar">Alterar Cadastro</a>
      </div>
    </div>
    <div class="nav-item">
      Faturamento
      <div class="sub-tasks">
        <a href="#faturamento1">Emitir Boleto</a>
        <a href="#faturamento2">Pagamentos</a>
      </div>
    </div>
    <div class="nav-item">
      Relatórios
      <div class="sub-tasks">
        <a href="#relatorio1">Relatório Geral</a>
        <a href="#relatorio2">Buscar por CPF</a>
      </div>
    </div>
  </nav>

  <div class="container">
    <section id="cadastro" class="form-section">
      <h2>Cadastro de Cooperativado</h2>
      <div class="form-group">
        <label>Nome completo:</label>
        <input type="text" id="nomeCompleto">
      </div>
      <div class="form-group">
        <label>Possui dependentes?</label>
        <select id="possuiDependentes" onchange="mostrarDependentes()">
          <option value="nao">Não</option>
          <option value="sim">Sim</option>
        </select>
      </div>
      <div id="dependentesInfo" class="dependents-container"></div>

      <div class="form-group">
        <label>CPF:</label>
        <input type="text" id="cpf">
      </div>
      <div class="form-group">
        <label>Endereço:</label>
        <input type="text" id="endereco">
      </div>
      <div class="form-group">
        <label>Valor a ser pago (R$):</label>
        <input type="number" id="valor">
      </div>
      <div class="form-group">
        <label>Número de parcelas:</label>
        <input type="number" id="parcelas">
      </div>
      <div class="form-group">
        <label>Foto do cooperativado:</label>
        <input type="file" accept="image/*">
      </div>
    </section>
  </div>

  <script>
    function mostrarDependentes() {
      const select = document.getElementById("possuiDependentes");
      const container = document.getElementById("dependentesInfo");
      container.innerHTML = "";

      if (select.value === "sim") {
        const labelQtd = document.createElement("label");
        labelQtd.textContent = "Quantidade de dependentes:";
        const inputQtd = document.createElement("input");
        inputQtd.type = "number";
        inputQtd.min = "1";
        inputQtd.onchange = () => gerarCamposDependentes(inputQtd.value);

        container.appendChild(labelQtd);
        container.appendChild(inputQtd);
      }
    }

    function gerarCamposDependentes(qtd) {
      const container = document.getElementById("dependentesInfo");

      // Remover todos os elementos abaixo da quantidade
      while (container.children.length > 2) {
        container.removeChild(container.lastChild);
      }

      for (let i = 1; i <= qtd; i++) {
        const input = document.createElement("input");
        input.className = "dependent-input";
        input.placeholder = `Nome completo do dependente ${i}`;
        container.appendChild(input);
      }
    }
  </script>
</body>
</html>
