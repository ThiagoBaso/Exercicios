<?php

    abstract class Funcioanrio {
        protected $nome;

        public function __construct($nome)
        {
            $this->nome = $nome;
        }

        abstract function calcularSalario();

        public function getName() {
            echo "$this->nome\n";
        }

        public function setName($nome) {
            $this->nome = $nome;
        }

    }

    class Gerente extends Funcioanrio {
        public function calcularSalario() {
            echo "4000\n";
        }
    }

    class Asistente extends Funcioanrio {
        public function calcularSalario() {
            echo "1800\n";
        }
    }


    $gerente = new Gerente("Thiago");
    $gerente->getName();
    $gerente->calcularSalario();
    $asistente = new Asistente("Pedro");
    $asistente->getName();
    $asistente->calcularSalario();

?>