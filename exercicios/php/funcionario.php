<?php

    class Funcionario
    {
        public $nome;
        public $rg;
        public $cpf;
        public $data_nascimento;
        public $cargo;
        public $salario;

        function __construct()
        {
            $this->salario = 4500.00;
        }

        function promocao($taxa){
            $this->salario = $this->salario + ($this->salario * $taxa);
            echo "\n Novo salario: $this->salario"; 
        }
    }

    $thiago = new Funcionario();
    $thiago->promocao(0.10);

?>