<?php

class Produto {
    private $nome;
    private $preco;

    public function __construct($nome, $preco) {
        $this->nome = (string) $nome;
        $this->preco = (int) $preco;
    }

    public function __destruct() {
        echo "Destruindo objeto Produto: {$this->nome}\n";
    }

    public function detalhesProduto() {
        return "Produto: {$this->nome} | Preço: R$ {$this->preco}";
    }
}

class Eletronico extends Produto {
    protected $garantia;

    public function __construct($nome, $preco, $garantia) {
        parent::__construct($nome, $preco);
        $this->garantia = (int) $garantia;
    }

    public function detalhesProduto() {
        return parent::detalhesProduto() . " | Garantia: {$this->garantia} meses";
    }
}

class Funcionario {
    protected $nome;
    protected $salario;

    public function __construct($nome, $salario) {
        $this->nome = (string) $nome;
        $this->salario = (int) $salario;
    }

    public function __destruct() {
        echo "Destruindo objeto Funcionario: {$this->nome}\n";
    }

    public function detalhesFuncionario() {
        return "Funcionário: {$this->nome} | Salário: R$ {$this->salario}";
    }
}

class Gerente extends Funcionario {
    private $setor;

    public function __construct($nome, $salario, $setor) {
        parent::__construct($nome, $salario);
        $this->setor = (string) $setor;
    }

    public function detalhesFuncionario() {
        return parent::detalhesFuncionario() . " | Setor: {$this->setor}";
    }
}

$produtoComum = new Produto("Caderno Universitário", 25);
echo $produtoComum->detalhesProduto() . "\n";

$tv = new Eletronico("Smart TV 50\"", 2800, 24);
echo $tv->detalhesProduto() . "\n\n";

$func = new Funcionario("Lucas", 3500);
echo $func->detalhesFuncionario() . "\n";

$gerente = new Gerente("Mariana", 8500, "TI & Inovação");
echo $gerente->detalhesFuncionario() . "\n\n";