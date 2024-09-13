clc
clear
warning off
pkg load symbolic
syms x(t) k y(t)

n = input("Tamaño de población n: ");
tiempo = input("Tiempo de la enfermedad: ");
printf("Ingrese número de infectados al tiempo %d: ", tiempo);
crecimiento = input(" ");

ED = diff(x) / (x*(n-x)) == k*diff(t);

SOLUCION = dsolve(ED, x(0) == 1);

y(k) = SOLUCION;

K1 = subs(SOLUCION, t, tiempo);
K1 = solve(K1 == crecimiento, k);

SOLUCION = y(K1);

x(t) = SOLUCION;

expand(SOLUCION);

printf("Ecuación que expresa la cantidad x(t) de infectados que hay en el tiempo t: \n\n");

disp(SOLUCION)

#Ahora, para la grafica buscamos el tiempo máximo donde todo el mundo se infectó
tiempoMAX = solve(SOLUCION==n-1, t);
ejeT = [tiempo];
ejeXt = [crecimiento];


#Un simple menú
do

fprintf("\n\n\tPropagación de una enfermedad\n");
fprintf("1. Conocer números de infectados al tiempo t\n");
fprintf("2. Mostrar gráfica\n");

OPCION = input("Ingrese la opción deseada: ");
  switch(OPCION)
    case 1
      time = input("Ingrese el tiempo: ");
      printf("El número de infectados es %.2f ",double(x(time)));

      ejeT = [ejeT, time];
      ejeXt = [ejeXt, double(x(time))];

    case 2
      skip = 0;
    otherwise
      skip = 0;
  endswitch
until(OPCION==2);

#Graficación desde t=0 hasta el max

grid on;
ezplot(SOLUCION, [0, double(tiempoMAX)]);
hold on;
xlabel("Población [x(t)]");
ylabel("Tiempo [t]");
title("Propagación de enfermedad");
printf("La gráfica es: ");
plot(ejeT, ejeXt, "xr");


