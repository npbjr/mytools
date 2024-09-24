class App {
    
    constructor(document){
        this.document = document;
        console.log(this.document);
        this.document.addEventListener('DOMContentLoaded', ()=>{
            this.onDocumentReady();
        });  
    }
    text = "Please input your video url below";
    index = 0;
    runTextAnimation = () =>{
        if (this.index < this.text.length) {
            this.document.getElementById("message").innerHTML += this.text.charAt(this.index);
            this.index++;
            setTimeout(this.runTextAnimation, 50); 
        }
        else{
          setTimeout(() => {
                this.document.getElementById("message").innerHTML = ""; 
                this.index = 0; 
                this.runTextAnimation();
            }, 1000); 
        }
    }

    onDocumentReady() {
        this.runTextAnimation();
    }
}

const appInstance = new App(document);

