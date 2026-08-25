<?php

    class Conta{
        public $saldo;

        function __construct()
        {
            $this->saldo = 0;
        }

        function depositar($d){
            $this->saldo = $this->saldo+$d;
            echo "\nSaldo atualizado: $this->saldo";
        }

        function sacar($s){
            if ($this->saldo >= $s){
                $this->saldo = $this->saldo - $s;
                echo "\nSaldo atualizado: $this->saldo";
                return;
            }
            echo "\nSaldo insuficiente";
        }

        function exibir_saldo(){
            echo "\nSaldo atual: $this->saldo";
        }
    }

    $thiago = new Conta();
    $thiago->exibir_saldo();
    $thiago->depositar(1000);
    $thiago->sacar(650);
    $thiago->sacar(650);

?>