<?php

class Funcionario {
    protected $nome;
    protected $salario;

    public function __construct($nome, $salario) {
        $this->nome = $nome;
        $this->salario = $salario;
    }

    public function getNome() {
        return $this->nome;
    }

    public function calcularSalario() {
        return $this->salario;
    }
}

class Programador extends Funcionario {
    private $horasExtras;
    private $valorHoraExtra;

    public function __construct($nome, $salario, $horasExtras = 0, $valorHoraExtra = 50.00) {
        parent::__construct($nome, $salario);
        $this->horasExtras = $horasExtras;
        $this->valorHoraExtra = $valorHoraExtra;
    }

    public function calcularSalario() {
        return $this->salario + ($this->horasExtras * $this->valorHoraExtra);
    }
}

class Designer extends Funcionario {
    private $projetosEntregues;
    private $bonusPorProjeto;

    public function __construct($nome, $salario, $projetosEntregues = 0, $bonusPorProjeto = 250.00) {
        parent::__construct($nome, $salario);
        $this->projetosEntregues = $projetosEntregues;
        $this->bonusPorProjeto = $bonusPorProjeto;
    }


    public function calcularSalario() {
        return $this->salario + ($this->projetosEntregues * $this->bonusPorProjeto);
    }
}

$dev = new Programador("Carlos", 5000.00, 10, 60.00); // Salário base 5000 + (10h * R$ 60)
$designer = new Designer("Ana", 4500.00, 4, 250.00);  // Salário base 4500 + (4 projetos * R$ 250)

printf("Funcionário: %s | Salário Final: R$ %.2f\n", $dev->getNome(), $dev->calcularSalario());
printf("Funcionária: %s | Salário Final: R$ %.2f\n", $designer->getNome(), $designer->calcularSalario());