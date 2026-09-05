<?php

class Carro {
  public $placa;
  public $num_chassi;
  
  function __construct($placa, $num_chassi)
  {
    $this->placa = $placa;
    $this->num_chassi = $num_chassi;
  }

  function acelerar($velocidade) {
    echo "Velocidade do carro de placa $this->placa é $velocidade km/h";
  }
}

$uno = new Carro('ABC123', 12345);

$uno->acelerar(56);

?>