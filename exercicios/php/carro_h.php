<?php

class Veiculo {
    public $marca;
    public $modelo;

    public function __construct($marca, $modelo)
    {
        $this->marca = $marca;
        $this->modelo = $modelo;
    }

    public function detalhes(){
        return "Marca: $this->marca, Modelo: $this->modelo";
    }
}

class Carro extends Veiculo{
    public $tipo;

    public function __construct($marca, $modelo, $tipo)
    {
        parent::__construct($marca,$modelo);
        $this->tipo - $tipo;
    }

    #[Override]
    public function detalhes()
    {
        return parent::detalhes() . ",Tipo: $this->tipo";
    }
}

$meuCarro = new Carro("Toyota", "Corolla", "Sedan");
echo $meuCarro->detalhes();

?>