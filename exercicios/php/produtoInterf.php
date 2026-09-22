<?php

    interface Produto {
        function calcularPreco();
        function exibirDetalhes();
    }

    class Livro implements Produto {
        public $preco = 19.00;
        public $detalhes = "habitos atomicos";

        public function __construct()
        {
            
        }

        function calcularPreco() {
            return $this->preco+($this->preco*0.07);
        }

        function exibirDetalhes() {
            return $this->detalhes;
        }
    }

    class Eletronico implements Produto {
        public $preco = 599.00;
        public $detalhes = "3 anos de garantia";

        function calcularPreco() {
            return $this->preco-($this->preco*0.15);
        }

        function exibirDetalhes() {
            return $this->detalhes;
        }
    }

    $livro = new Livro();
    $geladeira = new Eletronico();

    echo "Geladeira\n preco: R\${$geladeira->calcularPreco()}\n detalhes: {$geladeira->exibirDetalhes()}\n";
    echo "Livro\n preco: R\${$livro->calcularPreco()}\n detalhes: {$livro->exibirDetalhes()}\n";

?>