<?php

class Funcionario{
    public function cargo(){
        return "esse funcionario trabalho como generalista";
    }
}

class Gerente extends Funcionario{
    public function cargo(){
        return "esse funcionario trabalho como gerente";
    }
}

$gerente = new Gerente();
echo $gerente->cargo();

?>