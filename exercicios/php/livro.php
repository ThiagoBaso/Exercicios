<?php 

    class Livro {
        public $titulo;
        public $autor;
        public $paginas;

        function __construct($t, $a, $p)
        {
            $this->titulo = $t;
            $this->autor = $a;
            $this->paginas = $p;
        }

        function resumo() {
            echo "\n$this->titulo";
            echo "\n$this->autor";
        }

    }

    $marco = new Livro("Meditações", "Marco Aurelio", 124);
    $napoleon = new Livro("+Esperto que o Diabo", "Napoleon Hill", 76);

    $marco->resumo();
    $napoleon->resumo();
?>