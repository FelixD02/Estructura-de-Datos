<?php 

require_once 'vendor/autoload.php'; //Mediante Composer intallé la biblioteca faker

use Faker\Factory; //Aquí utilizo la biblioteca faker para generar nombre aleatorios

##$faker = Factory::create();

$estudiantes = array();

for($i=0; $i<6500; $i++){
    $nombre = $faker->name();

    $estudiantes[$i][0] = $nombre; //Genera un número aleatorio
    $estudiantes[$i][1] = rand(1000000, 10000000); //Genera un código de 7 digitos
    $estudiantes[$i][2] = round(rand(0,500)/100 ,2); //Genera un numero entre 0 y 500, lo divide en 100 y lo limita a 2 decimales (0.0 a 5.0)
    $estudiantes[$i][3] = rand(1, 99); //Genera un codigo para las 99 diferentes carreras
    $estudiantes[$i][4] = rand(1944, 2023); //Genera un año de ingreso entre 1994 y 2023
}
echo "PARTE UNO: \n";
echo "Ingrese el código de la carrera que desea consultar (1-99): ";
$codigo_carrera = (int)readline();

while($codigo_carrera<1 || $codigo_carrera>99){ //Si el número es menor a 0 o mayor a 99, pide de nuevo el codigo
    echo "**CÓDIGO DE CARRERA NO VALIDA** \n";
    echo "Ingrese el código de la carrera que desea consultar (1-99): ";
    $codigo_carrera = (int)readline();
}

echo "\nEstudiantes de la carrera (".$codigo_carrera.") con promedio mayor o igual a 4.0: \n";

$total_estudiantes = 0;

for($i=0; $i<6500; $i++){
    if($estudiantes[$i][3]==$codigo_carrera && $estudiantes[$i][2]>=4.0){ //Busca estudiantes de una carrera en especifico con un promedio mayor o igual a 4.0
        $total_estudiantes++;
        echo "Nombre: {$estudiantes[$i][0]} || Código: {$estudiantes[$i][1]} || Promedio: {$estudiantes[$i][2]} \n";
    }
}
echo "TOTAL DE ESTUDIANTES: {$total_estudiantes}";

echo "\n\n";

echo "PARTE DOS: \n\n";
echo "Estudiantes que ingresaron antes de 1990 y están condicionales: \n";
for($i=0; $i<count($estudiantes); $i++){
    if($estudiantes[$i][4]<1990 && $estudiantes[$i][2]>2.7 && $estudiantes[$i][2]<3.2){ //Busca estudiantes que ingresaran antes de 1990 y que tengan un promedio entre 2.7 y 3.2
        echo "Nombre: {$estudiantes[$i][0]} || Código: {$estudiantes[$i][1]} || Promedio: {$estudiantes[$i][2]} \n";
    }
}


?>