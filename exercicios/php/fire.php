<?php

$width = 200;
$height = 95;

$fire = array_fill(0, $width * $height, 0);

for ($j = 0; $j < $width; $j++) {
    $fire[($height - 1) * $width + $j] = 9;
}

//echo $fire[($width * $height)-1];

while (True){

    for($i = 0; $i < $height-1; $i++){
        for($j = 0; $j < $width; $j++){
            $p1 = $i * $width + $j;
            $r1 = random_int(-1,1);
            $r2 = random_int(-1,0);
            $p2 = $p1 + $width + (($j == 0 && $r1 == -1) || ($j == $width - 1 && $r1 == 1) ? 0 : $r1);
            $fire[$p1] = max(0, $fire[$p2] + $r2);
        };
    };
 
    echo "\e[H\e[J";

    $print = "";

    for($i = 0; $i < $height; $i++){
        for($j = 0; $j < $width; $j++){
            if($fire[$i * $width + $j] != 0){
                //echo $fire[$i * $width + $j];
                $print .= $fire[$i * $width + $j];
            }
            else{
                //echo " ";
                $print .= " ";
            };
        };
        //echo "\n";
        $print .= "\n";
    };
    
    echo $print;
    usleep(80000); 

}

?>