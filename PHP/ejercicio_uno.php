<?php 
//Creamos un array de tamaño 30:
$votos = array_fill(0, 30, 0);

//Repartimos los 5000 votos de manera aleatoria:
for($i = 0; $i<5000; $i++){
$voto = rand(0, 29);
$votos[$voto]++;
}

//Ordenamos los votos de mayor a menor:
arsort($votos);

//Imprimimos los votos obtenidos por cada candidato:
echo "\nVOTOS OBTENIDOS POR CADA CANDIDATO: <br>";
$suma_de_votos = 0;
foreach($votos as $candidato => $votos_obtenidos){
    echo "\nCandidato (".($candidato+1)."): ".$votos_obtenidos. "<br>";
    $suma_de_votos = $suma_de_votos + $votos_obtenidos;
}

//Comprobación de que la suma de votos de 5000
$texto = "Suma de votos: ".$suma_de_votos;
$color = "red";
echo "<span style='color:".$color."'>".$texto."</span>";

?> 