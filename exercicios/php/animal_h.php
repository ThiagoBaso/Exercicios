<?php

class Animal{
    public function som(){
        return "esse animal faz um som";
    }
}

class Cachorro extends Animal{
    public function som(){
        return "esse animal late";
    }
}

$meuCachorro = new Cachorro();
echo $meuCachorro->som();

?>