<?php

class Pessoa {
    public $nome;
    public $idade;

    public function __construct($nome, $idade)
    {
        $this->nome = $nome;
        $this->idade = $idade;
    }

    public function apresentar(){
        return "Nome: $this->nome, Idade: $this->idade";
    }
}

class Aluno extends Pessoa{
    public $curso;

    public function __construct($nome, $idade, $curso)
    {
        parent::__construct($nome,$idade);
        $this->curso = $curso;
    }

    #[Override]
    public function apresentar()
    {
        return parent::apresentar() . ", Curso: $this->curso";
    }
}

$aluno1 = new Aluno("Thiago", "20", "ADS");
echo $aluno1->apresentar();

?>