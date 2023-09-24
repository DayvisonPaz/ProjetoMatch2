let contador = 1
function mudarNome(x){
    document.getElementById("erro").innerHTML =`${x} ${contador}`
contador+=1
}

function registrar(){
    console.log('alguem digitou algo')
}