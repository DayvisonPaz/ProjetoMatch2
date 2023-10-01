
async function verificar(){
    let cep = 36960000
    let age = 10/12/2023
    let data = {
        cache: "no-cache",
        method: "POST",
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            'tweet': age,
        }),
    }
    await fetch('http://127.0.0.1:5000/api/age',data).then(res => res.json())
      .then(data => {
        console.log(data);
      })
    
    }
    verificar()