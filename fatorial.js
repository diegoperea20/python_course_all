function factorial(numeros){
 let lista=[];
 let resultado=1;
    while (numeros !=1){
        lista.push(numeros);
        numeros=numeros-1;}
 console.log(lista);
 //for (let numero in lista){
    
   // resultado=numero;   } 
 lista.forEach(numero => resultado=resultado*numero);
 console.log("Terminado,  el factorial es: ", resultado);    
}        

let numeros=5;
factorial(numeros);