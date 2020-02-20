query = document.getElementById("query")
results = document.getElementById("results")
header = document.getElementById("header")

/* “A meddil, emblim of honna, simbil of integiddy, mokk of estimm, and glory…” - George Herriman, "Krazy Kat" */ 

const expressions = [
    "euphonious expressions", 
    "melodious mottoes", 
    "mellifluous maxims", 
    "cunning coinages", 
    "charming collocations", 
    "enchanting euphemisms", 
    "eye-catching expressions", 
    "lovesome locutions", 
    "nifty neologisms", 
    "pulchritudinous polysyllables", 
    "telegenic terms",
    "glad glyphs",
    "radiant runes",
    "striking symbols"]

function get_submit_button_text() {
    number_of_expressions = expressions.length;
    i = Math.floor(Math.random() * (number_of_expressions));
    document.getElementById("glad_glyphs").innerHTML = expressions[i];
}

window.addEventListener('load', (event) => {
    get_submit_button_text()
})


