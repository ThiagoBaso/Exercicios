<?php

$a = readline("Valor 1: \n");
$b = readline("Valor 2: \n");

echo "Escolha a operação: \n1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão \n";
$c = readline("");

switch ($c){
    case 1:
        echo "soma: ". ($a + $b);
        break;
    case 2:
        echo "subtração: ". ($a - $b);
        break;
    case 3:
        echo "multiplicação: ". ($a * $b);
        break;
    case 4:
        echo "divisão: ". ($a / $b);
        break;
}

?>