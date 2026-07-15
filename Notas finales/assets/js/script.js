// NOTAS HTML
let nota1html = +prompt("ingresa nota 1 para el ramo HTML")
let nota2html = +prompt("ingresa nota 2 para el ramo HTML")
let nota3html = +prompt("ingresa nota 3 para el ramo HTML")
let promedioHTML = (nota1html + nota2html + nota3html) / 3

let tdnota1html = document.getElementById("nota1HTML")
let tdnota2html = document.getElementById("nota2HTML")
let tdnota3html = document.getElementById("nota3HTML")
let tdpromediohtml = document.getElementById("promedioHTML")

tdnota1html.innerHTML = nota1html
tdnota2html.innerHTML = nota2html
tdnota3html.innerHTML = nota3html
tdpromediohtml.innerHTML = promedioHTML

// NOTAS CSS
let nota1css = +prompt("ingresa nota 1 para el ramo CSS")
let nota2css = +prompt("ingresa nota 2 para el ramo CSS")
let nota3css = +prompt("ingresa nota 3 para el ramo CSS")
let promediocss = (nota1css + nota2css + nota3css) / 3

let tdnota1css = document.getElementById("nota1CSS")
let tdnota2css = document.getElementById("nota2CSS")
let tdnota3css = document.getElementById("nota3CSS")
let tdpromediocss = document.getElementById("promedioCSS")

tdnota1css.innerHTML = nota1css
tdnota2css.innerHTML = nota2css
tdnota3css.innerHTML = nota3css
tdpromediocss.innerHTML = promediocss

// NOTAS JAVA
let nota1java = +prompt("ingresa nota 1 para el ramo JAVA")
let nota2java = +prompt("ingresa nota 2 para el ramo JAVA")
let nota3java = +prompt("ingresa nota 3 para el ramo JAVA")
let promediojava = (nota1java + nota2java + nota3java) / 3

let tdnota1java = document.getElementById("nota1JAVA")
let tdnota2java = document.getElementById("nota2JAVA")
let tdnota3java = document.getElementById("nota3JAVA")
let tdpromediojava = document.getElementById("promedioJAVA")

tdnota1java.innerHTML = nota1java
tdnota2java.innerHTML = nota2java
tdnota3java.innerHTML = nota3java
tdpromediojava.innerHTML = promediojava