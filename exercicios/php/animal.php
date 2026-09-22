<?php

    abstract class Animal {
        protected $nome;

        public function __construct($nome)
        {
            $this->nome = $nome;
        }

        abstract public function som();
    }

    class Cachorro extends Animal {
        public function som() {
            return "Latido";
        }
    }

    $cachorro = new Cachorro("Rex");
    echo $cachorro->som();
?>