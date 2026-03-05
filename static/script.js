function runCode(){

let code = document.getElementById("code").value

fetch("/run",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({code:code})
})
.then(res=>res.json())
.then(data=>{
document.getElementById("output").innerText = data.output
})

}